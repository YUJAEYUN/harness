# Team Roster — 상세 멤버 구성 및 스폰 템플릿

이 문서의 "팀"은 논리적 그룹핑일 뿐, `TeamCreate`로 만드는 실제 팀 객체가 아니다. 이 세션에는 정식 Agent Team API(`TeamCreate`/`TaskCreate`/`TeamDelete`)가 없고, `Agent`(이름 붙여 백그라운드 스폰) + `SendMessage`(이름으로 이어서 대화) + `TaskOutput`/`TaskStop`(상태 확인/중지)만 있다. 의존관계는 도구가 아니라 **PM이 스폰 순서로 직접 관리**한다.

## 목차
- 웨이브 1: 리서치 멤버 구성 (8명)
- 웨이브 2: 시나리오 멤버 구성 (7명)
- Agent 스폰 예시
- 순서 관리 원칙

---

## 웨이브 1: 리서치 (8명)

| 이름 | subagent_type | 스킬 | 출력 |
|--------|--------------|------|------|
| research-team-lead | `research-team-lead` (커스텀) | `team-synthesis-review`, `data-sourcing-protocol` | `01_research_synthesis.md`, `01_research_escalations.md` |
| semiconductor | `semiconductor-analyst` | `semiconductor-cycle-analysis`, `data-sourcing-protocol` | `01_semiconductor-analyst_report.md` |
| macro | `macro-economist` | `macro-liquidity-analysis`, `data-sourcing-protocol` | `01_macro-economist_report.md` |
| geopolitical | `geopolitical-analyst` | `geopolitical-risk-analysis`, `data-sourcing-protocol` | `01_geopolitical-analyst_report.md` |
| microstructure | `market-microstructure-analyst` | `market-microstructure-analysis`, `data-sourcing-protocol` | `01_market-microstructure-analyst_report.md` |
| valuation | `valuation-quant-analyst` | `valuation-decomposition`, `data-sourcing-protocol` | `01_valuation-quant-analyst_report.md` |
| historical | `historical-market-analyst` | `historical-crash-comparison`, `data-sourcing-protocol` | `01_historical-market-analyst_report.md` |
| behavioral | `behavioral-finance-analyst` | `behavioral-signal-analysis`, `data-sourcing-protocol` | `01_behavioral-finance-analyst_report.md` |

### 1단계 — 7명 동시 스폰 (한 메시지에서 병렬 Agent 호출)

```
Agent(name: "semiconductor", subagent_type: "semiconductor-analyst", model: "opus", run_in_background: true,
  prompt: "코스피 반도체 급락 저점 분석 하네스의 반도체 산업 조사를 담당합니다.
           semiconductor-cycle-analysis, data-sourcing-protocol 스킬을 사용하세요.
           분석 기준일: {date}. raw 데이터 경로(있는 경우): _workspace/kospi-bottom/00_input/.
           출력: _workspace/kospi-bottom/01_semiconductor-analyst_report.md")

Agent(name: "macro", subagent_type: "macro-economist", model: "opus", run_in_background: true, prompt: "...")
Agent(name: "geopolitical", subagent_type: "geopolitical-analyst", model: "opus", run_in_background: true, prompt: "...")
Agent(name: "microstructure", subagent_type: "market-microstructure-analyst", model: "opus", run_in_background: true, prompt: "...")
Agent(name: "valuation", subagent_type: "valuation-quant-analyst", model: "opus", run_in_background: true, prompt: "...")
Agent(name: "historical", subagent_type: "historical-market-analyst", model: "opus", run_in_background: true, prompt: "...")
Agent(name: "behavioral", subagent_type: "behavioral-finance-analyst", model: "opus", run_in_background: true, prompt: "...")
```

이 7개는 서로 의존이 없으므로 **한 메시지에서 동시에** 호출한다. 완료 알림은 각각 자동으로 온다 — 폴링하지 않는다.

### 2단계 — 7명 전부 완료 후 research-team-lead 스폰

```
Agent(name: "research-team-lead", subagent_type: "research-team-lead", model: "opus",
  prompt: "당신은 리서치팀장입니다. 아래 7개 보고서를 검수하고 종합하세요.
           _workspace/kospi-bottom/01_semiconductor-analyst_report.md
           _workspace/kospi-bottom/01_macro-economist_report.md
           _workspace/kospi-bottom/01_geopolitical-analyst_report.md
           _workspace/kospi-bottom/01_market-microstructure-analyst_report.md
           _workspace/kospi-bottom/01_valuation-quant-analyst_report.md
           _workspace/kospi-bottom/01_historical-market-analyst_report.md
           _workspace/kospi-bottom/01_behavioral-finance-analyst_report.md
           team-synthesis-review 스킬을 사용하세요.
           출력: _workspace/kospi-bottom/01_research_synthesis.md, _workspace/kospi-bottom/01_research_escalations.md")
```

research-team-lead가 특정 전문가에게 재확인이 필요하다고 보고하면, PM이 `SendMessage(to: "{전문가 이름}", message: "...")`로 이어서 요청하고 결과를 research-team-lead에게 전달한다.

---

## 웨이브 2: 시나리오 (7명)

| 이름 | subagent_type | 스킬 | 출력 |
|--------|--------------|------|------|
| scenario-team-lead | `scenario-team-lead` (커스텀) | `team-synthesis-review`, `data-sourcing-protocol` | `02_scenario_synthesis.md`, `02_scenario_escalations.md` |
| bull | `bull-case-builder` | `scenario-case-building`, `data-sourcing-protocol` | `02_bull-case_report.md` |
| bear-a | `bear-case-a-builder` | `scenario-case-building`, `data-sourcing-protocol` | `02_bear-case-a_report.md` |
| bear-b | `bear-case-b-builder` | `scenario-case-building`, `data-sourcing-protocol` | `02_bear-case-b_report.md` |
| red-team | `cross-red-team` | `red-team-critique` | `02_red-team_report.md` |
| quant-val | `quant-validator` | `quant-validation` | `02_quant-validation_report.md` |
| behavioral-obs | `behavioral-finance-observer` | `meta-bias-audit` | `02_behavioral-observer_report.md` |

### 순서 (병렬 1단계 + 순차 3단계 + 종합)

```
1단계 (병렬, 동시 스폰): bull, bear-a, bear-b
   ↓ 3개 전부 완료 대기
2단계 (순차 — 반드시 하나씩): red-team 스폰 → 완료 대기 → quant-val 스폰 → 완료 대기 → behavioral-obs 스폰 → 완료 대기
   ↓
3단계: scenario-team-lead 스폰 (6개 산출물 전부 입력)
```

red-team/quant-val/behavioral-obs는 이전 단계 산출물을 읽어야 하므로 **절대 동시에 스폰하지 않는다** — 순서를 지키지 않으면 레드팀이 없는데 정량검증자가 레드팀 결과를 요구하는 식으로 입력이 비어있는 채로 실행된다.

## 공통 주의사항

- 모든 `Agent` 프롬프트에는 `_workspace/kospi-bottom/00_input/`(raw 데이터 경로), 분석 기준일, 사용할 스킬, 정확한 출력 경로를 명시한다
- `model: "opus"`를 모든 스폰에 명시한다
- 병렬 스폰 가능한 것은 반드시 **한 메시지에서 동시에** 호출한다 (한 메시지에 한 개씩 순서대로 부르면 병렬 이점이 없다)
- 백그라운드로 스폰한 에이전트는 완료 후에도 이름이 유지되므로, 검수자가 재작업을 요청하면 새로 스폰하지 않고 `SendMessage(to: 그 이름, ...)`로 이어서 대화한다
