---
name: personal-market-research-harness
description: "개인용 증권/시장 리서치 총괄 오케스트레이터(PM). 임의의 리서치 질문을 research-router로 lookup/explain/analyze/deep_research 중 하나로 분류하고, 결정적 코드(research_snapshot)로 Evidence Pack을 만든 뒤 예산에 맞는 도메인 전문가와 반론 검토자를 선택적으로 호출하고 research-editor로 종합한다. 코스피 반도체 급락 저점 판단처럼 특정 주제에 고정된 18명 하네스가 아니라, 새 주제가 생길 때마다 매번 재사용하는 범용 시스템."
---

# Personal Market Research Harness — 범용 오케스트레이터(PM)

`docs/personal-market-research-agent-architecture.md`의 설계를 실제로 조율하는 PM 역할. 사용자가 어떤 리서치 주제로 질문하든 매번 새 팀을 조립하지 않고, 이 스킬 하나로 질문 성격에 맞는 최소 구성을 그때그때 짠다.

## kospi-semiconductor-bottom-harness와의 관계

`kospi-semiconductor-bottom-harness`는 "코스피/반도체 급락 저점 판단" 그 자체를 정밀 재분석해 달라는 요청 전용으로 남긴다(18명 고정 웨이브 구조, 이미 만들어진 스냅샷·검증 계약이 그 주제에 맞춰져 있음). **그 주제를 다시 요청받은 게 아니라면** — 개별 종목, 다른 산업, 매크로 이벤트, 포트폴리오 질문 등 그 외 모든 리서치는 이 스킬을 쓴다. 두 하네스는 산출물 디렉터리도 분리한다(`output/kospi-bottom/` vs `output/research/<run_id>/`).

## 상시 에이전트는 3개뿐, 도메인 전문가는 그때그때 스폰

| 역할 | 방식 |
|---|---|
| `research-router` | 상시 커스텀 에이전트. 질문 분류 + 계획 수립 |
| `counter-reviewer` | 상시 커스텀 에이전트. `analyze`/`deep_research`에서만 호출 |
| `research-editor` | 상시 커스텀 에이전트. 최종 종합, `lookup` 제외 항상 호출 |
| 도메인 전문가 | **커스텀 에이전트 파일을 만들지 않는다.** `general-purpose` Agent에 "판단 과제" 프롬프트를 실어 그때그때 스폰 — 매 질문마다 고정 인원을 부르지 않는다는 이 시스템의 핵심 원칙 그 자체 |

스폰은 `Agent` 툴 + `SendMessage`로 하고 `TeamCreate` 같은 팀 API는 쓰지 않는다(이 세션에 없음 — `kospi-semiconductor-bottom-harness`와 동일한 이유).

## 워크플로우

### Phase 1: 라우팅

1. `Agent(subagent_type: "research-router", prompt: 사용자 질문 전문 + 이전 스냅샷 경로(있으면))`를 **foreground**로 호출한다 — 이후 모든 단계가 이 결과에 의존하므로 background로 띄우고 방치하지 않는다.
2. 반환된 JSON 계획에서 `mode`, `agent_budget.max_agents`, `sources`(`existing` 재사용 가능 / `needs_new_adapter` 신규 필요), 필요한 판단 과제 목록, 반론 검토자 필요 여부를 확인한다.
3. `mode`가 `research_snapshot`의 4개 허용값(`lookup`/`explain`/`analyze`/`deep_research`) 중 하나가 아니면 라우터에게 재작업을 요청한다 — 다른 이름으로 진행하지 않는다.

### Phase 2: 스냅샷 빌드 (결정적 코드, 에이전트 아님)

1. 라우터가 나열한 소스가 전부 `existing`이면 PM이 직접 `request.json`을 작성한다 (`schemas/research-request.schema.json` 형식, `examples/research_snapshot/request.json` 참고).
2. `needs_new_adapter` 항목이 있으면: 인증 없는 정적 HTTP 자료면 `sources[].type`을 `http_csv`/`http_json`으로 추가한다. 인증·페이지네이션·PDF·브라우저 자동화가 필요하면 동적 수집기(`generated_csv`/`generated_json`)가 필요하다는 뜻이므로, **코드를 짜기 전에 사용자에게 `allow_dynamic_collectors: true` 사용을 먼저 허가받는다** — 코드 실행과 네트워크 접근을 동반하므로 자동 승인하지 않는다. 승인 후에도 `docs/static-research-runtime.md`의 계약을 그대로 따른다: 수집기는 stdout에만 레코드를 출력하고, 인증정보는 `collector.env`에 환경변수 이름만 전달한다(요청 파일에 값 직접 기입 금지).
3. `python -m research_snapshot build --request <request.json 경로> --run-dir output/research/<run_id>/run`을 실행한다.
4. `run/validation/validation_report.json`의 `status`가 `PASS`가 아니면 **여기서 멈춘다** — 실패한 체크 항목을 사용자에게 보고하고 Phase 3로 진행하지 않는다 (fail-closed. `kospi-semiconductor-bottom-harness`의 신뢰도 게이트와 같은 원칙).
5. `mode == "lookup"`이면 에이전트를 하나도 부르지 않는다. `evidence/evidence_pack.json`의 관측값을 그대로 정리해 사용자에게 답하고 종료한다 (이후 Phase는 전부 스킵).

### Phase 3: 도메인 전문가 (모드별 인원, 라우터 계획대로)

1. `explain`: 전문가 1명만 스폰
2. `analyze`: 전문가 최대 2명 — 서로 다른 판단 과제라면 한 메시지에서 병렬 스폰 가능
3. `deep_research`: 전문가 2~3명 — 병렬 스폰

각 스폰 프롬프트에 반드시 포함할 것:
- 판단 과제 정의 (`research-routing` 스킬의 8개 판단 과제 중 하나 — 시장 참여자 직함이 아니라 과제로: 예 "밸류에이션 해석가 — PER/PBR이 왜 이 값인지, 가격 요인과 이익 요인을 분해하라")
- `evidence/evidence_pack.json` 경로 (이 파일 밖의 사실을 새로 수집하지 말 것을 명시)
- "원문에 없는 숫자·목표가·확률을 만들지 말 것"
- 과제와 맞는 기존 방법론 스킬이 있으면 참고 지시 (예: 밸류에이션 분해 과제 → `valuation-decomposition`, 역사적 비교 과제 → `historical-crash-comparison`, 거시 과제 → `macro-liquidity-analysis`, 수급 과제 → `market-microstructure-analysis`, 지정학 과제 → `geopolitical-risk-analysis`, 행동재무 과제 → `behavioral-signal-analysis` — 이 스킬들은 방법론 자체는 코스피 하네스 전용이 아니므로 재사용 가능. 해당하는 기존 스킬이 없으면 지시 없이 일반 조사만 시킨다)

`general-purpose` Agent로 스폰한다 (`model: "opus"`, `run_in_background: true`). 전원 완료 알림을 받을 때까지 대기한다.

### Phase 4: 반론 검토 (`analyze`/`deep_research`에서만)

1. 전문가 전원 완료 후 `Agent(subagent_type: "counter-reviewer", prompt: evidence_pack 경로 + 전문가 메모 전체 경로)`를 스폰한다 — 전문가 메모 전체가 입력이므로 전문가들과 병렬로 띄우지 않는다.
2. `lookup`/`explain`에서는 이 단계를 건너뛴다.

### Phase 5: 장기 경로의존적 테제일 때만 — 임시 시나리오 검토 (선택, 기본은 건너뛰기)

1. 질문이 "수개월~수년 뒤 결과가 두 갈래 이상으로 크게 갈리는 구조적 장기 테제"인지 PM이 판단한다. 아니라면 이 Phase는 완전히 건너뛴다.
2. 필요하다고 판단되면 `general-purpose` 에이전트 2~3개를 "이 질문에서 가장 강한 낙관/비관 논리를 구축하라"는 임시 프롬프트로 스폰한다. `bull-case-builder`/`bear-case-a-builder`/`bear-case-b-builder` 같은 코스피 전용 고정 에이전트는 재사용하지 않는다 — 그 에이전트들의 시나리오 정의 자체가 코스피 반도체 소재에 맞춰져 있다.
3. 이 Phase를 썼다면 시나리오 결과도 Phase 6 편집자 입력에 포함한다.

### Phase 6: 편집

1. `Agent(subagent_type: "research-editor", prompt: evidence_pack 경로 + 전문가 메모 경로 전체 + 반론 검토 결과(있으면) + 시나리오 결과(있으면))`를 스폰한다.
2. 출력은 `research-editing` 스킬의 6개 필드 JSON뿐이어야 한다. `output/research/<run_id>/research_draft.json`으로 저장한다.

### Phase 7: 리포트 렌더링

1. `analyze`/`deep_research`는 `report-rendering` 스킬로 `research_draft.json` + `evidence_pack.json`을 `output/research/<run_id>/research_note.html`로 조립한다 (항상 수행).
2. `explain`은 산출물이 짧으므로 기본은 채팅 답변으로 충분하다 — 사용자가 명시적으로 문서 형태를 요청했을 때만 렌더링한다.

### Phase 8: 전달

1. 결과 요약과 함께 `research_draft.json`/`research_note.html` 경로를 사용자에게 전달한다 (`SendUserFile` 등).
2. Artifact로 공개 게시할지는 항상 먼저 사용자에게 확인한다 — 자기사용 전제 시스템이므로 기본은 비공개 전달이다.

## 에러 핸들링

| 상황 | 전략 |
|---|---|
| 질문이 모호해 라우터가 모드를 확정 못함 | 라우터가 예산이 가장 적은 모드로 임시 분류하고 이유를 명시 — PM이 그 이유를 사용자에게 되묻고 답변에 따라 재라우팅 |
| Phase 2 검증 FAIL | Phase 3 이후로 진행하지 않고, 실패한 체크 항목과 원인을 사용자에게 그대로 보고 |
| 도메인 전문가 응답 없음/실패 | 1회 재시도, 재실패 시 해당 판단 과제를 "미수집"으로 명시하고 나머지로 진행 |
| 반론 검토자가 결정적 반박을 제기 | `research-editor`가 `counter_evidence`로 반드시 반영 — 삭제·무시 금지 |
| `allow_dynamic_collectors`가 필요한데 사용자가 승인하지 않음 | 해당 소스 없이 진행하고 `missing_data`에 기록 |
| 라우터가 이미 있는 스냅샷과 같은 질문을 다시 물음 | 새로 빌드하지 않고 기존 `evidence_pack.json` 재사용 여부를 먼저 확인 (자료가 오래됐으면 사용자에게 재수집 여부 확인) |

## 절대 하지 않는 것 (research-router/research-editor와 동일 경계, 예외 없음)

- `recommendation`/`order`/`target_position`/목표가/매수의견/확률가중치 필드나 문구를 어느 단계·어느 산출물에서도 새로 만들지 않는다 — `research-editing`의 6필드 스키마 자체에 그 칸이 없다는 구조적 제약을 그대로 지킨다
- 계좌 데이터·주문 실행과 이 파이프라인을 연결하지 않는다 — 읽기 전용 리서치용
- 매 질문마다 도메인 전문가 전원을 부르지 않는다 — `research-routing` 스킬의 예산표를 넘는 `max_agents`를 쓰지 않는다
- `kospi-semiconductor-bottom-harness`의 IC(투자위원회) 개념을 이 시스템에 들여오지 않는다 — "IC"라는 명칭은 개인 도구에서 실제 투자위원회 승인으로 오해될 수 있다는 이유로 이 시스템에서는 배제됐다 (`docs/personal-market-research-agent-architecture.md` 참고)

## 참고

- 설계 근거: `docs/personal-market-research-agent-architecture.md`, `docs/static-research-runtime.md`
- 라우팅 규칙: `research-routing` 스킬
- 편집 규칙: `research-editing` 스킬
- 반론 검토 규칙: `counter-review` 스킬
- 렌더링 규칙: `report-rendering` 스킬
- 결정적 파이프라인: `research_snapshot/pipeline.py`, `research_snapshot/cli.py`
