## 하네스: 코스피 반도체 급락 저점 판단

**목표:** 2026년 7월 코스피 반도체 급락의 저점 판단을 위한 정적 스냅샷 분석 — 리서치팀(9명)→시나리오팀(7명)→투자위원회(2명)를 웨이브 방식으로 조율해 IC 메모가 포함된 HTML 대시보드와 미확인 가정 문서를 생성한다. raw 시계열이 없으면 공개 기관 리서치를 A~D 증거등급과 원천 데이터 계열별로 정규화한다. 투자 조언이 아닌 프레임워크/논리검증 수준까지만 다룬다.

**트리거:** 코스피/반도체 급락 저점 분석 관련 작업 요청 시 `kospi-semiconductor-bottom-harness` 스킬을 사용하라. 단순 질문은 직접 응답 가능.

**변경 이력:**
| 날짜 | 변경 내용 | 대상 | 사유 |
|------|----------|------|------|
| 2026-07-29 | 초기 구성 (에이전트 15개, 스킬 15개, 오케스트레이터 1개) | 전체 | 코스피 반도체 급락 저점 분석 하네스 브리핑에 따른 신규 구축 |
| 2026-07-29 | 실행 메커니즘을 TeamCreate/TaskCreate 가정에서 Agent+SendMessage 실제 툴 프리미티브로 수정 | 오케스트레이터, team-roster.md | 이 세션에 정식 Agent Team API가 없음을 확인 |
| 2026-07-29 | 웨이브3(투자위원회) 신설 — risk-manager, ic-chair 에이전트 2개 + 스킬 2개 추가. 시나리오 구축자 3개에 Risk/Reward 프레임워크, scenario-team-lead에 촉매 캘린더 추가 | 전체 | "리서치 후 가설까지만" 피드백 — 헤지펀드 실제 프로세스(리스크 심사·IC 게이트)를 프레임워크 수준까지 반영, 포지션 사이징/매수 지시는 명시적으로 배제 |
| 2026-08-01 | 공개 리서치 증거 큐레이터 추가, 보고서 A~D 등급·source-family 중복 제거·역사 EPS 사이클·반등 트리거·신뢰도 게이트·첫 화면 의사결정 표 도입, P/E 기여도 부호 규약 수정 | 데이터 소싱/역사/밸류에이션/검증/대시보드/오케스트레이터 | raw 부재 시 임의 10%·20% 가정을 판별선으로 사용한 문제와 “가격 86%/이익 14%” 표현 오류를 재발 방지 |
| 2026-08-01 | 최종 HTML 쉬운말 원칙과 전문용어 회귀 테스트 추가 | 대시보드/오케스트레이터 | 내부 금융 약어와 업계 표현이 최종 사용자 화면에 그대로 노출되는 문제 방지 |
| 2026-08-02 | 실행 가능한 신뢰도 게이트·원자료 해시 계약·회귀 테스트 추가 | 오케스트레이터, run-contract, validate_run, tests | 문서형 체크리스트를 결정적 fail-closed 검증으로 전환해 원자료 변조·산식 회귀·폐기 숫자 재유입 방지 |
| 2026-08-03 | 데이터 공백 항목 2차 조사(`06/07_gap_research_*`), 전 세계 급락-회복 기저율 참고조사(`08_global_recovery_baserate`) 진행, 대시보드형 뷰 대신 아티클 형식 `research_note.html`을 직접 커밋으로 작성·반복 수정 | _workspace 산출물, output/kospi-bottom/research_note.html | dashboard.html의 첫 화면 이해도 문제를 보완하려는 시도였으나, 이 과정이 Agent 스폰 파이프라인과 신뢰도 게이트(run-contract.json)를 거치지 않고 진행돼 검증되지 않은 채 배포됨 (2026-08-04 정리 대상) |
| 2026-08-04 | `research_note.html`을 공식 최종본으로 전환, `dashboard.html`은 전문가용 상세보기(선택)로 격하. `run-contract.json` artifacts 검증 대상을 dashboard.html→research_note.html로 교체, `dashboard-assembly`/오케스트레이터 Phase 6 문서 갱신 | run-contract.json, dashboard-assembly, 오케스트레이터 Phase 6 | 사용자 확인 결과 research_note.html이 실제로 쓰이는 최종본인데 검증기·문서는 dashboard.html만 인지하고 있어 실사용 산출물이 fail-closed 게이트를 우회하던 문제 수정 |
| 2026-08-05 | 증권사 리서치 리포트(미래에셋 S-Oil 예시) 프로세스를 모티브로 `research_note.html`에 "한눈에 보기" 요약 박스, 원자료 관측값 부록표, 콜로폰(발행정보·이해관계 고지) 3종을 추가하고 `dashboard-assembly` 스킬에 동일 기준을 필수 요건으로 명문화 | output/kospi-bottom/research_note.html, dashboard-assembly | 사용자가 목표주가·매수의견 같은 투자조언 요소는 배제하되(기존 원칙 유지) 형식·프로세스의 완성도만 증권사 리포트 수준으로 끌어올리길 요청 |

## 하네스: 개인용 증권 리서치 시스템 (범용)

**목표:** 코스피 반도체처럼 특정 주제 하나에 고정된 하네스가 아니라, 사용자가 그때그때 알아보고 싶은 임의의 증권/시장 주제를 받아 재사용하는 시스템. `research-router`가 질문을 `lookup`/`explain`/`analyze`/`deep_research`로 분류하고, 결정적 코드(`research_snapshot`)가 Evidence Pack을 만든 뒤, 질문에 필요한 도메인 전문가만(상시 조직이 아니라 그때그때 스폰) 호출하고, `analyze`/`deep_research`에서는 `counter-reviewer`가 가장 강한 주장을 검토하며, `research-editor`가 확인된 사실/해석/가설/반대근거/미확인/판단변경조건 6칸으로 종합한다. 출력 스키마 자체에 목표가·추천·포지션 필드가 없어 투자 조언 요소가 구조적으로 들어갈 수 없다. 설계 근거는 `docs/personal-market-research-agent-architecture.md`.

**트리거:** 코스피/반도체 급락 저점 판단 그 자체를 다시 정밀 분석해 달라는 요청이 아닌, 그 외 모든 증권/시장 리서치 질문(개별 종목, 다른 산업, 매크로 이벤트, 포트폴리오 등)에는 `personal-market-research-harness` 스킬을 사용하라. 단순 조회는 스킬 없이도 `research-router`가 `lookup`으로 분류해 코드만으로 답할 수 있다.

**변경 이력:**
| 날짜 | 변경 내용 | 대상 | 사유 |
|------|----------|------|------|
| 2026-08-04 | `research-router`/`research-editor` 에이전트 2개와 `research-routing`/`research-editing` 스킬 2개, `research_snapshot` 결정적 파이프라인(수집·정규화·검증) 최초 구현 | .claude/agents, .claude/skills, research_snapshot/ | 코스피 하네스처럼 매 질문마다 18명 고정 팀을 부르는 방식이 범용 개인 리서치에는 맞지 않는다는 아키텍처 검토(`docs/personal-market-research-agent-architecture.md`) 반영 |
| 2026-08-05 | 상시 에이전트 `counter-reviewer`(+ `counter-review` 스킬), 범용 리포트 조립 `report-rendering` 스킬, 라우터→전문가(그때그때 스폰)→반론검토→편집자를 실제로 조율하는 `personal-market-research-harness` 오케스트레이터 스킬 신설. `research-router`/`research-editor` 협업 섹션과 `research-routing` 스킬을 새 오케스트레이터에 맞춰 갱신 | .claude/agents/counter-reviewer.md, .claude/skills/counter-review, .claude/skills/report-rendering, .claude/skills/personal-market-research-harness, research-router.md, research-editor.md, research-routing | 라우터·편집자만 있고 실제로 이 둘을 연결해 실행하는 오케스트레이터가 없었음(설계 문서의 "4단계 — 기존 딥리서치 경량화"가 미착수 상태). 사용자가 "주제가 생길 때마다 재사용할 범용 구조"를 우선순위로 요청해 이 공백을 메움 |
