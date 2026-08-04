---
name: research-editing
description: "개인용 증권 리서치 시스템에서 Evidence Pack과 전문가 메모를 확인된 사실/해석/가설/반대근거/미확인/판단변경조건으로 분리·종합하는 방법론. research-editor 에이전트가 사용. 산출물은 항상 초안(research_draft)이며 행동 지시 필드를 포함하지 않는다."
---

# Research Editing

`docs/personal-market-research-agent-architecture.md`의 리서치 편집자 설계를 구현한다. 코스피 하네스의 `research-team-lead`/`scenario-team-lead`/`ic-chair` 세 역할이 이 시스템에서는 하나로 통합된 것이 이 스킬이다.

## 출력 게이트 — 필수, 협상 불가

출력 스키마에는 아래 6개 필드만 존재한다. `recommendation`/`order`/`target_position`/목표가/확률가중치 같은 행동 지시 필드는 **스키마 자체에 존재하지 않는다** — "쓰지 않는다"가 아니라 "그런 칸이 없다." 이건 문구 필터가 아니라 구조적 제약이며, 예외 없이 지킨다.

```json
{
  "question": "",
  "as_of": "",
  "output_class": "research_draft",
  "observed_facts": [{"statement": "", "evidence_id": ""}],
  "interpretations": [{"statement": "", "based_on": ["evidence_id"]}],
  "hypotheses": [{"statement": "", "confidence_note": ""}],
  "counter_evidence": [{"statement": "", "source": ""}],
  "unknowns": [""],
  "change_conditions": [{"if": "", "then": ""}]
}
```

## 6개 범주 분리 절차

1. **확인된 사실(observed_facts)**: Evidence Pack의 `observations`에서 `directly_observed: true`이고 Evidence ID(관측값의 `entity`+`metric`+`observed_at`+`source_id` 조합, 또는 소스별 `sha256`)를 붙일 수 있는 것만. 역산값·추정값은 여기 넣지 않는다.
2. **해석(interpretations)**: 전문가 메모가 사실에 근거해 내린 해석. 반드시 `based_on`에 어떤 확인된 사실을 근거로 했는지 Evidence ID를 명시한다. 전문가 메모가 없으면(단순 `lookup`/`explain`) 이 칸은 비워둔다.
3. **가설(hypotheses)**: 근거는 있으나 확정할 수 없는 것. `confidence_note`에 "왜 확정 못 하는지"를 적는다.
4. **반대 근거(counter_evidence)**: 반론 검토자 결과가 있으면 그대로, 없으면 빈 배열.
5. **미확인(unknowns)**: Evidence Pack의 `missing_data` 전체 + 전문가가 조사했지만 못 찾은 항목. 빠짐없이 옮긴다 — 사소해 보여도 누락하지 않는다.
6. **판단 변경 조건(change_conditions)**: "무엇이 관측되면 해석이 바뀌는지"를 `if`/`then` 쌍으로. 최소 1개 이상 있어야 완성으로 본다(없으면 아직 분석이 안 끝난 것).

## 신뢰도 규칙

- Evidence Pack `status`가 `blocked`(검증 실패)면 그 소스의 값은 `observed_facts`에 넣지 않고 `unknowns`로 내린다
- 같은 `source_family`를 여러 개의 독립 근거처럼 세지 않는다 — `data-sourcing-protocol`의 원칙과 동일
- 원문에 없는 숫자·목표가·확률을 새로 만들지 않는다. 계산이 필요한데 `calculator`가 아직 없으면 "계산 미구현"으로 `unknowns`에 남긴다
- 전문가 메모 간 사실관계가 어긋나면 삭제하지 않고 둘 다 남기되 출처를 병기한다

## 톤

산출물은 항상 `output_class: research_draft`다 — "결정"이 아니라 "초안". 사용자가 이걸 근거로 최종 판단을 내리는 것이지, 이 편집자가 판단을 대신 내리는 게 아니다.
