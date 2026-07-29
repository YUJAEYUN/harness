---
name: behavioral-signal-analysis
description: "시장 심리 지표(공포·탐욕 지수), 투매 클라이맥스 신호, 과거 유사 패턴 조사 방법론. behavioral-finance-analyst 에이전트가 코스피 반도체 급락 저점 분석 하네스에서 시장 데이터를 조사할 때 사용. 분석 과정 자체의 편향을 점검하는 meta-bias-audit 스킬과는 다름."
---

# Behavioral Signal Analysis

`data-sourcing-protocol` 스킬의 태깅 규칙을 함께 적용한다. 이 스킬은 **시장 참여자들의 심리 데이터**를 다룬다 — 분석 과정 자체의 편향 점검(meta-bias-audit, behavioral-finance-observer 전용)과 혼동하지 않는다.

## 조사 순서

1. **공포·탐욕 지수류**: VIX, 국내 유사 지수(있는 경우) 추이
2. **투매 클라이맥스 정량 신호**: market-microstructure-analyst의 수급 데이터를 참조해 거래량 급증, 하한가 종목 수, 신용융자 반대매매 규모를 심리적 해석의 근거로 활용 (원자료 재수집 금지)
3. **과거 유사 패턴**: historical-market-analyst의 사례 데이터에서 투매 클라이맥스 국면의 공통 특징(거래량 폭증 후 안정화 등) 대조
4. **담론 편향**: 최근 뉴스·시장 코멘트에서 비관론이 과도하게 쏠려 있는지, 아니면 여전히 낙관론이 우세한지 정성적으로 조사

## 핵심 원칙: 정량 지표 우선

"시장이 패닉에 빠진 것 같다"는 식의 인상 서술은 금지한다. 항상 거래량, 변동성, 반대매매 건수 같은 측정 가능한 지표에 근거해 서술한다. 지표가 없으면 "정량적 근거 없이는 판단 보류"로 명시한다.

## 출력 시 주의

- market-microstructure-analyst, historical-market-analyst의 데이터를 인용할 때는 원출처 태그를 그대로 유지
- 담론 편향 조사에 쓴 뉴스/커뮤니티 소스는 `[WEB]`으로 태깅하고 출처·날짜 명시
