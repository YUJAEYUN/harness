# Team Roster — 상세 팀 구성 및 호출 템플릿

## 목차
- 웨이브 1: research-team 구성
- 웨이브 2: scenario-team 구성
- TeamCreate 호출 예시
- TaskCreate 의존관계 예시

---

## 웨이브 1: research-team (8명)

| 멤버명 | 에이전트 타입 | 스킬 | 출력 |
|--------|--------------|------|------|
| research-team-lead | `research-team-lead` (커스텀) | `team-synthesis-review`, `data-sourcing-protocol` | `01_research_synthesis.md`, `01_research_escalations.md` |
| semiconductor | `semiconductor-analyst` | `semiconductor-cycle-analysis`, `data-sourcing-protocol` | `01_semiconductor-analyst_report.md` |
| macro | `macro-economist` | `macro-liquidity-analysis`, `data-sourcing-protocol` | `01_macro-economist_report.md` |
| geopolitical | `geopolitical-analyst` | `geopolitical-risk-analysis`, `data-sourcing-protocol` | `01_geopolitical-analyst_report.md` |
| microstructure | `market-microstructure-analyst` | `market-microstructure-analysis`, `data-sourcing-protocol` | `01_market-microstructure-analyst_report.md` |
| valuation | `valuation-quant-analyst` | `valuation-decomposition`, `data-sourcing-protocol` | `01_valuation-quant-analyst_report.md` |
| historical | `historical-market-analyst` | `historical-crash-comparison`, `data-sourcing-protocol` | `01_historical-market-analyst_report.md` |
| behavioral | `behavioral-finance-analyst` | `behavioral-signal-analysis`, `data-sourcing-protocol` | `01_behavioral-finance-analyst_report.md` |

### TeamCreate 예시

```
TeamCreate(
  team_name: "research-team",
  members: [
    { name: "research-team-lead", agent_type: "research-team-lead", model: "opus",
      prompt: "당신은 리서치팀장입니다. 7명 전문가의 산출물을 검수하고 종합하세요. 
               입력 경로: _workspace/kospi-bottom/00_input/. 전문가 산출물 대기 후 검수를 시작하세요." },
    { name: "semiconductor", agent_type: "semiconductor-analyst", model: "opus",
      prompt: "코스피 반도체 급락 저점 분석 하네스의 반도체 산업 조사를 담당합니다.
               semiconductor-cycle-analysis, data-sourcing-protocol 스킬을 사용하세요.
               분석 기준일: {date}. raw 데이터 경로(있는 경우): _workspace/kospi-bottom/00_input/.
               출력: _workspace/kospi-bottom/01_semiconductor-analyst_report.md" },
    { name: "macro", agent_type: "macro-economist", model: "opus", prompt: "..." },
    { name: "geopolitical", agent_type: "geopolitical-analyst", model: "opus", prompt: "..." },
    { name: "microstructure", agent_type: "market-microstructure-analyst", model: "opus", prompt: "..." },
    { name: "valuation", agent_type: "valuation-quant-analyst", model: "opus", prompt: "..." },
    { name: "historical", agent_type: "historical-market-analyst", model: "opus", prompt: "..." },
    { name: "behavioral", agent_type: "behavioral-finance-analyst", model: "opus", prompt: "..." }
  ]
)
```

### TaskCreate 의존관계

```
TaskCreate(tasks: [
  { title: "반도체 산업 조사", assignee: "semiconductor" },
  { title: "거시경제 조사", assignee: "macro" },
  { title: "지정학/정책 조사", assignee: "geopolitical" },
  { title: "수급/시장미시구조 조사", assignee: "microstructure" },
  { title: "밸류에이션/퀀트 조사", assignee: "valuation" },
  { title: "역사/비교시장 조사", assignee: "historical" },
  { title: "행동재무 시장데이터 조사", assignee: "behavioral" },
  { title: "리서치팀 검수·종합", assignee: "research-team-lead",
    depends_on: ["반도체 산업 조사", "거시경제 조사", "지정학/정책 조사",
                 "수급/시장미시구조 조사", "밸류에이션/퀀트 조사",
                 "역사/비교시장 조사", "행동재무 시장데이터 조사"] }
])
```

---

## 웨이브 2: scenario-team (7명)

| 멤버명 | 에이전트 타입 | 스킬 | 출력 |
|--------|--------------|------|------|
| scenario-team-lead | `scenario-team-lead` (커스텀) | `team-synthesis-review`, `data-sourcing-protocol` | `02_scenario_synthesis.md`, `02_scenario_escalations.md` |
| bull | `bull-case-builder` | `scenario-case-building`, `data-sourcing-protocol` | `02_bull-case_report.md` |
| bear-a | `bear-case-a-builder` | `scenario-case-building`, `data-sourcing-protocol` | `02_bear-case-a_report.md` |
| bear-b | `bear-case-b-builder` | `scenario-case-building`, `data-sourcing-protocol` | `02_bear-case-b_report.md` |
| red-team | `cross-red-team` | `red-team-critique` | `02_red-team_report.md` |
| quant-val | `quant-validator` | `quant-validation` | `02_quant-validation_report.md` |
| behavioral-obs | `behavioral-finance-observer` | `meta-bias-audit` | `02_behavioral-observer_report.md` |

### TaskCreate 의존관계 (순차 웨이브 내 순서 중요)

```
TaskCreate(tasks: [
  { title: "낙관 시나리오 구축", assignee: "bull" },
  { title: "비관A 시나리오 구축", assignee: "bear-a" },
  { title: "비관B 시나리오 구축", assignee: "bear-b" },
  { title: "교차 레드팀 검토", assignee: "red-team",
    depends_on: ["낙관 시나리오 구축", "비관A 시나리오 구축", "비관B 시나리오 구축"] },
  { title: "정량/통계 검증", assignee: "quant-val",
    depends_on: ["교차 레드팀 검토"] },
  { title: "행동재무 메타 감사", assignee: "behavioral-obs",
    depends_on: ["정량/통계 검증"] },
  { title: "시나리오팀 검수·종합", assignee: "scenario-team-lead",
    depends_on: ["행동재무 메타 감사"] }
])
```

3개 구축자는 병렬로 시작 가능(서로 의존 없음). red-team → quant-val → behavioral-obs는 순차적으로 이전 산출물을 입력받으므로 의존관계를 반드시 지킨다.

## 공통 주의사항

- 모든 `TeamCreate` 멤버 프롬프트에는 `_workspace/kospi-bottom/00_input/`(raw 데이터 경로), 분석 기준일, 자신의 에이전트 정의 파일(`.claude/agents/{name}.md`)과 사용할 스킬을 명시한다
- `model: "opus"`를 모든 멤버에 명시한다
- 웨이브 전환 시 반드시 `TeamDelete`로 이전 팀을 정리한 뒤 새 `TeamCreate` (세션당 1팀만 활성 가능)
