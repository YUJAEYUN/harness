# 거시경제 리서치 보고서 — 코스피 반도체 급락 저점 분석

**작성**: macro-economist (research-team)
**분석 기준일**: 2026년 7월 30일 (일부 지표는 7월 29일 종가/발표 기준)
**적용 스킬**: `macro-liquidity-analysis`, `data-sourcing-protocol`
**데이터 조달 상황**: 사용자 제공 raw 데이터 없음 → 전 항목 WebSearch/WebFetch 기반. `[RAW]` 태그 사용 항목 0건.

> **결론 배제 원칙 준수**: 본 보고서는 거시 데이터의 사실관계와 1차 해석까지만 다룹니다. 저점 여부·매수 판단·목표가는 제시하지 않습니다.
> **역할 경계**: 실제 매매 데이터(외국인/기관/개인 순매매, 레버리지 ETF 청산, 신용융자)는 market-microstructure-analyst 영역이며, 본 보고서는 "유동성/자금조달 환경"에만 집중합니다. 수출규제·정책개입 등은 geopolitical-analyst 영역입니다.

---

## 0. 핵심 판단축용 재료 요약

`macro-liquidity-analysis` 스킬이 정의한 핵심 판단축 — **"이번 급락이 거시적 유동성 위기인가, 반도체 국지적 이벤트인가"** — 에 대한 재료를 먼저 정리합니다. (판단은 시나리오팀/IC 몫)

| 거시 스트레스 지표 | 2026년 7월 관측값 | 위기 시 통상 방향 | 실제 방향 |
|---|---|---|---|
| 원/달러 환율 | 7/1 장중 1,559.47 → 7/29 종가 1,446.7 (월간 원화 **강세** 약 6.7%) | 원화 급락(환율 급등) | **반대** |
| 국고채 금리 | 10년 -11bp대 급락(3개월 최대 낙폭), 3년 -4.4bp | 금리 급등(투매) | **반대(강세)** |
| 미국 HY 신용스프레드(OAS) | 2.77%(7/23) ~ 2.84%(7/28) | 급확대(500~2000bp) | **역사적 타이트 수준 유지** |
| 미 Fed 정책 | 3.50~3.75% 동결, **매파** 반대 3명(인상 주장) | 긴급 인하/유동성 공급 | **반대(긴축 압력)** |
| 한은 정책 | 7/16 2.50%→**2.75% 인상**(만장일치) | 인하/유동성 공급 | **반대(인상)** |
| 미 종합 PMI(7월 flash) | 53.6 — **8개월 최고** | 급락/50 이하 | **반대(개선)** |
| 한국 6월 수출 | 1,022.5억달러, **사상 첫 1,000억달러 돌파** (+70.9% YoY) | 급감 | **반대(사상 최대)** |
| 하이퍼스케일러 IG 스프레드 | 2~4년 30→40bp, 5~7년 50→60bp 확대 | — | **확대(유일한 스트레스 신호)** |

**1차 해석**: 전방위적 신용경색·유동성 위기를 시사하는 거시 지표는 확인되지 않습니다. 오히려 광범위 지표(환율·국고채·HY 스프레드·PMI·수출)는 위기와 **반대 방향**을 가리킵니다. 확인된 유일한 자금조달 스트레스는 **하이퍼스케일러 발행 채권에 국한된 국지적 스프레드 확대**입니다(5장 상세).

---

## 1. 금리·유동성 사이클

### 1-1. 한국은행 — 3년 6개월 만의 인상 전환 (급락 진행 중 결정)

`[WEB-교차확인]` 한국은행 금융통화위원회는 **2026년 7월 16일** 기준금리를 **연 2.50% → 2.75%로 0.25%p 인상**. 금통위원 **7명 전원 만장일치**. **2023년 1월 이후 3년 6개월 만의 첫 인상**으로, 그간의 인하 사이클 종료.
- 출처: [한국일보 2026-07-16](https://www.hankookilbo.com/news/article/A2026071608420005789) / [beincrypto 2026-07](https://kr.beincrypto.com/bank-of-korea-rate-hike-2026/) / [EBC](https://www.ebc.com/kr/forex/304100.html) / [이투데이 7월 금통위 종합](https://www.etoday.co.kr/news/view/2604536) — 4개 소스 인상폭·날짜·만장일치 일치

`[WEB]` 금통위가 제시한 인상 배경 3가지:
1. 물가 상승 압력이 상당 기간 지속될 것으로 예상
2. **반도체 경기 호조에 힘입어 성장세 강화**
3. 가계부채·수도권 주택가격 상승 등 금융 불균형 위험 확대
- 출처: [한국일보 2026-07-16](https://www.hankookilbo.com/news/article/A2026071608420005789)

`[WEB]` **신현송 총재 기자회견 발언** (2026-07-16):
- "반도체 호조의 파급효과" 언급, **"추가 금리인상 필요"**
- 기준금리 인상이 주가에 악재라는 주장에 **동의하지 않는다**고 명시
- 향후 추가 인상의 시기·속도는 물가 압력 정도, 경기 개선 흐름, 금융안정 상황을 점검하며 결정
- 국내 경제 평가: "반도체 부문을 중심으로 수출과 투자가 높은 증가세를 지속하고 소비도 양호한 흐름"
- 출처: [헤럴드경제](https://biz.heraldcorp.com/article/10824084) / [이투데이](https://www.etoday.co.kr/news/view/2604536) / [금통위 통화정책방향 전문](https://v.daum.net/v/20260716110353864)

`[WEB]` 시장 쟁점은 **추가 인상 시점(8월 vs 10월)** 으로 이동. 인하 논의 아님.
- 출처: [이투데이 2026-07-16](https://www.etoday.co.kr/news/view/2604728)

> **⚠ 시점상 중요**: 이 인상 결정은 **코스피 급락이 진행되던 7월 중순**에 내려졌으며, 만장일치였고, 총재는 추가 인상 필요성을 공개 언급했습니다. 즉 한국 통화당국은 급락을 **유동성 위기로 규정하고 완화 대응한 것이 아니라, 반도체 호조를 근거로 긴축을 개시**했습니다. 이는 "거시 유동성 위기" 가설에 대한 강한 반증 재료입니다.

### 1-2. 미 연준 — 동결이나 매파 반대 3명

`[WEB-교차확인]` **2026년 7월 29일 FOMC**: 연방기금금리 목표범위 **3.50~3.75% 유지**. 표결 **9-3**.
- 반대 3인: **Beth M. Hammack, Neel Kashkari, Lorie K. Logan** — 모두 **0.25%p 인상**을 선호(매파적 반대)
- **2016년 9월 이후 처음으로 3명이 동일 방향 반대**
- 출처(1차): [Federal Reserve 보도자료 2026-07-29](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm) / 교차: [CNBC 2026-07-29](https://www.cnbc.com/2026/07/29/fed-rate-decision-july-2026.html) / [Fox Business](https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-july-29-2026) / [Qz](https://qz.com/federal-reserve-rate-decision-hold-july-2026-072926)

`[WEB]` FOMC 성명 문구 (연준 1차 소스):
- 경제활동: "중동 분쟁 등에 기인한 높은 불확실성에도 **견조한 속도로 확장**", **강한 생산성 증가와 자본투자** 언급
- 고용: "고용 증가가 노동력 증가에 부합했고, 실업률은 거의 변화 없음"
- 물가: 2% 목표 대비 여전히 높음 — **"에너지를 포함한 일부 부문의 공급 충격"** 이 일부 반영
- 대차대조표: "은행시스템에 **충분한(ample) 지급준비금을 유지하는 정책을 지속**" — 증권보유 관련 별도 조정 언급 없음
- 다음 회의: **9월 15~16일**
- 출처: [Federal Reserve 2026-07-29](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm)

> **⚠ 중요**: FOMC는 급락 **직후(7/29)** 회의에서 완화가 아니라 오히려 **인상 반대표 3표**가 나왔습니다. 성명은 "자본투자 강함"을 명시했습니다. 연준은 이 급락을 금융안정 이슈로 취급하지 않았습니다.

### 1-3. 달러 유동성 환경 — QT 종료, 충분한 지급준비금

`[WEB-미확인]` **QT(양적긴축)는 2025년 12월 종료**. 팬텐데믹 대차대조표 확대분의 약 절반만 되돌림.
- 출처: [Brookings](https://www.brookings.edu/articles/how-will-the-federal-reserve-decide-when-to-end-quantitative-tightening/) — 단일 소스 성격, 다만 7/29 FOMC 성명의 "ample reserves 유지" 문구와 정합적

`[WEB-미확인]` 연준 대차대조표 **약 6.75조 달러** (2026-07-22 기준).
- 출처: [Convex/WALCL](https://convextrade.com/metrics/walcl) — 단일 소스, FRED 원계열 직접 확인 실패

`[WEB]` **상시 레포기구(SRF) 사용액**은 2026년 1월 초 0으로 하락(2025년 말 750억 달러에서). 2026년 1월 이후 사용이 2025년 10~12월 대비 **현저히 감소** — 자금시장 압박 부재 신호.
- 출처: [Wolf Street 2026-01-05](https://wolfstreet.com/2026/01/05/feds-standing-repo-facility-srf-drops-to-zero-from-75-billion-on-the-last-balance-sheet-as-yearend-liquidity-turmoil-dissolves/) / [Wolf Street 2026-03-05](https://wolfstreet.com/2026/03/05/update-on-the-feds-balance-sheet-and-its-reserve-management-purchases/)

> **데이터 공백**: 7월 급락 기간(7/2~7/29)의 SRF 일별 사용액, EFFR-IORB 스프레드, FRA-OIS 스프레드는 확인하지 못했습니다. 달러 자금시장 스트레스 여부의 결정적 증거이므로 **미확인 항목**으로 명시합니다(임의 추정 없음).

### 1-4. 한국 채권시장 — 주식 급락 중 국고채 강세(안전자산 선호)

`[WEB]` 국고채 금리 수준: **국고 3년 3.829%, 국고 10년 4.289%**, 10-3년 스프레드 **46.0bp**.
- 출처: [이투데이 채권마감](https://www.etoday.co.kr/news/view/2607957)

`[WEB]` 급락 기간 채권시장 방향:
- 2026-07-02: 증시 급락·물가 안도 속 **국고 3년 4.4bp 하락(강세)**
- 7월 하순: 이틀 연속 강세, **10년물 금리 11bp 넘게 급락 — 3개월 만의 최대 낙폭**. 미국의 이란 공습 중단에 따른 국제유가 급락 + 반도체 우려에 따른 주가 폭락이 채권 강세로 반사이익
- 출처: [KB 2026-07-02 채권마감](https://kbthink.com/news-list/view.html?newsId=20260702164048903) / [이투데이](https://www.etoday.co.kr/news/view/2607957) / [네이트/이투데이 2026-07-28](https://news.nate.com/view/20260728n28436)

`[WEB-미확인]` 동 기사 내 코스피 일간 낙폭 언급: **-732.09pt(-10.84%), 역대 최대 낙폭**. 코스닥 -59.01pt(-7.72%).
- 출처: [이투데이 채권마감](https://www.etoday.co.kr/news/view/2599768) — **지수 데이터는 market-microstructure-analyst / historical-market-analyst 영역이므로 검증을 이관**합니다. 여기서는 채권-주식 동시 관측 맥락으로만 인용.

> **1차 해석**: 주식이 급락하는 동안 한국 국고채는 **강세(금리 하락)** 였습니다. 1997·2008년형 위기에서는 주식·채권·통화가 동시에 투매되며 국고채 금리가 급등합니다. 이번에는 국내 자산시장 내부에서 **주식→채권 안전자산 이동(flight to quality)** 이 정상 작동했습니다. 원화 조달시장이 얼어붙었다는 증거는 확인되지 않습니다.

### 1-5. 신용스프레드 — 광범위 시장은 타이트, 하이퍼스케일러만 확대

**(a) 미국 광범위 하이일드**

`[WEB-교차확인]` ICE BofA US High Yield Index OAS:
- 2026년 7월 평균 **2.79%(≈279bp)**
- 2026-07-23 **2.77%**
- 2026-07-28 **2.84%(≈284bp)**
- 출처: [TradingEconomics/FRED 계열](https://tradingeconomics.com/united-states/bofa-merrill-lynch-us-high-yield-option-adjusted-spread-fed-data.html) / [govspending BAMLH0A0HYM2](https://govspending.org/series/BAMLH0A0HYM2/) / [Convex 2026-07-10 269bp](https://convextrade.com/metrics/bamlh0a0hym2) — 3개 소스 270~285bp 레인지로 수렴

`[DERIVED]` 해석 기준: HY OAS 역사적 위기 수준은 2008년 약 2,000bp, 2020년 3월 약 1,100bp, 장기 중위값 약 450~500bp. **270~285bp는 역사적으로 매우 타이트한 구간**에 해당.
- 계산식: 위 관측값(277~284bp)을 과거 위기·중위 수준과 대조한 정성 비교. 과거 수준 수치는 일반적으로 알려진 범위이며 본 조사에서 개별 URL 재확인은 하지 않았으므로, **이 비교 자체를 `[WEB-미확인]` 수준으로 취급**할 것을 권고.

**(b) 하이퍼스케일러 IG 스프레드 — 유일하게 확인된 확대**

`[WEB]` Amazon·Alphabet·Meta·Oracle 채권 스프레드(중위):
- 2~4년물: 2025년 **30bp → 40bp**
- 5~7년물: 2025년 **50bp → 60bp**
- 출처: [Yahoo Finance/Reuters](https://finance.yahoo.com/markets/stocks/articles/hyperscaler-debt-binge-pushes-yields-134825104.html) / [Sage Advisory](https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure)

`[WEB]` 2차시장 악화 신호:
- 2026년 발행 하이퍼스케일러 채권 중 가격 비교 가능한 **91개 중 78개가 2026-07-28 시점 발행 시점보다 높은 금리에 거래**. 중위 상승폭 약 **22bp**
- Apollo Global Management: 하이퍼스케일러 채권 발행 **응찰배수(cover ratio)가 2월 약 5배 → 7월 2배 미만**으로 하락
- 출처: [Yahoo/Reuters](https://finance.yahoo.com/markets/stocks/articles/hyperscaler-debt-binge-pushes-yields-134825104.html)

`[WEB]` 신용등급: **S&P가 Oracle을 BBB → BBB- 로 강등 (2026-07-09)**. 사유: 급증하는 capex, 마이너스 잉여현금흐름, 고객 집중도. Moody's는 Baa2 Negative 유지.
- 출처: [FactSet Insight 2026-07-23](https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow)

`[WEB]` 전망: UBS는 미국 크레딧 스프레드가 3분기까지 대체로 박스권, **4분기 확대**, 2027년으로 갈수록 디컴프레션 예상.
- 출처: [Sage Advisory](https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure)

> **1차 해석 (핵심)**: 광범위 하이일드는 타이트(≈280bp)한데 하이퍼스케일러 IG만 10bp 확대되고 응찰배수가 5배→2배 미만으로 붕괴했습니다. 이는 **거시 신용경색이 아니라 특정 발행군의 공급 과다·수요 포화**의 형태입니다. 다만 하이퍼스케일러 capex가 부채 의존으로 이동한 만큼(5장), 이 채널은 향후 거시로 전이될 **잠재 경로**로 모니터링 대상입니다.

> **데이터 공백**: **한국 CDS 프리미엄 현재 수준**을 확인하지 못했습니다. 검색 결과 상위에 노출된 "한국 CDS 19bp, 2008년 이후 최저" 자료는 WebFetch 결과 **2021년 5월 6일 기재부 발표**로 확인되어 **폐기**했습니다(2026년 데이터 아님). 한국 CDS·회사채 신용스프레드는 "거시 위기 vs 국지 이벤트" 판단의 직접 증거이므로 데이터 공백을 명시하고 임의 보간하지 않습니다. → **NEEDS_CLARIFICATION (2번 항목)**

---

## 2. 인플레이션 추이

### 2-1. 한국 소비자물가 — 유가 주도로 3%대 재진입

`[WEB-교차확인]` **2026년 6월 소비자물가 +3.2% YoY** (CPI 119.99, 2020=100). **2023년 12월(3.2%) 이후 최고**.
- 출처: [경향신문 2026-07-02](https://www.khan.co.kr/article/202607020811001) / [YTN 2026-07-02](https://www.ytn.co.kr/_cs/_ln_0102_202607020801031915_005.html) / [뉴스핌 2026-07-02](https://www.newspim.com/news/view/20260702000083) / [헤럴드경제](https://biz.heraldcorp.com/article/10795920) / [전자신문](https://www.etnews.com/20260702000060) — 5개 소스 3.2% 일치

`[WEB-교차확인]` **2026년 월별 CPI 경로**: 1~2월 **2.0%** → 3월 **2.2%** → 4월 **2.6%** → 5월 **3.1%** → 6월 **3.2%** (2개월 연속 3%대)
- 출처: [경향신문](https://www.khan.co.kr/article/202607020811001) / [더쎈뉴스](https://www.mhns.co.kr/news/articleView.html?idxno=752106) / 기재부 6월·7월 최근경제동향과 정합

`[WEB]` **근원물가(식료품·에너지 제외) 2.5%** — 헤드라인(3.2%)과 0.7%p 괴리.
- 출처: [기재부 2026년 7월 최근경제동향 (2026-07-15)](https://eiec.kdi.re.kr/policy/materialView.do?num=284260)

`[WEB]` 상승 요인 분해 (6월):
- **석유류 +24.7% YoY → 전체 물가 +0.93%p 기여**. 휘발유 +23.1%, 경유 +33.7%(2022년 7월 이후 최대), 등유 +23.1%
- 공업제품 +4.4% → 전체 물가 **+1.47%p** 기여
- 출처: [경향신문 2026-07-02](https://www.khan.co.kr/article/202607020811001) / [뉴스핌](https://www.newspim.com/news/view/20260702000083)

`[WEB]` **한국은행 7월 물가 전망**: 국제유가 반락 흐름과 정부 민생안정 대책 효과 반영으로 **6월보다 오름폭 둔화 예상**.
- 출처: [전자신문 2026-07-02](https://www.etnews.com/20260702000060)

> **1차 해석**: 한국 인플레이션 3.2%는 **근원 2.5% vs 헤드라인 3.2%** 구조로, 중동 분쟁발 유가 충격(석유류 +24.7%)이 주도한 **공급측 물가**입니다. 수요 과열형 인플레이션 근거는 약합니다. 다만 이 헤드라인 물가가 7/16 한은 인상의 핵심 명분이 되었으므로, **유가 반락이 지속되면 추가 인상 압력이 약화될 수 있는 구조**입니다(인하 전환 근거가 아니라 인상 속도 변수).

### 2-2. 미국 소비자물가 — 헤드라인 급락, 근원 안정

`[WEB-교차확인]` **2026년 6월 미국 CPI** (BLS, 발표 2026-07-14 08:30 ET):

| 지표 | 2026년 6월 | 2026년 5월 |
|---|---|---|
| 헤드라인 YoY | **3.5%** | 4.2% |
| 헤드라인 MoM | **-0.4%** (2020년 4월 이후 최대 월간 하락) | +0.5% |
| 근원 YoY | **2.6%** | 2.9% |
| 근원 MoM | **0.0%** | +0.2% |
| 에너지 YoY | +15.7% | +23.5% |
| 에너지 MoM | **-5.7%** | +3.9% |

- 6월 헤드라인 3.5%는 컨센서스 3.8%를 **하회**
- 휘발유 6월 **-9.7% MoM** (5월 +7.0% 급등 이후 반전), 전력 -1.0% MoM
- 출처: [usinflationcalculator (WebFetch 원문 확인)](https://www.usinflationcalculator.com/inflation/us-cpi-june-2026/100072543/) / [CNBC 2026-07-14](https://www.cnbc.com/2026/07/14/consumer-price-index-inflation-report-june-2026.html) / [EY](https://www.ey.com/en_us/insights/strategy/macroeconomics/cpi-report) / [Finance Calendar](https://www.financecalendar.com/event/us-cpi-report-july-2026/) — 헤드라인 3.5%·근원 2.6% 복수 소스 일치

> **⚠ 상충 지점 명시**: 7/29 FOMC 성명은 물가가 "에너지를 포함한 공급 충격"으로 높다고 서술했으나, 6월 CPI에서 에너지는 **-5.7% MoM으로 급락**했습니다. 두 서술은 **YoY(+15.7%) vs MoM(-5.7%)의 시점 차이**로 설명 가능하나, 연준의 매파적 톤이 6월 디스인플레 데이터를 아직 반영하지 않은 것일 가능성도 있습니다. 임의로 한쪽을 채택하지 않고 병기합니다.

### 2-3. 유가 — 급락(디스인플레 요인)이 급락장과 동시 발생

`[WEB-교차확인]` Brent 유가 7월 경로:
- **2026-07-20: $91.42** (6월 11일 이후 최고) — 미국의 이란 공습 이후 급등
- 이후 미·이란 휴전 협상 헤드라인에 리스크 프리미엄 축소 → **약 $88.28**
- 9월물 **-8.7%, $88.36 마감** — 이란이 미국의 공격 중단 지속을 조건으로 공격 유예 발표
- 7/27 시점 "Brent $90 하회"
- 출처: [CNBC 2026-07-27](https://www.cnbc.com/2026/07/27/oil-price-wti-brent-slide-as-iran-reportedly-may-halt-attacks.html) / [FX Leaders 2026-07-26](https://www.fxleaders.com/news/2026/07/26/brent-and-wti-crude-oil-prices-dive-as-selloff-accelerates-after-us-iran-ceasefire-and-markets-turn-risk-on/) / [CryptoDaily](https://cryptodaily.co.uk/2026/07/oil-price-today-brent-ceasefire-pullback) / [Al Jazeera 2026-07-08](https://www.aljazeera.com/news/2026/7/8/oil-prices-surge-as-us-strikes-iran-reversing-fall-to-pre-war-levels)

`[WEB-미확인]` WTI는 약 **$5.42(-6%) 하락, $83.80** 근방.
- 출처: [FX Leaders](https://www.fxleaders.com/news/2026/07/26/brent-and-wti-crude-oil-prices-dive-as-selloff-accelerates-after-us-iran-ceasefire-and-markets-turn-risk-on/) — 단일 소스

> **1차 해석**: 코스피 급락 기간 중 유가는 **하락**했습니다. 한국은 원유 순수입국이므로 유가 하락은 교역조건 개선·물가 하방 요인입니다. 즉 급락 기간의 거시 환경은 한국에 **불리하지 않은 방향**으로 움직였습니다. 이는 "급락이 거시 악화 때문"이라는 해석과 상충하는 재료입니다. (중동 정세의 정책적 함의는 geopolitical-analyst 영역)

---

## 3. 원/달러 환율 동향

> **역할 분담 명시**: 본 절은 **글로벌 유동성·자금조달 요인**으로서의 환율만 다룹니다. 외국인 순매도 규모·매매 패턴은 market-microstructure-analyst, 당국 개입·정책은 geopolitical-analyst 영역입니다. 아래 상관성 기술은 **인과관계 단정이 아닌 참고자료**입니다.

### 3-1. 관측값 — 6월 17년 저점 → 7월 급격한 원화 강세 반전

`[WEB-교차확인]` 주요 시점별 원/달러:

| 시점 | 수준 | 비고 |
|---|---|---|
| 2026-06-05 | **1,561.5** | **17년 만의 원화 최저** |
| 2026-07-01 시가 | 1,552.53 / 장중 고 1,559.47 | 7월 초 급등 |
| 2026-07-08 종가 | 1,498.5 | 1,500원 하회 |
| 2026-07-09 장중 저 | 1,497.5 | |
| 2026-07-28 종가 | **1,462.5** (-6.0원) | |
| 2026-07-29 종가 | **1,446.7** (-15.8원) | |
| 2026-07-30 | 약 **1,438.27** | **2월 하순 이후 최강** |

- 6/22~7/21 구간: 최고 1,559.89 / 최저 1,471.27 / 평균 1,516.00
- **월간 변화: 원화 약 +6.66% 강세**
- 12개월 변화: 원화 약 **-3.67%** (연초 대비로는 약 -2.93% 약세 — 7/16 기준 보도)
- 출처: [파이낸셜뉴스 2026-07-29](https://www.fnnews.com/news/202607291534513058) / [머니투데이 2026-07-28](https://www.mt.co.kr/economy/2026/07/28/2026072815364551633) / [TradingEconomics KRW (WebFetch, 2026-07-30 확인)](https://ko.tradingeconomics.com/south-korea/currency) / [나무위키 2025-2026 원화 고환율 사태](https://namu.wiki/w/2025-2026%EB%85%84%20%EC%9B%90%ED%99%94%20%EA%B3%A0%ED%99%98%EC%9C%A8%20%EC%82%AC%ED%83%9C) / [글로벌이코노믹 2026-07-03](https://www.g-enews.com/article/Finance/2026/07/202607031530521994cd0bfacc1c_1) / [beincrypto](https://kr.beincrypto.com/bank-of-korea-rate-hike-2026/)

### 3-2. 원화 강세 요인 (보도된 설명)

`[WEB]` TradingEconomics: 원화가 "2월 하순 이후 최강" 수준에 도달 — **수출기업의 이익 환전(exporter conversion)이 증시 변동성 국면의 외국인 자금 유출을 상쇄**.
- 출처: [TradingEconomics](https://ko.tradingeconomics.com/south-korea/currency)

`[WEB]` 7/29 원화 강세 요인: **지정학적 리스크 완화, 위험회피 심리 감소로 달러 약세**.
- 출처: [파이낸셜뉴스 2026-07-29](https://www.fnnews.com/news/202607291534513058)

`[DERIVED]` 원화 강세를 지지한 경상 요인: **6월 무역수지 361.5억 달러 흑자(사상 첫 300억 달러 초과)**. 수출대금 환전 압력이 자본유출을 압도할 수 있는 규모.
- 계산식: 6월 수출 1,022.5억달러 − 수입 661.0억달러 = 361.5억달러 (출처 수치 그대로, 4장 참조). 무역흑자 규모와 외국인 주식 순매도 규모의 직접 비교는 통화·기간 단위가 달라 본 보고서에서 수행하지 않음.

`[WEB-미확인]` 외국인 국내 주식투자 **약 413억 달러 감소**, 자본수지 대규모 유출 발생.
- 출처: [KB의 생각 2026 원·달러 환율 전망](https://kbthink.com/investment/issues/2026-krw-usd-outlook.html) — 단일 소스, 기준 시점(연간/누적/특정월) 불명확. **market-microstructure-analyst의 원화 기준 순매도 데이터와 교차 검증 필요**.

### 3-3. 1차 해석

> **핵심 재료**: 외국인이 대규모(브리핑상 7월 약 17.9조원) 순매도하는 동안 원화는 **약 6.7% 강세**를 보였습니다.
>
> - **1997·2008년 패턴**: 자본유출 → 원화 폭락 → 환헤지 손실 → 추가 유출의 악순환. 환율이 위기의 **증폭기**로 작동.
> - **2026년 7월 패턴**: 자본유출이 있었으나 **사상 최대 무역흑자에 따른 수출대금 환전 + 유가 급락 + 중동 리스크 완화**가 이를 상쇄. 환율이 **완충기**로 작동.
>
> 즉 환율 채널에서는 **외국인 자금 이탈이 거시 유동성 위기로 증폭되는 메커니즘이 확인되지 않습니다.** 이는 급락의 성격을 "거시 유동성 요인"보다 "코스피 반도체 쏠림 구조에 따른 국지적 수급 요인"으로 볼 근거를 제공합니다 — 단, **실제 매매 데이터 검증은 market-microstructure-analyst 소관**이며, 본 보고서는 유동성 환경 측면의 배경 정보만 제공합니다.
>
> **반대 방향 유보**: 원화 강세는 반도체 수출기업의 원화 환산 실적에는 역풍입니다. 이 실적 영향은 semiconductor-analyst / valuation-quant-analyst 영역으로 이관합니다.

---

## 4. 글로벌 경기 선행지표

### 4-1. 글로벌 제조업 PMI — 확장 유지, 모멘텀 둔화

`[WEB]` **J.P.Morgan Global Manufacturing PMI**: 2026년 5월 **52.7 (50개월 최고)** → 6월 **52.2** (3월 이후 최저).
- 50 상회 = 확장. **11개월 연속 확장**
- 그러나 **기업 신뢰도 8개월 최저**, 제조업체 고용은 4개월 중 3번째 감축이자 **약 1년 만의 최속 감소**
- 출처: [S&P Global / J.P.Morgan Global Manufacturing PMI 보도자료](https://www.pmi.spglobal.com/Public/Home/PressRelease/99c4c5f2e4184a7697ccaccc514a9ca6) / [LFI 분석 2026년 6월](https://www.lfiusa.com/insights/the-global-manufacturing-sugar-high-is-wearing-off)

> 민간 지표이므로 교차확인 절차 적용 대상이나, PMI는 S&P Global 독점 산출로 **단일 발표기관** 구조입니다. 2차 인용(LFI)이 원 보도자료와 52.2/52.7로 일치하여 `[WEB]`로 사용합니다.

### 4-2. 미국 PMI (7월 flash) — 제조 4개월 최저, 종합 8개월 최고

`[WEB-교차확인]` **2026년 7월 S&P Global US flash PMI** (발표 2026-07-24):
- **제조업 53.8** (6월 53.9 → 4개월 최저, 컨센서스 54.3 하회)
- **종합(Composite) 53.6** (6월 51.9 → **8개월 최고**, 컨센서스 52.2 대폭 상회) — **서비스업 주도**
- 출처: [investinglive](https://investinglive.com/news/the-july-flash-s-p-global-manufacturing-53-8-vs-54-3-estimate/) / [FXStreet](https://www.fxstreet.com/news/us-sp-global-pmi-expected-to-show-steady-business-growth-in-july-202607241000) / [cryptobriefing](https://cryptobriefing.com/us-sp-composite-pmi-july-2026-53-6/) / [NAM](https://nam.org/sp-global-flash-u-s-manufacturing-pmi-drops-to-four-month-low/) — 53.8 / 53.6 복수 소스 일치

`[WEB]` 제조업 둔화 내역:
- 생산 증가세 3월 이후 최저로 급격 둔화, 신규주문 4개월 최저
- 5~6월의 이례적 강한 재고축적 이후 **재고 축적 속도 둔화**가 헤드라인 압박
- 상쇄 요인: **공장 고용 재증가**, 납기 지연 장기화 — 단 납기 지연은 수요 강세가 아니라 **중동발 공급 교란** 때문
- 출처: [investinglive](https://investinglive.com/news/the-july-flash-s-p-global-manufacturing-53-8-vs-54-3-estimate/) / [NAM](https://nam.org/sp-global-flash-u-s-manufacturing-pmi-drops-to-four-month-low/)

> **⚠ 시점상 중요**: 이 7월 flash PMI는 **2026-07-24 발표 — 코스피 급락이 진행되던 시점**입니다. 미국 종합 PMI가 **8개월 최고치**를 기록했습니다. 글로벌 경기 침체 진입을 시사하는 선행지표 신호는 이 시점에 확인되지 않습니다.

### 4-3. 한국 제조업 PMI

`[WEB]` **S&P Global 한국 제조업 PMI**: 5월 **54.8** → 6월 **52.1** (발표 2026-07-01). 50 상회 확장 유지, 모멘텀은 2분기 초 대비 둔화.
- 출처: [FX.co](https://www.fx.co/en/forex-news/3046038) / [S&P Global 한국 PMI 보도자료](https://www.pmi.spglobal.com/Public/Home/PressRelease/70bb58bb8f804354841961b33505c3f5)

> **데이터 공백**: **7월 한국 제조업 PMI는 2026-07-30 기준 미발표** (통상 익월 초, 8월 3일경 발표 예정). 급락이 실물 심리에 미친 영향을 확인할 첫 지표이므로, **분석 기준일 시점에는 구조적으로 확인 불가**임을 명시합니다. 추정치를 만들지 않습니다.

### 4-4. 한국 실물지표 — 수출 사상 최대, 고용은 미약

`[WEB-교차확인]` **2026년 6월 수출입** (산업통상자원부, 발표 2026-07-01):
- **수출 1,022.5억 달러 (+70.9% YoY)** — **사상 첫 1,000억 달러 돌파**, 전 세계 4번째 국가
- **반도체 수출 448.2억 달러 (+199.5% YoY)** — 사상 첫 400억 달러 돌파
- 수입 661.0억 달러 (+30.1%)
- **무역수지 361.5억 달러 흑자** — 사상 첫 300억 달러 초과
- 상반기 누적: 수출 **4,967억 달러(+48.4%)** 역대 최대, 반도체 **1,924억 달러(+162.6%)** — 기존 연간 최대 실적 상회
- 출처: [아주경제 2026-07-01](https://www.ajunews.com/view/20260701093537051) / [파이낸셜뉴스 2026-07-01](https://www.fnnews.com/news/202607010906341295) / [MBC뉴스](https://imnews.imbc.com/news/2026/econo/article/6834127_36932.html) / [정책브리핑 6월 수출입동향](https://www.korea.kr/briefing/policyBriefingView.do?newsId=156769112) / [KDI 경제정책자료](https://eiec.kdi.re.kr/policy/materialView.do?num=283602) — 1,022.5억달러·+70.9%·반도체 448.2억달러 복수 소스 일치

> **⚠ 상충 수치 병기**: [헤럴드경제](https://biz.heraldcorp.com/article/10783830) 기사 제목은 "6월 수출 620억弗…반도체 188.4% 급증"으로 위 수치와 크게 다릅니다. 월중 일부 기간(1~20일) 통계이거나 다른 기준월일 가능성이 있으나 확인하지 못했습니다. **평균을 내거나 삭제하지 않고 병기**합니다. 5개 소스가 일치하는 1,022.5억 달러를 본문 기준값으로 사용하되 상충 사실을 남깁니다.

`[WEB-교차확인]` **2026년 6월 고용** (발표 2026-07-15):
- 취업자 **2,915만 4천명, +6만 3천명 YoY** — 5월 -4만명(2024년 12월 이후 17개월 만의 감소) 이후 **1개월 만에 증가 전환**
- 15세 이상 고용률 **63.4% (-0.2%p)**, 15~64세 70.2% (-0.1%p)
- 실업자 83만 4천명(+1만명), **실업률 2.8%** (전년 동월과 동일)
- 연령별: 20대 **-19만 9천명**, 60세 이상 +21만 1천명, 30대 +6만 5천명, 50대 +3천명
- 청년층(15~29세) 고용률 **43.9% (-1.7%p)**, **26개월 연속 하락**
- 출처: [아시아투데이 2026-07-15](https://www.asiatoday.co.kr/kn/view.php?key=20260715010005538) / [전자신문 2026-07-15](https://www.etnews.com/20260715000178) / [뉴스핌 2026-07-15](https://www.newspim.com/news/view/20260715000066) / [이투데이](https://www.etoday.co.kr/news/view/2603940) — +6만 3천명·63.4%·2.8% 일치

> **⚠ 오독 정정 기록**: 기재부 7월 최근경제동향에 대한 최초 WebFetch 결과는 취업자를 "630,000명 증가"로 반환했습니다. 이는 **"6.3만명"의 오독**으로, 위 4개 1차 보도(6만 3천명)와 대조해 **정정**했습니다. 원 수치를 채택합니다.

`[WEB]` **기재부 최근경제동향** 종합 평가:
- **2026년 7월호 (2026-07-15 발간)**: 수출 대폭 증가, 소비 개선 등 회복 흐름 지속. 설비투자는 **1분기 +4.4% YoY**. 소비자물가 +3.2%(농산물·석유류 주도), 근원 2.5%. 금융시장은 6월 중 **원/달러 환율과 국고채 금리 상승**, 주가는 보합, 전국 주택가격 +0.21%
- **2026년 6월호 (2026-06-12 발간, 5월/4월 데이터)**: 수출 +53.2%(일평균 +60.7%). 설비투자 4월 **-3.6% MoM**, 1분기 +6.6%. 4월 전산업생산 -0.6% MoM. 취업자 **-4만명 YoY**, 실업률 2.9%. 물가 +3.1%, 근원 2.5%
- 정부 평가 문구(6월호): *"최근 우리 경제는 수출 호조, 소비·기업심리 개선 등 경기 회복흐름이 이어지고 있으나, 중동전쟁 등에 따른 불확실성이 지속되는 가운데 물가 상승, 고용 둔화 등 민생 부담이 우려되고 있습니다"*
- 출처: [기재부/KDI 2026년 7월 최근경제동향](https://eiec.kdi.re.kr/policy/materialView.do?num=284260) / [정책브리핑 26년 6월 최근경제동향](https://www.korea.kr/news/policyNewsView.do?newsId=156766301)

> **데이터 공백 (중요)**: **2026년 6월 산업활동동향(설비투자·광공업생산)은 2026-07-31 발표 예정** — 즉 분석 기준일(7/30) **다음 날**입니다.
> 검색 과정에서 한 2차 집계 사이트가 6월 설비투자를 "**-0.1% MoM, -9.7% YoY**", 전산업생산을 "-0.3% MoM, -2.3% YoY"로 제시했으나([seonamtoday](https://seonamtoday.com/m/view.php?idx=50830&mcode=)), ① 공식 발표 전이고 ② 5월 산업활동동향의 설비투자 -0.1% MoM 수치와 중복되어 **5월 데이터의 오전재 가능성**이 높습니다. **채택하지 않고 폐기**합니다.
> 확인된 공식 수치는 **5월 산업활동동향(2026-06-30 발표)**: 전산업생산 -0.3% MoM(서비스업 +1.3%, **광공업 -3.0%**), 설비투자 **-0.1% MoM**(기계류 감소), 건설기성 +3.8% MoM.
> 출처: [정책브리핑 2026년 5월 산업활동동향](https://www.korea.kr/news/policyNewsView.do?newsId=156768746) / [KDI](https://eiec.kdi.re.kr/policy/materialView.do?num=283561&pg=&pp=&topic=C)

> **1차 해석 (한국 실물의 이중구조)**: 반도체 수출은 폭발적(+199.5%)이나, **광공업생산 -3.0% MoM, 설비투자 -0.1% MoM, 청년 고용률 26개월 연속 하락**이 병존합니다. 즉 **반도체 수출 부문과 내수·비반도체 제조업이 분리(decoupled)** 되어 있습니다. 이는 코스피 반도체 쏠림 구조가 실물에서도 대응물을 갖는다는 재료이며, "반도체 이벤트 = 한국 거시 전체 위기"라는 등치가 성립하지 않을 수 있음을 시사합니다. 동시에 반대로, **반도체 외 완충 부문이 얇다**는 취약성 재료이기도 합니다. 양방향 모두 기록합니다.

---

## 5. 하이퍼스케일러 Capex 가이던스와 실물경제 연결고리

> 본 절은 본 에이전트에게 배정된 **핵심 차별 과제**입니다: capex 둔화가 실제 경기 신호인지, 반도체 업종 국지적 이벤트인지 구분.

### 5-1. 트리거 사건의 성격 — "capex 삭감"이 아니라 "희소성 서사 붕괴"

`[WEB-교차확인]` **2026-07-01, Bloomberg 보도**: Meta가 **"Meta Compute"** 라는 클라우드 인프라 사업을 내부 검토 — 유휴 AI 컴퓨팅 파워와 모델 접근권을 외부 고객에 판매/임대.
- 출처: [CNBC 2026-07-01](https://www.cnbc.com/2026/07/01/meta-stock-cloud-ai-compute.html) / [KuCoin](https://www.kucoin.com/news/flash/meta-s-potential-excess-compute-power-sale-sparks-ai-hardware-market-correction) / [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/meta-compute-launch-sends-ai-015258040.html) / [BigGo Finance](https://finance.biggo.com/news/925ea856-432b-4eea-98a1-33777c850805)

`[WEB]` 시장 반응 (2026-07-01, 미국):
- Micron **-11%**, Intel **-9%**, AMD **-7%**, **SOX 지수 -6.3%**
- 네오클라우드: CoreWeave **-14%**, Nebius **-17%** (최대 고객이 경쟁자로 전환)
- **Meta 자체는 +9% 상승**
- 섹터 전반 약 **2,000억 달러** 시가총액 소멸
- 출처: [Memeburn](https://memeburn.com/meta-cloud-chip-stocks-selloff/) / [CNBC 2026-07-01](https://www.cnbc.com/2026/07/01/meta-stock-cloud-ai-compute.html) / [ainvest](https://news.ainvest.com/deep-topic/topic/meta-to-sell-ai-computing-power-2607/)

`[WEB]` 시장 반응 (2026-07-02, 한국): **삼성전자 -9.06%, SK하이닉스 -14.57%**.
- 출처: [Memeburn](https://memeburn.com/meta-cloud-chip-stocks-selloff/) — 개별 종목 데이터 검증은 semiconductor-analyst / market-microstructure-analyst로 이관

`[WEB]` **사건의 본질에 대한 명시적 서술**: *"AI capex는 실제로 정점에 있지 않다 — 모든 주요 하이퍼스케일러가 가장 최근 가이던스에서 대규모 지출 계획을 상향 또는 재확인했다. 시장은 capex 삭감에 반응한 것이 아니라, **capex 수익화 위계(monetization hierarchy)** 가 형성되는 데 반응했다."*
- 출처: [ainvest](https://news.ainvest.com/deep-topic/topic/meta-to-sell-ai-computing-power-2607/)

`[WEB]` **SemiAnalysis 반박 (2026-07-06)**: 네오클라우드 우려는 **"erroneous(잘못됐다)"**.
- *"우리는 두 해석 모두 잘못됐다고 보며, Meta의 데이터센터·컴퓨트 조달은 **둔화가 아니라 가속**할 것으로 본다"*
- Meta는 **2026년 상반기만에 5GW 이상**의 데이터센터 용량을 계약
- Meta 2027년 capex는 "충격적으로 높을(shockingly high)" 것으로 전망 — 2026년 대비 가속
- 근거: ① CoreWeave·Nebius 등 3자 조달 지속 ② 4개 고마진 용처(초지능 연구소, 광고추천 스케일링, **Anthropic 파트너십 약 100억 달러 예상**, SpaceX형 온디맨드 컴퓨트) ③ 초고속 "텐트" 건설 방식 ④ 프리미엄 가격·단기 유연성을 지지하는 금융 모델
- 출처: [Investing.com / SemiAnalysis 2026-07-06](https://www.investing.com/news/stock-market-news/meta-capex-to-surge-in-2027-neocloud-fears-erroneous--semianalysis-4777202)

> **1차 해석**: 트리거는 **capex 가이던스 하향이 아닙니다.** Meta가 유휴 용량을 판매한다는 사실은 ① 용량이 남는다(수요 < 공급)는 해석과 ② 용량을 수익화한다(자금조달 강화)는 해석 양쪽으로 읽힙니다. 시장은 ①로 반응했고 SemiAnalysis는 ②를 주장합니다. **"AI 반도체의 희소성 프리미엄"이라는 가격 형성 논리 자체가 훼손된 사건**으로, 성격상 **반도체·AI 인프라 밸류에이션 이벤트**이며 거시 총수요 충격의 형태가 아닙니다.

### 5-2. Capex 가이던스 실제 수치 — 상향 중

`[WEB-교차확인]` **Alphabet Q2 2026 실적 (2026-07-22)**:
- 2026년 capex 가이던스 **$180~190B → $195~205B로 상향** (한 분기 만에 재상향)
- Google Cloud 매출 **+82% YoY, $24.8B**
- 수주잔고(backlog) 한 분기에 **$50B 증가 → $514B**
- **분기 capex가 영업현금흐름을 상회, 잉여현금흐름 마이너스 전환**
- 출처: [CNBC 2026-07-22](https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html) / [Value Add VC](https://valueaddvc.com/blog/alphabet-raises-2026-ai-capex-guidance-to-205-billion-what-changed) / [Value Add VC 2](https://valueaddvc.com/blog/alphabet-205b-ai-capex-guidance-2026-what-googles-q2-earnings-raise-actually-buys)

> **⚠ 상충 수치 병기 — Alphabet 주가 반응**: CNBC 계열 보도는 발표 다음 날 **-7%**, Value Add VC는 **-5%**. 병기하며 평균내지 않습니다.
> 출처: [CNBC 2026-07-28](https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html) vs [Value Add VC](https://valueaddvc.com/blog/alphabet-raises-2026-ai-capex-guidance-to-205-billion-what-changed)

**⚠ 상충 수치 병기 — 2026년 하이퍼스케일러 capex 총액**: 소스마다 **집계 범위·시점**이 달라 값이 크게 다릅니다. 임의 선택하지 않고 전부 병기합니다.

| 값 | 집계 범위 | 출처 |
|---|---|---|
| **> $690B** (FY26, +80%↑ YoY) | 하이퍼스케일러(5개사 추정) | [FactSet Insight 2026-07-23](https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow) |
| **약 $690B** | — | [Futurum](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/) |
| **> $700B** (2025년 약 $410B 대비) | Alphabet·Amazon·Microsoft·Meta 4사 | [Value Add VC](https://valueaddvc.com/blog/alphabet-raises-2026-ai-capex-guidance-to-205-billion-what-changed) |
| **$725B** (+77% vs $410B) | 동일 4사 | [valueaddvc](https://valueaddvc.com/blog/big-tech-ai-capex-in-2025-microsoft-google-meta-amazon-and-the-spending-race) |
| **약 $750B** (전년 약 $450B 미만) | **세계 14대 상장 데이터센터 운영사** | [CNBC 2026-07-28](https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html) |
| **약 $750B** (+67% YoY) | 상위 5개 하이퍼스케일러(애널리스트 상향 추정) | [CNBC 2026-07-28](https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html) |
| **> $440B** | 상위 5개사(Amazon·MS·Alphabet·Meta·Oracle) 확정 커밋 | [Epoch AI / 관련 집계](https://epoch.ai/data-insights/ai-datacenter-share-gdp) |

**⚠ 상충 수치 병기 — 개별사 2026 capex 가이던스**:

| 기업 | 값 A | 값 B |
|---|---|---|
| Alphabet | **$195~205B** (7/22 상향 후) | $175~185B (상향 전 보도) |
| Amazon | 약 **$200B** | (일치) |
| Microsoft | 약 **$190B** (역년 기준) | (단일 소스) |
| Meta | **$125~145B** (상향 후) | **$115~135B** |

- 출처: [CNBC 2026-07-28](https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html) / [Value Add VC](https://valueaddvc.com/blog/alphabet-raises-2026-ai-capex-guidance-to-205-billion-what-changed) / [CreditSights](https://know.creditsights.com/insights/tech-raising-hyperscaler-capex-2026-estimates/)

`[WEB]` **FactSet capex 시계열** (2026-07-23):
- FY20 기준선 **$95B** → LTM(2026년 5월까지) 약 **$490B** → FY26 예상 **> $690B** → FY28 추정 **> $900B**
- 잉여현금흐름은 FY24 이후 크게 감소, **FY26에 추가 감소 예상(Microsoft 제외)**
- 출처: [FactSet Insight 2026-07-23](https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow)

> **1차 해석**: 어느 집계를 쓰더라도 **2026년 하이퍼스케일러 capex는 전년 대비 67~80% 증가 방향**입니다. **capex 둔화(감액)는 2026년 7월 시점에 데이터로 확인되지 않습니다.** 시장이 반응한 것은 capex의 **수준**이 아니라 **ROI·수익화·자금조달 구조**입니다. 총액 수치는 집계 범위 혼동이 심하므로 시나리오팀은 반드시 **범위(4사/5사/14사)를 명시해 인용**해야 합니다. → **NEEDS_CLARIFICATION (1번 항목)**

### 5-3. 자금조달 구조 전환 — capex가 부채로 이동 (거시 전이 경로)

`[WEB]` **FactSet (2026-07-23)**: 하이퍼스케일러(Alphabet·Amazon·Meta·Microsoft·Oracle)가 **거의 전액 자체조달 capex에서 대규모 외부자본 조달로 이동**.
- **증분 연간 부채가 capex의 9%(FY24) → 32%(LTM, 2026년 중반)**
- Alphabet: **$84.75B 주식 발행** (2026년 6월)
- Amazon: **$25B 채권 발행** (최근)
- Oracle: FY27에 부채·주식 합계 약 **$40B** 계획(부채 약 $20B)
- 총부채/EBITDA: 5개사 중 4개사는 약 1배 이하. **Oracle이 이례치** — OpenAI 용량 커밋과 연동된 고레버리지
- 출처: [FactSet Insight 2026-07-23](https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow)

`[WEB]` **채권 발행 규모**:
- Amazon·Alphabet·Meta·Oracle: 2026년 **7월 7일까지 약 $194B 발행** — 2025년 연간 약 $108B 대비 **+79%**
- Goldman Sachs 전망: 5개 하이퍼스케일러(Microsoft 포함) 발행액 2026년 약 **$250B**, 2027년 약 **$400B**
- 출처: [Yahoo/Reuters](https://finance.yahoo.com/markets/stocks/articles/hyperscaler-debt-binge-pushes-yields-134825104.html)

> **1차 해석 (본 보고서의 핵심 거시 발견)**: AI capex가 **자체 현금흐름 조달 → 채권시장 조달**로 구조 전환했습니다. 이는 두 가지를 의미합니다.
> 1. **금리·신용스프레드가 AI capex의 직접 변수가 되었습니다.** 과거 하이퍼스케일러 capex는 금리에 거의 둔감했으나, 이제 capex의 약 1/3이 부채 의존입니다. 이 지점에서 **거시(금리·유동성)와 반도체 수요가 처음으로 직접 연결**됩니다.
> 2. **아직 거시 위기는 아닙니다.** 광범위 HY OAS는 약 280bp로 타이트하고, 5개사 중 4개사 레버리지는 1배 이하입니다. 스트레스는 **발행군 국지적**(스프레드 +10bp, 응찰배수 5배→2배 미만, Oracle 강등)입니다.
>
> 즉 **현재는 국지적, 그러나 전이 경로가 새로 열린 상태**입니다. 이 경로의 감시 지표는 6장에 제시합니다.

### 5-4. Capex → 실물경제(설비투자·고용) 전달

**(a) 미국 데이터센터 건설 — 실물 설비투자로 이미 계상됨**

`[WEB-미확인]` 미국 데이터센터 건설 착공액: 2023년 **$14.9B** → 2024년 **$26.9B** → 2025년 **$77.7B (+190% YoY)** → **2026년 4월까지 누적 $49.5B** (전년 동기 $13.6B의 약 4배).
- 출처: [American Industrial Magazine](https://www.americanindustrialmagazine.com/blogs/industry/data-center-construction-boom-2026-statistics-costs-amp-power-demand) / [Programs.com](https://programs.com/resources/data-center-statistics/) — 2차 집계 매체, 미 Census Bureau 원계열 직접 확인 실패

`[WEB-미확인]` GDP 비중:
- AI 관련 데이터센터 건설+컴퓨트 하드웨어+네트워킹 장비 = **2026년 1분기 미국 GDP의 약 0.8%**
- 컴퓨팅 인프라 전체 = GDP의 약 **1.5%** (2015~2022 평균 약 0.7% 대비 2배)
- 출처: [Epoch AI](https://epoch.ai/data-insights/ai-datacenter-share-gdp) / [J.P. Morgan Asset Management](https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/is-ai-already-driving-us-growth/)

`[WEB-미확인]` **성장 기여도 주장 (신뢰도 유보)**:
- AI 관련 capex가 2026년 미국 GDP 성장률에 **+2.5%p**, 2027년 **+3%p 이상** 기여 전망
- **2026년 1분기 미국 경제성장의 75%가 AI 관련 capex에 기인**
- 출처: [TECHi](https://www.techi.com/ai-capex-carries-us-economy-token-factories/) / [Beta Finch](https://betafinch.com/blog/us-gdp-q1-2026-ai-spending-impact) — **저신뢰 2차 매체, 방법론 미공개**. "성장률에 +2.5%p 기여"는 GDP 성장률 자체를 크게 초과할 수 있는 수치로 산정 방식(총투자액/GDP vs 증분 기여) 확인 불가. **시나리오 근거로 인용하지 말 것을 권고.** → **NEEDS_CLARIFICATION (3번 항목)**

**(b) 고용 전달 — 약함 (구조적 특성)**

`[WEB]` 데이터센터는 **건설 완료 후 고용 인원이 매우 적음**. 공장이나 오피스 캠퍼스 대비 **임금 주도 소비를 통한 승수효과가 제한적**.
- 한 주(state) 기준 데이터센터 건설·운영에 직접 귀속된 일자리 약 **36,000개**
- 출처: [Epoch AI](https://epoch.ai/data-insights/ai-datacenter-share-gdp) / [Programs.com](https://programs.com/resources/data-center-statistics/)

**(c) 관측된 실제 고용·투자 데이터와의 대조**

| 지표 | 관측값 | 시사점 |
|---|---|---|
| 미 7월 flash 제조업 고용 | **재증가** `[WEB]` | capex 붐이 아직 고용 위축으로 전환 안 됨 |
| 글로벌 제조업 고용(6월 PMI) | 4개월 중 3번째 감축, **약 1년 최속 감소** `[WEB]` | 글로벌 제조 고용은 이미 약화 |
| 한국 6월 취업자 | **+6.3만명** (5월 -4만명에서 전환) `[WEB-교차확인]` | 미약하나 플러스 |
| 한국 청년 고용률 | 43.9%, **26개월 연속 하락** `[WEB-교차확인]` | 반도체 호황이 청년 고용으로 전달 안 됨 |
| 한국 설비투자(공식 최신, 5월) | **-0.1% MoM** `[WEB]` | 수출 +70.9%와 괴리 |
| 한국 광공업생산(5월) | **-3.0% MoM** `[WEB]` | 동일 |
| 미 FOMC 성명(7/29) | "**강한 생산성 증가와 자본투자**" `[WEB]` | 연준은 capex를 강세 요인으로 인식 |

> **1차 해석 — 배정 과제에 대한 직접 답**:
>
> **"capex 둔화가 실제 경기 신호인가, 반도체 업종 국지적 이벤트인가"**에 대한 재료를 이렇게 정리합니다.
>
> **① 애초에 capex 둔화가 데이터로 확인되지 않습니다.** 2026년 7월 시점 하이퍼스케일러 가이던스는 전원 상향 또는 재확인이며(Alphabet은 7/22 재상향), 총액은 +67~80% YoY 방향입니다. "capex 둔화 → 경기 둔화"의 첫 고리인 capex 둔화 자체가 미확인입니다.
>
> **② 시장이 반응한 것은 capex의 양이 아니라 가격결정력 서사입니다.** Meta Compute는 AI 컴퓨트의 희소성을 훼손하는 신호였고, 이는 **메모리·GPU의 마진과 밸류에이션 배수**에 직결되는 문제입니다. 성격상 **업종 국지적 이벤트**의 형태를 취합니다.
>
> **③ 다만 두 개의 실질적 거시 연결고리가 새로 존재합니다.**
> - **자금조달 채널(5-3)**: capex의 32%가 부채 의존 → 금리·스프레드가 AI 수요의 변수화. 현재 국지적이나 전이 경로 존재.
> - **성장 집중도 채널(5-4a)**: AI capex가 미 GDP의 1.5%(컴퓨팅 인프라 전체) 규모로 커져 성장 기여가 집중. 다만 정확한 기여도 수치는 저신뢰 소스뿐이라 **미확인**.
>
> **④ 고용 채널은 구조적으로 약합니다.** 데이터센터는 자본집약·저고용이므로, capex 사이클이 꺾여도 **고용을 통한 실물 파급은 시차가 길고 규모가 작을 가능성**이 있습니다. 역으로 capex 호황이 고용·소비를 지지하는 힘도 약합니다 — 한국 청년 고용률 26개월 연속 하락, 설비투자 -0.1% MoM이 반도체 수출 +199.5%와 병존하는 것이 그 방증입니다.
>
> **⑤ 시차**: capex 가이던스 변경이 실제 설비투자·고용 통계에 반영되는 시차를 정량화할 근거를 확보하지 못했습니다. 데이터센터 착공→준공 리드타임, 반도체 장비 발주→매출 인식 시차 등에 대한 신뢰 가능한 수치를 찾지 못했으므로 **임의 추정하지 않습니다**(semiconductor-analyst의 장비 수주/BB Ratio 데이터와 결합해야 함). → **NEEDS_CLARIFICATION (4번 항목)**

---

## 6. 거시 유동성 요인 vs 국지적 수급 요인 — 판단 재료 정리

> 투자 결론이 아니라, 시나리오팀·IC가 사용할 **판별 재료와 감시 지표**를 정리합니다.

### 6-1. "거시 유동성 위기" 가설을 지지하는 재료

1. `[WEB-교차확인]` **한·미 통화정책이 동시에 긴축 방향**. 한은 7/16 인상 + 추가 인상 시사, 연준 매파 반대 3표. 유동성 사이클의 **정책 지원이 없는 국면**.
2. `[WEB]` **하이퍼스케일러 자금조달 스트레스**: IG 스프레드 +10bp, 2026년 발행 91개 중 78개가 발행가 대비 금리 상승, 응찰배수 5배 → 2배 미만, Oracle BBB→BBB- 강등, 잉여현금흐름 마이너스(Alphabet).
3. `[WEB]` **capex의 32%가 부채 의존** — 금리·스프레드 상승이 AI 수요를 직접 훼손할 수 있는 신규 경로.
4. `[WEB]` **글로벌 제조업 고용 약화**: 6월 PMI 기준 약 1년 만의 최속 감소, 기업 신뢰도 8개월 최저.
5. `[WEB]` **한국 내수·비반도체 취약**: 광공업생산 -3.0% MoM(5월), 설비투자 -0.1% MoM, 청년 고용률 26개월 연속 하락 — 반도체 외 완충 부문이 얇음.
6. `[WEB]` UBS 전망: 미 크레딧 스프레드 **4분기 확대** 예상.

### 6-2. "반도체·AI 국지적 이벤트" 가설을 지지하는 재료

1. `[WEB-교차확인]` **원화 강세**: 외국인 대규모 순매도 중에도 월간 약 +6.7% 강세, 2월 하순 이후 최강(1,438~1,447). 1997·2008년형 통화 악순환 부재.
2. `[WEB]` **한국 국고채 강세**: 주식 급락 중 10년물 -11bp대(3개월 최대 낙폭). 원화 조달시장 정상 작동, flight to quality 정상 기능.
3. `[WEB-교차확인]` **미 HY OAS 약 277~284bp** — 역사적 타이트 구간. 광범위 신용경색 부재.
4. `[WEB-교차확인]` **미 7월 종합 PMI 53.6 — 8개월 최고** (급락 진행 중 7/24 발표). 경기 침체 선행 신호 부재.
5. `[WEB-교차확인]` **한국 6월 수출 사상 첫 1,000억 달러**(+70.9%), 무역흑자 사상 첫 300억 달러 초과. 실물 수출 엔진 훼손 없음.
6. `[WEB]` **연준·한은 모두 급락을 금융안정 이슈로 취급하지 않음**. 한은은 오히려 반도체 호조를 인상 근거로 제시하고 총재가 "인상이 주가에 악재라는 주장에 동의하지 않는다"고 명시.
7. `[WEB]` **유가 하락**(Brent $91.42 → $88대) — 한국 교역조건·물가에 우호적 방향. 거시 환경이 악화된 것이 아님.
8. `[WEB]` **capex 가이던스 상향 중**(Alphabet 7/22 $195~205B로 재상향). 트리거는 capex 삭감이 아니라 희소성 서사 훼손.
9. `[WEB]` **하락 집중도**: 7/1 미국 하락은 반도체·네오클라우드 집중(Micron -11%, CoreWeave -14%, Nebius -17%)이나 **Meta 자체는 +9%**. 시장 전체 리스크오프가 아니라 **밸류체인 내 재배분**의 형태.
10. `[WEB]` **SemiAnalysis 반박**: Meta 상반기 5GW 이상 계약, 2027년 capex 가속 전망.

### 6-3. 감시 지표 (거시 → 국지 전이 여부 판별용)

시나리오팀이 확률 업데이트에 쓸 수 있는 거시 조기경보 지표를 제안합니다.

| 감시 지표 | 현재 값 | 전이 시사 임계 방향 | 발표 주기 |
|---|---|---|---|
| 미 HY OAS | 약 280bp | 400bp 상회 시 광범위 신용 스트레스 전환 | 일별(FRED) |
| 하이퍼스케일러 IG 스프레드 | 2~4년 40bp / 5~7년 60bp | 추가 확대 + 응찰배수 1배대 고착 | 발행 시 |
| 하이퍼스케일러 채권 응찰배수 | 2배 미만 (2월 5배) | 1배대 진입 = 발행 실패 리스크 | 발행 시 |
| 원/달러 | 약 1,438~1,447 | 1,560(6/5 고점) 재돌파 = 통화 채널 악순환 개시 | 일별 |
| 국고 10년 | 4.289% | 주식 급락 중 **동반 상승** 전환 = 국내 조달 스트레스 | 일별 |
| 미 종합 PMI | 53.6 (8개월 최고) | 50 하회 | 월 2회(flash/final) |
| 한국 제조업 PMI | 6월 52.1 | **7월치 8월 초 발표 — 급락 반영 첫 지표** | 월별 |
| 한국 설비투자(산업활동동향) | 5월 -0.1% MoM | **6월치 7/31 발표 — 기준일 익일** | 월별 |
| 한은 추가 인상 | 8월 vs 10월 쟁점 | 금융불안 시 동결/인하 전환 = 당국 인식 변화 신호 | 금통위 |
| 연준 반대표 구성 | 매파 3표 | 비둘기 반대 출현 = 금융안정 우려 반영 | FOMC |
| Brent | 약 $88 | 재급등 = 물가 재점화 → 긴축 재강화 | 일별 |
| 하이퍼스케일러 capex 가이던스 | 상향 중 | **실제 하향 첫 사례** = 5-4 ①번 전제 붕괴 | 분기 실적 |

> **주의**: 위 임계값 중 HY OAS 400bp, PMI 50 등은 **일반적으로 통용되는 기준선**이며 본 조사에서 개별 검증한 최적화 임계값이 아닙니다. quant-validator의 검증을 받을 것을 권고합니다.

---

## 7. 미확인 가정 및 데이터 공백

### 7-1. 태그별 집계

| 태그 | 건수(개략) | 비고 |
|---|---|---|
| `[RAW]` | **0** | 사용자 제공 raw 데이터 없음 |
| `[WEB-교차확인]` | 주요 항목 12건 | 한은 인상, FOMC, 한/미 CPI, 원화, 수출, 고용, 미 PMI, HY OAS, Meta Compute, Alphabet capex 등 |
| `[WEB]` | 다수 | 1차 기관 소스(연준·기재부·산업부·통계당국·S&P Global) 중심 |
| `[WEB-미확인]` | 8건 | 아래 7-2 |
| `[DERIVED]` | 2건 | 무역흑자 계산, HY OAS 역사 비교 — 계산식 본문 병기 |

### 7-2. `[WEB-미확인]` 항목 (단일 소스 또는 검증 실패)

1. **연준 대차대조표 $6.75조 (7/22)** — 단일 소스(Convex), FRED 원계열 미확인. *영향도: 사소*
2. **QT 2025년 12월 종료** — Brookings 단일, 다만 FOMC "ample reserves" 문구와 정합. *영향도: 사소*
3. **미 데이터센터 건설 착공액 시계열** ($14.9B→$26.9B→$77.7B→$49.5B) — 2차 집계 매체, Census 원계열 미확인. *영향도: 중간(비관B 시나리오의 "과잉투자" 규모 논거)*
4. **AI capex의 미 GDP 성장 기여 +2.5%p(2026)/+3%p(2027), 1분기 성장의 75%** — 저신뢰 2차 매체, 방법론 미공개. *영향도: **큼** → NEEDS_CLARIFICATION 3번*
5. **외국인 국내 주식투자 약 413억 달러 감소** — KB 단일 소스, 기준 시점 불명. *영향도: 중간(market-microstructure-analyst 데이터와 교차 필요)*
6. **WTI 약 $83.80 (-6%)** — 단일 소스. *영향도: 사소*
7. **HY OAS의 역사적 위기 수준 비교(2008년 약 2,000bp, 2020년 약 1,100bp, 중위 450~500bp)** — 본 조사에서 개별 URL 재확인 안 함. *영향도: 중간(6-3 임계값 근거)*
8. **코스피 일간 -732.09pt(-10.84%) 역대 최대 낙폭** — 채권 기사 내 인용. *영향도: 검증을 market-microstructure-analyst / historical-market-analyst로 이관*

### 7-3. 데이터 공백 (임의 보간 없이 명시)

1. **한국 CDS 프리미엄 현재 수준 — 미확보**. 검색 상위 노출 자료("19bp, 2008년 이후 최저")는 WebFetch 확인 결과 **2021년 5월 기재부 발표**로 판명되어 폐기. 한국 국가신용위험의 직접 지표이므로 공백이 중요. → NEEDS_CLARIFICATION 2번
2. **한국 회사채 신용스프레드(AA-, BBB- 등급별) 7월 수준 — 미확보**. 국내 신용경색 여부의 직접 증거.
3. **급락 기간 달러 자금시장 지표 — 미확보**: SRF 일별 사용액(7/2~7/29), EFFR-IORB 스프레드, FRA-OIS, 한미 통화스왑 베이시스. 달러 조달 스트레스 판별의 결정적 재료.
4. **2026년 6월 산업활동동향(설비투자·광공업생산) — 2026-07-31 발표 예정**. 분석 기준일 익일이므로 구조적으로 확인 불가. 2차 사이트가 제시한 "설비투자 -9.7% YoY" 값은 5월 데이터 오전재 가능성으로 **폐기**.
5. **2026년 7월 한국 제조업 PMI — 8월 초 발표 예정**. 급락이 실물 심리에 미친 영향을 볼 첫 지표. 미발표.
6. **2026년 7월 한/미 CPI — 8월 발표 예정**. 유가 하락 반영분 미확인. 한은 "7월 오름폭 둔화" 전망만 존재.
7. **capex 가이던스 → 설비투자·고용 통계 반영 시차의 정량 근거 — 미확보**. → NEEDS_CLARIFICATION 4번
8. **한국 가계부채 최근 잔액·증가율 — 미확보**. 한은이 인상 근거로 "가계부채·수도권 주택가격"을 명시했으나 수치를 확보하지 못함. (확보된 것은 기재부 7월호 "전국 주택가격 +0.21%")
9. **Microsoft·Amazon·Meta의 Q2 2026 실적 발표 결과 — 기준일 시점 미공개/부분**. CNBC 7/28 기사는 "이번 주 발표 예정"으로 서술. Alphabet(7/22)만 확정.

### 7-4. 분석 기준점 관련 상충 (protocol 3번 상황)

`[WEB-미확인]` 코스피 고점·낙폭에 대해 브리핑과 검색 결과가 다릅니다.
- **브리핑(PM 제공)**: 고점 8,476, 7월 약 -29%
- **검색 결과**: 6/29~7/29 구간 최고 **8,667.73** → 최저 **5,262.77**, **-32.67%** ([Investing.com 계열 요약](https://kr.investing.com/indices/kospi-historical-data))
- 종가 기준 vs 장중 기준, 기간 정의 차이일 가능성이 크나 확인하지 못했습니다.
- **본 보고서는 지수 수치에 의존한 계산을 하지 않았으므로 결론에 영향 없음.** 다만 팀 전체가 동일 기준점을 써야 하므로 **research-team-lead에게 기준점 통일을 요청**합니다. → NEEDS_CLARIFICATION 5번

### 7-5. 기타 상충 수치 병기 목록 (본문 내 처리 완료)

| 항목 | 값 A | 값 B | 처리 |
|---|---|---|---|
| 한국 6월 수출 | 1,022.5억달러(+70.9%) — 5개 소스 | 620억달러(반도체 +188.4%) — 헤럴드경제 | 병기, A를 본문 기준 |
| Alphabet 주가 반응 | -7% (CNBC) | -5% (Value Add VC) | 병기 |
| 하이퍼스케일러 총 capex | $690B / $700B+ / $725B / $750B / $440B+ | — | 전부 병기 + 집계범위 명시 |
| Meta 2026 capex | $125~145B | $115~135B | 병기 |
| Alphabet 2026 capex | $195~205B (7/22 상향) | $175~185B (상향 전) | 병기, 시점 구분 |
| 미 물가·에너지 서술 | FOMC "에너지 공급충격으로 물가 높음" | 6월 CPI 에너지 -5.7% MoM | 병기, YoY/MoM 시점차 설명 부기 |
| 한국 6월 취업자 | 6.3만명(4개 1차 보도) | 63만명(WebFetch 오독) | 오독 정정, 6.3만명 채택 |

---

## 8. NEEDS_CLARIFICATION (research-team-lead 보고용)

```
NEEDS_CLARIFICATION #1
- 항목: 2026년 하이퍼스케일러 총 capex 집계 기준
- 상황: 소스마다 집계 범위(4사/5사/14대 데이터센터 운영사)와 시점이 달라 $440B~$750B로 편차가 큼. 범위를 명시하지 않고 인용하면 시나리오 간 비교가 불가능해짐.
- 후보값: >$690B, FY26 하이퍼스케일러 (FactSet 2026-07-23) vs >$700B, 4사 (Value Add VC) vs $725B, 4사 (valueaddvc) vs ~$750B, 상위 5사 및 14대 DC 운영사 (CNBC 2026-07-28) vs >$440B, 상위 5사 확정 커밋 (Epoch AI)
- 시나리오 영향도 판단: 큼. 비관B(구조적 버블 붕괴)는 capex 절대 규모를 "과잉투자" 논거로 쓰고, 낙관은 동일 수치를 "수요 견조" 논거로 씀. 두 팀이 서로 다른 집계 범위를 쓰면 대칭 비교가 무너짐. 팀 차원의 단일 기준(권고: FactSet 5개사 기준, FY26 >$690B) 지정 필요.
```

```
NEEDS_CLARIFICATION #2
- 항목: 한국 CDS 프리미엄 및 회사채 신용스프레드 현재 수준
- 상황: "거시 유동성 위기 vs 반도체 국지 이벤트"라는 핵심 판단축의 직접 증거인데 확보 실패. 검색 상위에 노출된 "한국 CDS 19bp, 2008년 이후 최저" 자료는 WebFetch 확인 결과 2021년 5월 기재부 발표로 판명되어 폐기함(2026년 데이터 아님). 대체 소스(INDEXerGO, 한국경제 데이터센터)는 실시간 조회형으로 수치 추출 실패.
- 후보값: 없음 (데이터 공백). 폐기값: 19bp (기재부, 2021-05-06)
- 시나리오 영향도 판단: 큼. 한국 CDS와 회사채 스프레드가 안정적이면 "국지 이벤트" 가설이 강화되고, 확대되었다면 비관A/B의 거시 전이 논거가 강화됨. 현재 본 보고서는 환율·국고채·미 HY OAS 세 지표로 우회 논증했으나 한국 신용위험 직접 지표가 비어 있음. PM 차원의 raw 데이터 확보 또는 다른 에이전트의 접근 가능 소스 확인 요청.
```

```
NEEDS_CLARIFICATION #3
- 항목: AI capex의 미국 GDP 성장 기여도
- 상황: "2026년 성장률에 +2.5%p, 2027년 +3%p 이상 기여", "2026년 1분기 미국 성장의 75%가 AI capex" 주장이 저신뢰 2차 매체에만 존재하고 방법론 미공개. GDP 성장률 자체를 초과할 수 있는 수치여서 산정 방식(총투자액/GDP vs 증분 기여) 판별 불가. 반면 Epoch AI/JPMAM의 "GDP 대비 비중 0.8%/1.5%"는 상대적으로 신뢰 가능.
- 후보값: +2.5%p(2026)·+3%p(2027)·1분기 성장의 75% (TECHi, Beta Finch) vs GDP 비중 0.8%(AI DC 관련)·1.5%(컴퓨팅 인프라 전체), 2015~22 평균 0.7% (Epoch AI, J.P. Morgan AM)
- 시나리오 영향도 판단: 큼. "AI capex가 미 성장의 75%"는 비관B의 핵심 논거("AI 꺾이면 미국 경제도 꺾인다")로 직결됨. 검증되지 않은 수치가 시나리오 골격에 들어가면 IC 단계에서 전체가 무너질 수 있음. 권고: 비중 지표(0.8%/1.5%)만 사용하고 성장기여도 주장은 시나리오 근거에서 배제. quant-validator 사전 검증 요청.
```

```
NEEDS_CLARIFICATION #4
- 항목: capex 가이던스 변경 → 실제 설비투자·고용 통계 반영 시차
- 상황: 에이전트 정의상 배정된 항목이나 정량 근거 확보 실패. 데이터센터 착공→준공 리드타임, 반도체 장비 발주→매출 인식 시차, capex 가이던스 변경→건설지출 통계 반영 시차에 대한 신뢰 가능한 수치를 찾지 못함. 임의 추정을 금지하는 프로토콜에 따라 공백으로 남김.
- 후보값: 없음 (데이터 공백)
- 시나리오 영향도 판단: 중간~큼. "capex가 꺾이면 언제 실물·실적에 나타나는가"는 세 시나리오의 시간축을 결정함. 낙관은 시차가 길다고, 비관은 짧다고 가정할 유인이 있어 비대칭 위험이 큼. 권고: semiconductor-analyst의 장비 수주/BB Ratio 리드타임 데이터와 결합해 팀 차원 공통 가정으로 설정하고, "미확인 가정" 문서에 명시.
```

```
NEEDS_CLARIFICATION #5
- 항목: 코스피 고점·낙폭 분석 기준점 (protocol 3번 상황: 기준점 미합의)
- 상황: PM 브리핑은 고점 8,476, 7월 약 -29%. 검색 결과는 6/29~7/29 최고 8,667.73 → 최저 5,262.77, -32.67%. 종가/장중 기준 차이 또는 기간 정의 차이로 보이나 확인 못 함. 본 거시 보고서는 지수 수치 계산에 의존하지 않으므로 자체 결론에는 영향 없음.
- 후보값: 고점 8,476 / -29% (PM 브리핑) vs 고점 8,667.73, 저점 5,262.77 / -32.67% (Investing.com 계열)
- 시나리오 영향도 판단: 본 에이전트 산출물에는 사소. 그러나 팀 전체로는 큼 — historical-market-analyst의 percentile 산출, valuation-quant-analyst의 P/E 분해가 모두 이 기준점에 종속됨. 팀장 차원의 기준점 통일(종가 기준/장중 기준, 고점일, 측정기간) 선포 요청.
```

---

## 부록: 주요 출처 목록

**1차 기관 소스**
- [Federal Reserve, FOMC 성명 2026-07-29](https://www.federalreserve.gov/newsevents/pressreleases/monetary20260729a.htm)
- [한국은행 금통위 7월 통화정책방향 전문](https://v.daum.net/v/20260716110353864)
- [기획재정부 2026년 7월 최근경제동향 (KDI 경제정보센터)](https://eiec.kdi.re.kr/policy/materialView.do?num=284260)
- [기획재정부 26년 6월 최근경제동향 (정책브리핑)](https://www.korea.kr/news/policyNewsView.do?newsId=156766301)
- [2026년 5월 산업활동동향 (정책브리핑)](https://www.korea.kr/news/policyNewsView.do?newsId=156768746)
- [2026년 6월 및 상반기 수출입 동향 (KDI)](https://eiec.kdi.re.kr/policy/materialView.do?num=283602) / [정책브리핑](https://www.korea.kr/briefing/policyBriefingView.do?newsId=156769112)
- [S&P Global J.P.Morgan Global Manufacturing PMI](https://www.pmi.spglobal.com/Public/Home/PressRelease/99c4c5f2e4184a7697ccaccc514a9ca6)
- [S&P Global 한국 제조업 PMI](https://www.pmi.spglobal.com/Public/Home/PressRelease/70bb58bb8f804354841961b33505c3f5)
- [US CPI 2026년 6월 상세 (usinflationcalculator)](https://www.usinflationcalculator.com/inflation/us-cpi-june-2026/100072543/)

**금리·크레딧**
- [FactSet Insight, Hyperscalers Tap External Financing (2026-07-23)](https://insight.factset.com/hyperscalers-tap-external-financing-as-ai-capex-outruns-cash-flow)
- [Reuters/Yahoo, Hyperscaler debt binge pushes yields up](https://finance.yahoo.com/markets/stocks/articles/hyperscaler-debt-binge-pushes-yields-134825104.html)
- [Sage Advisory, Hyperscaler Debt Deluge](https://www.sageadvisory.com/article/hyperscaler-debt-deluge-the-new-driver-of-ig-spread-pressure)
- [ICE BofA US HY OAS (TradingEconomics)](https://tradingeconomics.com/united-states/bofa-merrill-lynch-us-high-yield-option-adjusted-spread-fed-data.html) / [govspending](https://govspending.org/series/BAMLH0A0HYM2/) / [Convex](https://convextrade.com/metrics/bamlh0a0hym2)
- [이투데이 채권마감](https://www.etoday.co.kr/news/view/2607957) / [KB 2026-07-02 채권마감](https://kbthink.com/news-list/view.html?newsId=20260702164048903) / [이투데이 2026-07-28](https://news.nate.com/view/20260728n28436)

**물가·환율·유가**
- [경향신문 6월 CPI 2026-07-02](https://www.khan.co.kr/article/202607020811001) / [YTN](https://www.ytn.co.kr/_cs/_ln_0102_202607020801031915_005.html) / [뉴스핌](https://www.newspim.com/news/view/20260702000083) / [전자신문](https://www.etnews.com/20260702000060)
- [CNBC US CPI 2026-07-14](https://www.cnbc.com/2026/07/14/consumer-price-index-inflation-report-june-2026.html)
- [파이낸셜뉴스 환율 2026-07-29](https://www.fnnews.com/news/202607291534513058) / [머니투데이 2026-07-28](https://www.mt.co.kr/economy/2026/07/28/2026072815364551633) / [TradingEconomics KRW](https://ko.tradingeconomics.com/south-korea/currency)
- [CNBC 유가 2026-07-27](https://www.cnbc.com/2026/07/27/oil-price-wti-brent-slide-as-iran-reportedly-may-halt-attacks.html) / [Al Jazeera 2026-07-08](https://www.aljazeera.com/news/2026/7/8/oil-prices-surge-as-us-strikes-iran-reversing-fall-to-pre-war-levels)

**Capex·트리거**
- [CNBC Meta cloud push 2026-07-01](https://www.cnbc.com/2026/07/01/meta-stock-cloud-ai-compute.html)
- [SemiAnalysis via Investing.com 2026-07-06](https://www.investing.com/news/stock-market-news/meta-capex-to-surge-in-2027-neocloud-fears-erroneous--semianalysis-4777202)
- [CNBC Alphabet Q2 2026-07-22](https://www.cnbc.com/2026/07/22/google-earnings-q2-goog-live-updates.html)
- [CNBC hyperscaler capex scrutiny 2026-07-28](https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html)
- [Epoch AI, Data center share of US GDP](https://epoch.ai/data-insights/ai-datacenter-share-gdp) / [J.P. Morgan AM](https://am.jpmorgan.com/us/en/asset-management/adv/insights/market-insights/market-updates/on-the-minds-of-investors/is-ai-already-driving-us-growth/)

**PMI·고용**
- [investinglive US flash PMI 2026-07-24](https://investinglive.com/news/the-july-flash-s-p-global-manufacturing-53-8-vs-54-3-estimate/) / [FXStreet](https://www.fxstreet.com/news/us-sp-global-pmi-expected-to-show-steady-business-growth-in-july-202607241000) / [NAM](https://nam.org/sp-global-flash-u-s-manufacturing-pmi-drops-to-four-month-low/)
- [아시아투데이 6월 고용 2026-07-15](https://www.asiatoday.co.kr/kn/view.php?key=20260715010005538) / [전자신문](https://www.etnews.com/20260715000178) / [뉴스핌](https://www.newspim.com/news/view/20260715000066)

---

*본 보고서는 사실관계 조사와 1차 해석까지만 담고 있으며, 투자 판단·저점 시점·매수 권고를 포함하지 않습니다.*
