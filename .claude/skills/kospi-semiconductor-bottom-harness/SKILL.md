---
name: kospi-semiconductor-bottom-harness
description: "코스피 반도체 급락 저점 판단 분석 하네스의 총괄 오케스트레이터(PM). raw 시계열이 없으면 공개 증권사·투자은행·바이사이드 보고서를 A~D 증거등급과 원천 데이터 계열별로 정규화하고, 역사적 EPS 하강·반등 트리거를 검증한 뒤 리서치팀(9명)→시나리오팀(7명)→투자위원회(2명)를 조율해 근거 중심 HTML 대시보드와 미확인 가정 문서를 생성한다."
---

# KOSPI Semiconductor Bottom Harness — 총괄 오케스트레이터(PM)

코스피 반도체 급락(2026.7~) 저점 판단을 위한 정적 스냅샷 분석 하네스. PM(오케스트레이터, 이 스킬을 실행하는 세션 자신)이 사용자와 유일하게 소통하며, 리서치팀 → 시나리오팀 → 투자위원회(IC) 순서로 세 웨이브를 조율한다.

**투자위원회(IC) 웨이브를 왜 추가했는가:** 리서치팀·시나리오팀까지만 있으면 "가설을 세우는 데서" 끝난다. 실제 헤지펀드는 여기서 리스크 관리자가 집중도·상관관계·테일리스크를 별도로 점검하고, IC(투자위원회)가 테제의 논리적 탄탄함을 심사하는 단계를 거친다. 이 하네스도 그 구조를 재현하되, **심사 결과는 어디까지나 "이 논리가 얼마나 검증됐는가"에 대한 것이지 "사라/팔아라"가 아니다** — 포지션 사이징이나 매수 지시는 risk-manager, ic-chair 둘 다 하지 않는다. 이 경계는 `.claude/agents/ic-chair.md`, `.claude/agents/risk-manager.md`, `risk-concentration-review`/`ic-memo-synthesis` 스킬에 명시돼 있으며, 이 경계를 흐리는 방향으로 수정하지 않는다.

## 왜 웨이브 방식인가, 그리고 실제로 어떤 툴을 쓰는가

원 설계는 PM→팀장→실무자 3단 계층이다. 이걸 문자 그대로 구현하려면 "팀장이 실무자 팀을 또 만드는" 중첩 구조가 필요한데, 이 세션에서 실제로 쓸 수 있는 툴은 `TeamCreate`/`TaskCreate`/`TeamDelete` 같은 정식 Agent Team API가 아니라 다음 3개뿐이다:

| 툴 | 용도 |
|---|---|
| `Agent` | `subagent_type`(현재 등록된 18개 커스텀 에이전트 중 하나), `model: "opus"`, `prompt`, `run_in_background: true`로 이름 붙여 스폰 |
| `SendMessage` | 이름으로 특정 서브에이전트에게 메시지 (완료 후에도 이름으로 이어서 대화 가능) |
| `TaskOutput` / `TaskStop` | 백그라운드로 스폰한 에이전트의 상태 확인 / 중지 |

즉 "팀"은 공유 작업 목록이 있는 별도 객체가 아니라, **PM이 이름 붙여 스폰한 백그라운드 서브에이전트들의 집합**이다. 의존관계(예: 8개 실무 산출물 완료 후 팀장이 종합)는 TaskCreate의 `depends_on`이 아니라, **PM이 직접 순서를 관리**해서 구현한다. 자세한 스폰 예시는 `references/team-roster.md` 참조.

## 실행 모드: 백그라운드 서브에이전트 + SendMessage 조율 (웨이브 3회)

**주의**: 이 스킬 본문과 `references/team-roster.md`에 등장하는 "팀 구성", "팀원" 같은 표현은 논리적 그룹핑을 뜻할 뿐, `TeamCreate`로 만드는 실제 팀 객체가 아니다. 실행 시에는 항상 `Agent` 도구로 이름 붙여 스폰한다.

## 워크플로우

### Phase 0: 컨텍스트 확인

이 하네스는 **1회성 정적 스냅샷 분석**으로 설계됐다 (재실행 자동 감지 로직 없음).

1. `_workspace/kospi-bottom/` 존재 여부 확인
2. 미존재 → Phase 1로 진행 (최초 실행)
3. 존재 → 사용자에게 "이전 분석 결과가 있습니다. 새로 분석할까요, 아니면 특정 부분만 다시 하시겠어요?"라고 묻는다. 새 분석이면 기존 `_workspace/kospi-bottom/`를 `_workspace/kospi-bottom_{YYYYMMDD_HHMMSS}/`로 이동 후 Phase 1. 부분 수정이면 해당 에이전트만 개별 Agent 호출로 재작업(팀 전체를 다시 만들지 않음)

**왜 `kospi-bottom/`으로 네임스페이스하는가:** 이 레포의 `_workspace/`, `output/`은 여러 하네스가 공유하는 범용 스크래치/산출물 폴더다 (예: 기존 `_workspace/01_auditor_repo_audit.md` 등은 이 하네스와 무관한 이전 작업). 네임스페이스 없이 `_workspace/01_*.md`에 바로 쓰면 다른 하네스의 산출물과 뒤섞이고, Phase 0의 "존재 여부 확인"이 무관한 파일 때문에 오작동한다.

### Phase 1: 준비 — 사용자 raw 데이터 확인 (PM이 직접 질의)

1. 브리핑 3장 기준 필요 데이터 목록을 사용자에게 제시하고 raw 파일(코스피/삼성전자/SK하이닉스 OHLCV, 수급, PER·PBR 시계열 등) 제공 여부 확인
2. 제공된 파일은 `_workspace/kospi-bottom/00_input/`에 저장, 형식(컬럼 구성)을 확인해 각 팀원에게 전달할 경로를 정리
3. 미제공 항목은 리서치팀이 웹서치로 보완한다는 점을 사용자에게 안내 (data-sourcing-protocol의 WEB-교차확인/WEB-미확인 절차 적용됨을 설명)
4. 분석 기준일 확정 (오늘 날짜 기준 스냅샷)
5. `_workspace/kospi-bottom/`, `_workspace/kospi-bottom/00_input/` 생성

### Phase 2: 웨이브 1 — 리서치 (준원자료 큐레이션 → 도메인 분석 → 팀장 종합)

1. raw 12MF EPS/PER 빈티지 시계열이 없으면 **공개 리서치 증거 모드**를 활성화한다. public-research-evidence-curator를 semiconductor/macro/geopolitical/microstructure/behavioral 전문가와 병렬 스폰한다.
2. 큐레이터가 `01_public-research-evidence-registry.md`를 완성하고 semiconductor 보고서가 준비된 뒤 valuation-quant-analyst와 historical-market-analyst를 병렬 스폰한다. 두 역할의 프롬프트에 레지스트리 경로를 필수 입력으로 전달한다.
3. 8개 실무 산출물 전부 완료 알림을 받을 때까지 대기한다.
4. research-team-lead를 스폰해 8개 산출물, 증거 레지스트리, source-family map을 검수·종합하도록 지시한다.
5. research-team-lead가 검수 중 특정 전문가에게 재확인이 필요하면 PM이 해당 전문가를 이어서 호출한다.
6. research-team-lead가 `01_research_synthesis.md`와 `01_research_escalations.md`를 작성한다. 종합본 첫 부분에는 현재 판정/확인된 근거/미확인/판단 변경 조건 표가 있어야 한다.
7. PM은 에스컬레이션을 읽어두되, 분석 전제 자체를 흔드는 항목 외에는 Phase 5에서 일괄 확인한다.

### Phase 3: 웨이브 2 — 시나리오 (3명 병렬 → 순차 검토 3단 → 팀장 종합)

1. `_workspace/kospi-bottom/01_public-research-evidence-registry.md`와 `_workspace/kospi-bottom/01_research_synthesis.md`를 공통 입력으로, 3명 시나리오 구축자(bull/bear-a/bear-b)를 한 메시지에서 동시에 `Agent(..., run_in_background: true)`로 병렬 스폰
2. 3개 전부 완료되면 cross-red-team을 스폰 (증거 레지스트리와 3개 시나리오 보고서 경로 입력) → 완료되면 quant-validator를 스폰 (증거 레지스트리와 레드팀 결과까지 입력) → 완료되면 behavioral-finance-observer를 스폰 (전체 산출물 입력). 이 3단계는 각자 이전 산출물을 읽어야 하므로 **반드시 순차 스폰** — 병렬로 동시에 띄우지 않는다
3. behavioral-finance-observer까지 완료되면 scenario-team-lead를 스폰해 6개 산출물 전부를 검수·종합하도록 지시
4. 검수 중 재작업이 필요하면 Phase 2와 동일하게 PM이 `SendMessage`로 해당 역할을 재호출
5. scenario-team-lead가 `_workspace/kospi-bottom/02_scenario_synthesis.md` + `_workspace/kospi-bottom/02_scenario_escalations.md` + `_workspace/kospi-bottom/02_catalyst_calendar.md` 작성 완료

### Phase 4: 웨이브 3 — 투자위원회(IC) 심사 (risk-manager 병렬 → ic-chair 종합)

1. `_workspace/kospi-bottom/01_public-research-evidence-registry.md` + `_workspace/kospi-bottom/01_research_synthesis.md` + `_workspace/kospi-bottom/02_scenario_synthesis.md`를 입력으로 `risk-manager`를 `Agent(..., run_in_background: true)`로 스폰
2. risk-manager 완료 후, 증거 레지스트리와 그 산출물(`_workspace/kospi-bottom/03_risk-manager_report.md`)까지 포함해 `ic-chair`를 스폰 — risk-manager 없이 ic-chair를 먼저 스폰하지 않는다 (ic-chair가 risk-manager 산출물을 IC 메모에 통합해야 함)
3. ic-chair가 `_workspace/kospi-bottom/03_ic_memo.md` 작성 완료
4. ic-chair 또는 risk-manager가 `NEEDS_CLARIFICATION`을 보고하면 PM이 직접 판단 (이 웨이브는 별도 팀장이 없으므로 PM이 1·2단계 에스컬레이션을 함께 처리) — 사소하면 미확인 가정에 기록, 중요하면 다음 Phase의 일괄 질문에 포함
5. **여기서 나온 PASS/CONDITIONAL/CHALLENGE 등급은 "논리 검증 상태"이지 매수 신호가 아니다** — 대시보드에도 이 구분을 명확히 노출해야 함 (Phase 6 참조)

### Phase 5: PM 통합

1. 리서치팀·시나리오팀·투자위원회 산출물 간 정합성 확인 — 시나리오팀이 리서치팀 사실관계를, ic-chair가 시나리오팀 사실관계를 왜곡 없이 인용했는지 대조
2. **신뢰도 게이트**를 통과하지 못하면 Phase 6로 진행하지 않는다.
   - 보고서 수를 독립 source family 수로 중복 계산하지 않았는가
   - [ASSUMPTION]을 역사적 관측 임계값이나 실시간 트리거로 표시하지 않았는가
   - P/E 분해에서 평가배수·이익 기여의 부호와 합이 맞는가
   - 역산 EPS와 직접 관측 EPS를 구분했는가
   - 보고서의 본문 요약과 표 산술을 재검산했는가
   - 현재 판정에 “무엇이 확인되면 판단을 바꾸는지”가 연결됐는가
3. 리서치·시나리오·IC 에스컬레이션을 취합해 한 번에 사용자에게 확인한다.
4. 사용자 답변을 반영해 관련 종합본의 해당 항목을 최종 확정한다.
5. 하나의 결론으로 강제 수렴시키지 않는다.

### Phase 6: 산출물 생성

`dashboard-assembly` 스킬을 사용해 HTML 대시보드를 생성한다. 함께 생성할 것:
1. `output/kospi-bottom/dashboard.html` — 인터랙티브(클라이언트 사이드 UI만, 데이터는 정적) 대시보드. Risk/Reward·촉매 캘린더·IC 심사 패널 포함
2. `output/kospi-bottom/미확인_가정.md` — 확인 없이 진행한 모든 항목 (팀 내 조정 로그 + 사소해서 사용자에게 안 올린 항목 전부)
3. 세 산출물(대시보드 2곳 + 미확인가정) 모두 "투자 조언이 아님 / IC 등급은 매수 신호가 아님" 명시 (대시보드는 눈에 띄는 위치에 고정 배너)

### Phase 7: 정리 및 피드백

1. `_workspace/kospi-bottom/` 보존 (삭제하지 않음 — 사후 검증·추적용)
2. 사용자에게 결과 요약 보고 + 피드백 요청 ("개선할 부분이 있나요?")
3. `CLAUDE.md`에 하네스 포인터 등록/갱신 (Phase 5-4 형식)

## 데이터 흐름

```
[PM] → Phase1: raw데이터 확인
     → Phase2: 공개리서치 큐레이터+5개 도메인 병렬 → valuation+historical 병렬
              → research-team-lead → evidence registry + 01_research_synthesis.md
     → Phase3: Agent×3 병렬 스폰(시나리오) → red-team→quant→behavioral 순차 스폰 → scenario-team-lead 스폰 → 02_scenario_synthesis.md, 02_catalyst_calendar.md
     → Phase4: risk-manager 스폰 → ic-chair 스폰 → 03_risk-manager_report.md, 03_ic_memo.md
     → Phase5: 에스컬레이션 일괄 확인 (사용자)
     → Phase6: dashboard-assembly 스킬 → HTML + 미확인가정.md
```

## 에러 핸들링

| 상황 | 전략 |
|------|------|
| 리서치 전문가 1명 실패/무응답 | research-team-lead가 PM에게 알리면 PM이 `SendMessage`로 1회 재작업 지시, 재실패 시 `TaskStop`으로 종료하고 해당 도메인 "미수집" 명시하고 진행 |
| 시나리오 3개 구축자 중 1명 완전 실패 | scenario-team-lead가 즉시 PM에게 보고 (시나리오 균형이 깨지므로 예외적으로 즉시 에스컬레이션) |
| risk-manager 실패 | ic-chair 스폰 시 "구조적 리스크 섹션 미수집"으로 명시하고 진행 (risk-manager 없이 ic-chair만으로도 시나리오 등급 심사는 가능) |
| ic-chair 실패 | 1회 재작업 지시, 재실패 시 IC 메모 없이 대시보드 진행하고 해당 패널에 "IC 심사 미수집" 표시 |
| raw 데이터 미제공 | data-sourcing-protocol의 WEB 대체 절차로 진행, 미확인 가정에 전부 기록 |
| 12MF EPS/PER 빈티지 raw 미제공 | 공개 리서치 증거 모드 활성화. A/B등급 원문 표·차트를 수집하고 source family 중복 제거. C등급 단독 임계값 금지 |
| 산출물 간 사실관계 불일치 (하위 웨이브가 상위 웨이브 원자료를 잘못 인용) | PM이 Phase 5에서 발견 시 해당 에이전트를 `SendMessage`로 이어서 호출해 재작업 지시 |
| 사용자가 Phase 5 질문에 답 없이 진행 요청 | 후보값 중 더 보수적인(비관 쪽에 가까운) 값을 채택하고 미확인 가정에 그 판단 근거 명시 |

## 테스트 시나리오

### 정상 흐름
1. 사용자가 "코스피 반도체 저점 분석해줘"로 트리거
2. Phase 0에서 최초 실행 확인, Phase 1에서 raw 데이터 여부 확인(사용자가 일부만 보유)
3. Phase 2에서 공개 리서치 큐레이터와 독립 도메인 조사 → valuation·historical 분석 → research-team-lead 종합
4. Phase 3에서 시나리오 3명 병렬 구축 + 레드팀·정량검증·행동재무관찰 순차 완료 후 scenario-team-lead 종합 + 촉매 캘린더
5. Phase 4에서 risk-manager → ic-chair 순차 완료, 시나리오별 PASS/CONDITIONAL/CHALLENGE 등급 산출
6. Phase 5에서 미해결 에스컬레이션 2건을 사용자에게 일괄 질문, 답변 반영
7. Phase 6에서 대시보드 + 미확인가정 문서 생성
8. 예상 결과: `output/kospi-bottom/dashboard.html`, `output/kospi-bottom/미확인_가정.md` 생성

### 에러 흐름
1. Phase 2에서 geopolitical-analyst가 응답 없이 중지
2. research-team-lead가 1회 재작업 지시 → 재실패
3. `_workspace/kospi-bottom/01_research_synthesis.md`에 "지정학 섹션 일부 미수집" 명시하고 나머지로 진행
4. Phase 5 통합 시 PM이 이 누락을 사용자에게 알림 (대시보드에도 해당 패널에 데이터 공백 표시)

### 공개 리서치 증거 흐름
1. 12MF EPS/PER 빈티지 raw 없이 실행해 공개 리서치 증거 모드가 자동 활성화되는지 확인
2. 큐레이터가 원문 표·차트의 관측기간·정의·페이지·원 데이터 제공자를 기록하고 A~D 등급을 부여하는지 확인
3. 동일 데이터 제공자와 동일 표본을 재인용한 보고서 3개를 입력했을 때 `report n=3`, `source family n=1`로 표시되는지 확인
4. 10%·20% 이익 하향값을 입력했을 때 `[ASSUMPTION]`으로 격리되고 역사적 평균·저점 트리거 계산에서 제외되는지 확인
5. 위 조건 중 하나라도 어기면 Phase 5 신뢰도 게이트가 실패해 대시보드 생성으로 넘어가지 않는지 확인

### 밸류에이션 부호 회귀 테스트
1. 가격은 하락하고 EPS는 상승한 사례를 입력한다.
2. 로그 분해에서 평가배수 기여가 100%를 넘고 이익 기여가 음수(하락 상쇄)로 표시되는지 확인한다.
3. 두 기여의 합이 100%인지, 화면에 `가격 86% / 이익 14%`처럼 두 항목이 모두 양수로 표시되지 않는지 확인한다.

## 참고
- 팀 구성 상세, 멤버 프롬프트 템플릿: `references/team-roster.md`
- 대시보드 조립 방법: `dashboard-assembly` 스킬
- 데이터 태깅 규칙: `data-sourcing-protocol` 스킬 (모든 팀원이 사용)
- 투자조언 경계: `ic-memo-synthesis`, `risk-concentration-review` 스킬의 "절대 하지 않는 것"/"필수 문구" 섹션
