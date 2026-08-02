# 06. 데이터 공백 4개 항목 추가 조사 결과 (Gap Research Follow-up)

- 조사 기준일: 2026-08-02 (Asia/Seoul)
- 조사 범위: `미확인_가정.md` §1의 미해소 4개 항목에 대한 **공개 원문 재조사**
- 결론 배제: 이 문서는 자료 조사 기록이다. 저점 판단·목표지수·매매 결론을 제시하지 않는다.
- 등급 체계: `data-sourcing-protocol` A~D 및 `[RAW]/[OFFICIAL]/[REPORT]/[WEB]/[DERIVED]/[ASSUMPTION]` 태그
- 기존 레지스트리(`01_public-research-evidence-registry.md`)와 source family 중복 여부를 항목마다 명시했다.

---

## 항목 1. 독립된 KOSPI 12MF EPS 장기 시계열

**판정: 부분 찾음 — 계열의 실재는 확인, 과거 하강 국면 수치는 못 찾음**

### 1-1. 찾음 — FnGuide 계열의 장기 KOSPI 12MF EPS 시계열 존재 확인

- `report_publisher`: 미래에셋증권 (유명간)
- `report_title`: 「2026 하반기 전망 — 주식전략」
- `report_date`: 2026-05-22
- `url`: https://securities.miraeasset.com/bbs/download/2144785.pdf?attachmentId=2144785
- `page`: PDF p.6, 우측 차트 「코스피와 12MF EPS」
- `metric_definition`: 코스피 지수(좌축)와 코스피 12MF EPS(우축), x축 **2003~2025**
- `original_data_provider`: **FnGuide** (차트 하단 “자료: FnGuide, 미래에셋증권 리서치센터”)
- `source_family_id`: `FNGUIDE_KOSPI_12MF_EPS` **(신규 · Refinitiv/LSEG와 독립)**
- `evidence_grade`: `[REPORT-B]` — **계열 존재만 A급으로 확인, 수치는 미확보**
- `methodology_notes`: 같은 페이지의 「코스피와 12MF PER」 차트도 자료: FnGuide. 차트에 **수치가 인쇄돼 있지 않고**, PDF 텍스트 추출로 우축 눈금 라벨을 복원하지 못했다. 프로토콜의 “차트 복원 시 눈금·오차범위 명시” 요건을 충족할 수 없으므로 **2008/2018-19/2022-23 고점·저점 값을 이 문서에서 산출하지 않는다.**

> **의미**: “FnGuide는 KOSPI 12MF EPS 장기 시계열을 보유·공표한다”가 공개 원문으로 확인됐다. 즉 두 번째 독립 계열은 **존재하나 공개 원문에 수치가 인쇄된 형태로는 유통되지 않는다.** 이는 “계열 부재”가 아니라 **“수치 공개본 부재”**로 공백의 성격이 바뀐 것이다.

### 1-2. 찾음 — FnGuide 계열의 12MF EPS 레벨 (단일 시점, 최근 국면)

- `report_publisher`: 신한투자증권 (노동길)
- `report_title`: 「2분기 주식시장 전망 Yellow Flag — V. 한국 주식시장 전략: 네 가지 축 포트폴리오」
- `report_date`: 2026-04-01
- `url`: https://open.shinhansec.com/cms/contents/bigdata/__media/260401_kor_stgy.pdf
- `page`: PDF p.70(문서 페이지 표기 70 I), 본문 및 「2분기 코스피 12MF EPS 시나리오별 경로」
- 인용 원문 수치: **“3월말 기준 12개월 선행 EPS는 664.9p, 20거래일 스무딩 값은 643.4p다. 올해 말 12개월 선행 EPS의 종착점이 되는 EPS는 736.0p다.”**
- `original_data_provider`: 에프앤가이드(FnGuide) — 해당 차트 “자료: 에프앤가이드, 신한투자증권”
- `evidence_grade`: `[REPORT-B]`
- `methodology_notes`: **정의 혼재 경고 —** 같은 보고서 p.58의 「코스피 12MF EPS 및 PER 추이」 차트는 “자료: LSEG”로 표기돼 있고, p.57·p.70의 밸류에이션 매트릭스·시나리오 차트는 “자료: 에프앤가이드”로 표기돼 있다. 한 보고서 안에서 두 제공자를 혼용하므로 664.9p가 FnGuide 산출인지 LSEG 산출인지 **단정할 수 없어 A가 아닌 B**로 등급을 낮췄다.

### 1-3. 찾음 — 과거 EPS 하강폭의 두 번째 계열 추정치 (기존 레지스트리 gap #9 부분 해소)

- 원출처: **Goldman Sachs** 한국 주식 전략 코멘트 (2026년 7월 초, 원문 PDF 미확보)
- 재인용 URL: https://www.investing.com/news/stock-market-news/koreas-kospi-pe-valuation-falls-to-lowest-since-global-financial-crisis-4775362 (2026-07-04)
- 보조 재인용: https://news.futunn.com/en/post/76234736/here-s-wall-street-s-latest-view-on-korean-equities
- 인용 수치:
  - NTM(향후 12개월) 컨센서스 EPS **약 1,150**
  - **“2008년 이후 6번의 저점 국면 EPS 하락률 중앙값 = 33%”** → 스트레스 EPS 771
  - **“과거 EPS 저점 시점의 선행 PER 중앙값 = 11.4배”** → 함의 코스피 약 8,750(다른 재인용은 8,778)
  - 최악 가정: **금융위기 수준 EPS -41%**
  - 12MF EPS 최근 **+4.8% 상향**
- `evidence_grade`: `[REPORT-C]` — 원문 보고서·표·페이지·원 데이터 제공자 **모두 미확보**
- `source_family_id`: `GS_KOREA_TROUGH_STUDY` (신규, 잠정)
- `methodology_notes`: 기존 레지스트리 §6-9는 Goldman “6개 저점”을 **C등급으로조차 등록 불가**로 두었다. 이번에 **추적 가능한 재인용과 구체 수치(33%·41%·11.4배·6회)**를 확보해 **C등급 등록 가능** 수준으로 올라왔다. 단 원 데이터 제공자 미표기이므로 Refinitiv 계열과의 중복 제거가 **아직 불가능**하다.

### 1-4. 못 찾음 / 독립성 부정

| 후보 | 결과 | 사유 |
|---|---|---|
| 대신증권 「[AI Insight] KOSPI, 언제까지 하락할 것인가」 (2026-07-30) | **독립 출처 아님** | 12MF EPS 자료 표기가 전부 **LSEG**. LSEG는 Refinitiv를 인수·승계한 동일 계열 → `REFINITIV_KOSPI_12MF_EPS`와 **같은 source family** |
| KB증권 「3월 전략: EPS가 바닥국면에 진입할 때」 (2023-02-28) <br>https://rdata.kbsec.com/pdf_data/20230228171556277K.pdf | **독립 출처 아님** | 12MF EPS 관련 전 도표가 “자료: REFINITIV, KB증권”. Quantiwise 표기는 **모델포트폴리오 표 1건뿐**이며 EPS 시계열이 아님 |
| QuantiWise 직접 공개 시계열 | **못 찾음** | 공개 웹에 지표 시계열 없음. 상용 단말/구독 필요 |

### 1-5. 기존 자료 대비 독립성 판정

- **EPS 하강 분포의 유효 표본은 여전히 `사건 n=3 / 독립 source family n=1`(Refinitiv/LSEG)이다.**
- FnGuide 계열은 **레벨·차트로만 확인**되어 2008/2018/2022 하락률 계산에 투입할 수 없다.
- Goldman 계열(33%/41%)은 **C등급·제공자 미확인**이라 독립 family로 셀 수 없다.
- 따라서 **-31.7%~-37.0%, 9~14개월을 “역사적 임계값”이라 부르는 금지는 해제되지 않는다.**

### 1-6. 시도한 검색

`코스피 12개월 선행 EPS FnGuide 추이 증권사 리포트` / `KOSPI 12개월 선행 EPS 컨센서스 퀀티와이즈 QuantiWise 하향` / `에프앤가이드 코스피 12개월 선행 EPS 2008년 2019년 2023년 저점 하락률 리포트` / `Korea KOSPI earnings revision ratio breadth percentage 2026` / `Goldman Sachs Korea KOSPI July 2026 forward EPS 1150 trough P/E stress scenario`

---

## 항목 2. 2026년 6~7월 같은 날짜의 코스피 지수·12MF EPS·12MF PER

**판정: 찾음 (복수 출처). 단 제공자별로 값이 상충하므로 병기한다.**

### 2-1. 지수·EPS·PER 3개를 동시에 명시한 유일 문서 — 대신증권 JAEMINI

- `report_publisher`: 대신증권 (AI Engineer 조재운 / 경제분석 AI 모델 JAEMINI)
- `report_title`: 「[AI Insight] KOSPI, 언제까지 하락할 것인가 — 45년에 여섯 번째인 국면을 읽는 법」
- `report_date`: 2026-07-30
- `url`: https://money2.daishin.com/PDF/Out/intranet_data/Product/ResearchCenter/Report/2026/07/58360_20260730_ai_insight_kospi_3_260730091042.pdf
- `page`: PDF p.2 표, p.12 본문, p.25 데이터 부록
- 인용 원문 수치:
  - **2026-07-29 종가 5,663.24 / 12MF EPS 1,112.3 / 12MF PER 5.09배** (원문 표기 “5.09배 (7/29 종가 5,663 ÷ 선행 EPS 1,112)”)
  - **2026년 7월 초 지수 8,303 / 12MF EPS 1,041.8** → 7월 중 지수 -31.8%, EPS **+6.8%**
  - 6월 22일 고점 **9,115** (고점 대비 -37.9%)
  - 5년 PE 밴드 하단(p25) 9.2배
- `original_data_provider`: **LSEG** (+ JAEMINI 자체 DB)
- `evidence_grade`: `[REPORT-B]`
- `source_family_id`: `REFINITIV_KOSPI_12MF_EPS` **(기존 계열과 중복 — 독립 출처 아님)**
- `methodology_notes`: **A등급을 주지 않은 이유** — 본문에 정의·날짜·수치·제공자가 모두 있으나, 발행사가 문서 전면에 **“경제 분석 AI 모델 JAEMINI가 작성. 대신증권 리서치센터의 뷰가 아니며, 생성형 AI 특성상 사실관계나 계산에 오류가 있을 수 있다”**고 명시적으로 면책했다. 발행사 자신이 검증을 보증하지 않는 수치이므로 B로 격하한다.

### 2-2. FnGuide 계열의 같은 날짜 지수·PER (EPS는 DERIVED)

| 보고서 | 발행일 | 기준일 | KOSPI | 12MF PER | PBR(TTM) | 5년평균 PER | `[DERIVED]` 12MF EPS |
|---|---|---|---:|---:|---:|---:|---:|
| 미래에셋 「Earnings Revision (6월 2주차)」 | 2026-06-08 | 보고서 기준 | 8,161pt | 7.8배 | 2.31배 | 10.2배 (-1.87σ) | 약 **1,046** |
| 미래에셋 「Earnings Revision (7월 5주차)」 | 2026-07-24 | **7/23(목) 종가** | 7,097pt | 6.1배 | 2.01배 | 10.0배 (-2.99σ) | 약 **1,163** |

- `url`: 6월 https://securities.miraeasset.com/bbs/download/2145066.pdf?attachmentId=2145066 (p.9 「한국 주식 시장의 밸류에이션」, 그림 39)
- `url`: 7월 https://securities.miraeasset.com/bbs/download/2146091.pdf?attachmentId=2146091 (p.9 「한국 주식 시장의 밸류에이션」, 그림 39 및 p.8 요약표)
- `original_data_provider`: **FnGuide**
- `evidence_grade`: 지수·PER·PBR **`[REPORT-A]`** / EPS **`[DERIVED from REPORT-A]`**
- `source_family_id`: `FNGUIDE_KOSPI_VAL` **(기존 계열과 중복 — 새 날짜를 추가할 뿐 새 독립 family 아님)**
- `methodology_notes`: **EPS는 원문에 인쇄돼 있지 않다.** `지수 ÷ 12MF PER`로 역산한 값이며, PER이 소수 1자리로 반올림돼 있어 정밀도 한계가 있다. 7/23의 경우 PER 6.05~6.15 구간을 적용하면 EPS는 **약 1,154~1,173** 범위다. **소수점 정밀도를 만들지 않는다.**

### 2-3. 하나증권 계열 (언론 재인용)

- 매체·일자: 파이낸셜뉴스 2026-08-02, https://www.fnnews.com/news/202608021337527083
- 인용 수치: **2026-07-30 종가 기준 코스피 12MF PER 4.7배**, “글로벌 금융위기 당시 저점 6.3배를 크게 밑돌았다”
- 부수 수치: 코스피 선행 12개월 **영업이익** 전망치 4월 초 695조원 → 최근 **1,164조원(+67.5%)**; 2026년 영업이익 전망치 663조원 → 967조원(+45.9%); 7/31 종가 **6,595.45(+17.91%, +1001.89p)**, 7월 한 달 -22.19%
- 발언자: 이재만 하나증권 글로벌투자분석실장
- `evidence_grade`: `[REPORT-C]` — 하나증권 원문 보고서 미확보
- `source_family_id`: `HANA_KOSPI_VAL_VIA_MEDIA` (신규, C)

### 2-4. 상충값 병기 (평균·선택 금지)

같은 2주 안의 코스피 12MF PER이 제공자·정의별로 다르게 보고된다.

| 기준일 | 12MF PER | 출처 / 제공자 | 등급 |
|---|---:|---|---|
| 2026-07-23 | **6.1배** | 미래에셋 / FnGuide (KOSPI) | A |
| 2026-07-24(주간) | **5.5배** | 미래에셋 / Refinitiv·MSCI (**MSCI Korea**, 정의 다름) | A |
| 2026-07-29 | **5.09배** | 대신 JAEMINI / LSEG (KOSPI) | B |
| 2026-07-30 | **4.7배** | 하나증권 / 언론 재인용 (KOSPI) | C |
| 2026-07-08 | **6.25배** | 키움증권 / 언론 재인용 | C |

- **처분**: 지수가 이 기간 급락 중이었으므로 날짜 차이만으로도 값이 크게 달라진다. 여기에 KOSPI/MSCI Korea, 제공자별 컨센서스 모집단 차이가 겹친다. **평균내지 않고 전부 병기한다.**
- **`NEEDS_CLARIFICATION` 후보**: 현재 PER 수준을 “금융위기 저점 대비 위치”로 표현할지 여부는 어느 계열을 쓰느냐에 따라 결론이 달라진다. research-team-lead 판단 필요.

### 2-5. 기존 자료 대비 독립성

- 항목 2는 **해소**로 볼 수 있다. 다만 `FNGUIDE_KOSPI_VAL`은 기존 등록 family이고, `REFINITIV/LSEG`도 기존 family다. **새 날짜는 얻었으나 새 독립 계열은 얻지 못했다.**
- **원문에 EPS 숫자가 인쇄된 유일한 2026년 문서는 대신 JAEMINI(LSEG 계열, B등급)뿐이다.**

---

## 항목 3. 이익 전망 개선/악화 기업 수의 변화 (revision breadth)

**판정: 요청한 정의로는 못 찾음. 정의가 다른 프록시 3종만 확보.**

### 3-1. 못 찾음 — 확인한 사실

미래에셋증권 「Earnings Revision」 주간 시리즈는 **breadth 지표를 싣지 않는다.** 2026-07-24판(7월 5주차) 전 도표(그림 1~75)를 확인한 결과:

- 표 1 「한국 이익 전망치 상향 종목 Top 20」, 표 2 「하향 종목 Bottom 20」 → **개별 종목 리스트만 있고 종목 수·비율 집계가 없다.**
- 주석은 “시가총액이 5,000억원 이상이면서 컨센서스가 4개 이상 존재하는 기업 대상”으로 **모집단 정의만** 제시한다.
- 기존 레지스트리의 `BREADTH-2013-01`(미래에셋 2013, Bloomberg, 상향/하향 종목 수 비율 28%)에 대응하는 **2026년판 동일 지표를 공개 원문에서 찾지 못했다.**

### 3-2. 프록시 A — 목표주가 상향/하향 **리포트 건수** (기업 수 아님)

- 매체·일자: 파이낸셜뉴스 2026-07-19, https://www.fnnews.com/news/202607191816577598
- 집계 주체: **에프앤가이드(FnGuide)** — “19일 금융정보업체 에프앤가이드에 따르면”
- 인용 수치:

| 기간 | 상향 리포트 | 하향 리포트 | 비고 |
|---|---:|---:|---|
| 2026-01 | 940건 | 228건 | 상향이 4배 초과 |
| 2026-02 | 1,122건 | 116건 | 낙관 우세 |
| 2026-07-01~16 | 249건 | **323건** | **2026년 최초로 하향이 상향 추월(+74건)** |
| 2026-07-10~16 | 91건 | 189건 | 하향이 2배 초과 |

- 종목별: 하향 최다 한화오션 10건, 현대차·카카오 각 9건, 하이브 8건 / 상향 최다 KB금융 11건, 신한지주 10건
- SK하이닉스 목표가 **상향** 리포트: 4월 34건 → 5월 22건 → 6월 18건 / 삼성전자: 4월 26건 → 5월 31건 → 6월 19건
- `evidence_grade`: `[REPORT-C]`
- `source_family_id`: `FNGUIDE_TARGETPRICE_REPORT_COUNT` (신규)
- **정의 경고**: 이것은 **목표주가 리포트 건수**이지 **이익 추정치가 상향/하향된 기업 수**가 아니다. 한 기업에 여러 건이 중복 계상되고, 목표주가는 이익 추정치와 밸류에이션 배수 양쪽에 반응한다. **breadth 지표로 대체 사용 금지.** 방향 참고용.

### 3-3. 프록시 B — 이익 추정치 **변화율** (breadth 아님)

- 대신 JAEMINI (2026-07-30), 자료: LSEG
- 인용: **“3개월 이익 추정치 상향률은 7월 초 55.4%에서 지금 32.6%로 내려왔다”**, 차트 제목 「코스피 3개월 이익추정치 상향률 — 0선이 판별선」
- **정의 경고**: “0선이 판별선”이라는 표현은 이 지표가 **추정치의 3개월 변화율(%)**임을 뜻한다. 기업 수 비율이 아니다. `evidence_grade`: `[REPORT-B]`, family `REFINITIV_KOSPI_12MF_EPS`(중복)

### 3-4. 프록시 C — 국가 단위 12MF EPS 변화율

- 미래에셋 2026-07-24판 p.28 요약: **“전세계 12MF EPS는 지난달 대비 +1.7% 상향. 국가별로 한국(+9.7%), 대만(+5.8%) 상향. 호주(-2.4%), 인도(-1.1%) 하향.”**
- 자료: **Factset, Refinitiv, MSCI** → `FACTSET_MSCI_EPS`(기존 family, 중복)
- 국내 기업 합산 영업이익 컨센서스 1주 변화(2026-07-24): 2026년 **-0.1%(-0.5조원)**, 2Q26 **+0.0%**; 2026년 영업이익 증가율 +230%YoY (반도체 +591%, 반도체 제외 +39%). 자료 FnGuide, `[REPORT-A]`
- **정의 경고**: 국가·합산 레벨 변화율이며 기업 수 분포가 아니다.

### 3-5. 기존 자료 대비 독립성

- **요청한 지표(상향/하향 기업 수·비율)는 미해소.** 기존 레지스트리 §6-7의 공백(“상향/하향 종목 수 비율의 2008·2018·2022 동일 정의 자료 필요”)은 **그대로 남는다.**
- 프록시 3종은 모두 정의가 달라 `BREADTH-2013-01`과 **시계열로 이어붙일 수 없다.**
- **판정 보류 유지**: “이익 감소가 일부 기업인지 시장 전반인지”는 여전히 **산출 불가**.

### 3-6. 시도한 검색

`코스피 이익수정비율 상향 종목 수 하향 종목 수 비율 2026년 7월` / `미래에셋증권 Earnings Revision 2026년 7월 코스피 12개월 선행 PER 이익수정비율` / `"이익수정비율" 코스피 상향 종목 비중 증권사 리포트 2026` / `코스피 이익 전망 상향 기업 비중 하향 기업 비중 컨센서스 breadth 2026년 7월 급락` / `"상향" "하향" 종목 수 코스피 실적 전망 순상향 비율 이익모멘텀 지표` / `Korea KOSPI earnings revision ratio breadth percentage of companies upgraded downgraded 2026`

---

## 항목 4. 동일 제품·납기·계약조건의 D램 고정거래가격

**판정: 찾음 — 동일 제품·월별 고정거래가 계열 확보**

### 4-1. TrendForce / DRAMeXchange 월별 고정거래가격

- 매체·일자: 이포커스 2026-07-02, https://www.e-focus.co.kr/news/articleView.html?idxno=3002499
- 원 데이터 제공자: **TrendForce 산하 DRAMeXchange** (기사에 명시)
- `metric_definition`: 고정거래가격 = 메모리 제조사와 대형 고객 간 월·분기 단위 대량 계약가

| 제품 | 4월 | 5월 | 6월 | 변화 |
|---|---:|---:|---:|---|
| **DDR4 8Gb** | $16 | $20 | **$21** | 5월 +25%, 6월 +5% / 4~6월 누적 +31.3% · 집계 시작(2016-06) 이후 최고 |
| DDR4 16Gb | — | $40.00 | — | 5월 +19.4% MoM |
| DDR5 8GB 노트북 모듈 | — | $112.00 | — | 5월 +2.75% MoM |
| **NAND 128Gb MLC** | — | — | **$28.82** | 6월 +8.72% MoM |
| (참고) DDR4 8Gb **현물가** | — | — | 7/1 $36.10 | 6월 고정가 대비 **+71.9%** |

- `evidence_grade`: `[REPORT-C]` (원 TrendForce 리포트 미확보, 언론 재인용)
- `source_family_id`: `TRENDFORCE_DRAMEXCHANGE_CONTRACT` (신규)

### 4-2. 보조 — ZDNet Korea (TrendForce 인용)

- URL: https://zdnet.co.kr/view/?no=20260529170256 (2026-05-30)
- **DDR5 16GB 모듈 5월 $205 (+45~50% QoQ)**, DDR4 8GB 모듈 $119 (+35~40% QoQ), NAND 128Gb $26.5 (+9.7% MoM, 17개월 연속 상승)
- 칩 단위 5월 MoM: DDR5 16Gb +7.1%, DDR4 16Gb +19.4%, DDR4 8Gb +25.0%
- `evidence_grade`: `[REPORT-C]` / family `TRENDFORCE_DRAMEXCHANGE_CONTRACT` (중복)

### 4-3. 보조 — 산업통상자원부 보도자료 (대신 JAEMINI 재수록)

- 원출처: 산업통상자원부 보도자료 2026-07-01 (대신 JAEMINI p.20·p.25에 재수록)
- 인용: **DDR5 16Gb 3월 $31 → 6월 $40 (+29%)**, **NAND 128Gb $17.7 → $28.8 (+63%)**
- `evidence_grade`: `[REPORT-B]` (공식 보도자료의 증권사 재수록)
- `source_family_id`: `MOTIE_MEMORY_PRICE`
- **중복 판정 주의**: 산업부 보도자료의 메모리 가격은 관례상 DRAMeXchange 집계를 재공표한다. NAND 128Gb 6월 값이 **$28.8(산업부) vs $28.82(DRAMeXchange)**로 사실상 일치하는 점이 이를 뒷받침한다. → **독립 계열로 세지 말고 `TRENDFORCE_DRAMEXCHANGE_CONTRACT`와 동일 family로 취급할 것을 권고한다.**

### 4-4. 전망치 (관측값 아님 — 격리)

- TrendForce 보도자료 2026-07-03, https://www.trendforce.com/presscenter/news/20260703-13134.html
- **3Q26 conventional DRAM 계약가 +13~18% QoQ, NAND +10~15% QoQ (전망)**
- ZDNet 2026-05-30 시점 3Q26 PC용 D램 전망은 +8~13%(종전 +3~8%에서 상향)
- `evidence_grade`: `[REPORT-D][ASSUMPTION]` — **발행사 전망이며 관측된 계약가가 아니다.**

### 4-5. 기존 자료 대비 독립성

- 기존 레지스트리에 DRAM 가격 계열은 **없었다.** 항목 4는 **신규 확보**이며 기존 어떤 family와도 중복되지 않는다.
- **동일 제품(DDR4 8Gb) 월별 연속 계열**을 4~6월 3개 시점 확보해 `미확인_가정.md` §1-4의 “가격 방향만 조건부 확인” 상태를 **수치 기반으로 개선**했다.
- **잔존 한계**: (1) 납기·계약기간·고객군 구분이 공개되지 않아 “동일 계약조건”은 여전히 미확인. (2) **HBM 계약가는 공개 수치를 찾지 못했다.** (3) 7월 고정가는 8월 초 발표 예정으로 아직 부재 — 대신 JAEMINI가 “D램 고정가 하락 전환”을 1순위 폐기 조건으로 지목한 만큼 **7월 값이 핵심 미확보 데이터**다.

---

## 5. 이번 조사에서 새로 격리한 가정 (Assumption quarantine 추가분)

| 항목 | 출처 | 격리 사유 | 등급 |
|---|---|---|---|
| EPS **-33%** 스트레스 / **-41%** 최악 | Goldman Sachs (언론 재인용) | 발행사가 선택한 스트레스 가정. 2026년 관측 하향률 아님 | `[REPORT-D][ASSUMPTION]` |
| 과거 EPS 저점 시 선행 PER **11.4배** 중앙값 | Goldman Sachs (언론 재인용) | 원표·모집단·제공자 미확인. 하나증권의 “금융위기 저점 6.3배”와 **정면 상충** | `[REPORT-C]` 관찰 · 임계값 사용 금지 |
| 1차 회복 PER 6.3배 → **코스피 7,400p** / 2차 7.4배 → **8,700p** | 하나증권 이재만 (fnnews 2026-08-02) | 목표지수 산출값 | `[REPORT-D][ASSUMPTION]` |
| 신용융자 **30조 초반** = 청산압력 완화 임계 | 대신 JAEMINI | 원문이 **“과거 사례로 검증된 임계가 아니라 이 글의 작업가설”**이라고 자인 | `[REPORT-D][ASSUMPTION]` |
| 3Q26 DRAM +13~18% / NAND +10~15% | TrendForce | 전망치 | `[REPORT-D][ASSUMPTION]` |
| “45년에 6번, 저점 후 3개월 중앙값 +30.3%” | 대신 JAEMINI | 원문이 **독립 국면 4개**이며 “저점을 사후에 알고 계산”이라고 자인. 최소 3사건·2독립계열 요건 중 **계열 1개(LSEG)** | `[DERIVED—QUARANTINED]` |

**상충 기록 (평균·선택 금지)**: 금융위기 국면 EPS 하락률이 **-37.0%**(Refinitiv, 월말 12MF, 유진투자증권 원표) vs **-41%**(Goldman, NTM 기준, 언론 재인용)로 보고된다. 정의(월말 12MF vs NTM)와 모집단(KOSPI vs 미확인)이 다르므로 **병기만 하고 결합하지 않는다.**

---

## 6. 요약 표

| # | 항목 | 찾음 여부 | 최고 등급 | 새 독립 source family | 기존 대비 판정 |
|---|---|---|---|---|---|
| 1 | 독립 KOSPI 12MF EPS 장기 시계열 | **부분 찾음** (계열 존재 확인, 과거 수치 미확보) | `[REPORT-B]` | `FNGUIDE_KOSPI_12MF_EPS` (차트만) · `GS_KOREA_TROUGH_STUDY` (C) | **미해소** — EPS 하강 분포는 여전히 사건 n=3 / 독립 family n=1 |
| 2 | 2026년 6~7월 동일 날짜 지수·12MF EPS·12MF PER | **찾음** | `[REPORT-A]` (지수·PER) / `[DERIVED]` (EPS) | 없음 (기존 family에 새 날짜 추가) | **해소** — 단 EPS 인쇄본은 LSEG 계열 1건뿐, PER 4.7~6.25배 상충 병기 |
| 3 | 이익 전망 개선/악화 **기업 수** breadth | **못 찾음** (프록시 3종만) | `[REPORT-C]` (프록시) | `FNGUIDE_TARGETPRICE_REPORT_COUNT` (정의 불일치) | **미해소** — 시장 전반 여부 판정 보류 유지 |
| 4 | 동일 제품 D램 고정거래가격 | **찾음** | `[REPORT-B]` (산업부 재수록) / `[REPORT-C]` (TrendForce 재인용) | `TRENDFORCE_DRAMEXCHANGE_CONTRACT` · `MOTIE_MEMORY_PRICE`(중복 의심) | **부분 해소** — DDR4 8Gb 4~6월 확보, HBM·7월 값 미확보 |

### 6-1. 독립성 요약

- 이번 조사로 확인한 **신규 고유 문서 7건**: 대신 JAEMINI(7/30), 미래에셋 ER 6월2주차·7월5주차, 미래에셋 2H26 전망, 신한 2Q26 전략, KB 2023 3월전략, TrendForce 3Q26 보도자료
- 그중 **12MF EPS 관련 문서 4건 중 독립 source family는 2개**(`REFINITIV/LSEG`, `FNGUIDE`)이며, **FnGuide 쪽은 수치가 인쇄돼 있지 않아 계산에 투입 불가**하다.
- 따라서 **“보고서 n 증가 ≠ 독립성 증가”** 원칙에 따라, 기존 핸드오프 제약(“보고서 n=1, 사건 n=3, 독립 EPS source family n=1”)을 **유지**한다.

---

## 7. 남은 공백 (다음 라운드 요구사항)

1. **FnGuide 또는 QuantiWise의 KOSPI 12MF EPS 월말 수치 시계열** — 차트가 아닌 숫자. 유료 단말(FnGuide DataGuide, QuantiWise) 필요 가능성이 높다.
2. **Goldman Sachs 원문 보고서** — “2008년 이후 6개 저점”의 표·모집단·원 데이터 제공자. 확보 시 Refinitiv 계열과 중복 제거 필요.
3. **이익추정치 상향/하향 기업 수 비율의 2026년 값** — `BREADTH-2013-01`(Bloomberg, 2013)과 동일 정의.
4. **2026년 7월 D램 고정거래가격** — 8월 초 발표분. 하락 전환 여부가 다수 보고서의 명시적 폐기 조건.
5. **HBM 계약가** — 공개 수치 전무.
6. **하나증권 원문** — 12MF PER 4.7배와 “금융위기 저점 6.3배”의 산출 정의(현재 언론 재인용 C등급).
7. **키움증권 원문** — 7/8 기준 12MF PER 6.25배의 정의.

### 7-1. `NEEDS_CLARIFICATION` (research-team-lead 앞)

```
NEEDS_CLARIFICATION
- 항목: 2026년 7월 코스피 12MF PER 수준 및 "금융위기 저점 대비 위치"
- 상황: 같은 2주 안에 제공자·정의별로 4.7 / 5.09 / 5.5(MSCI Korea) / 6.1 / 6.25배가 병존.
  또 과거 저점 배수도 6.3배(하나, C)와 11.4배(Goldman, C)로 2배 가까이 상충.
- 후보값: 6.1배 (FnGuide/미래에셋 7/23, A) vs 5.09배 (LSEG/대신 7/29, B)
  vs 4.7배 (하나/fnnews 7/30, C) / 과거저점 6.3배 vs 11.4배
- 시나리오 영향도 판단: 큼. "현재 배수가 역사적 저점 아래인가"는 낙관 시나리오의 핵심
  전제이며, 어느 계열을 채택하느냐로 결론 부호가 바뀐다. 단일 계열 채택을 금지하고
  대시보드에 병기할지 여부에 대한 팀장 판단이 필요하다.
```

---

## 8. 재현성 노트

- 모든 PDF는 원 URL에서 직접 내려받아 `pdftotext -layout`으로 본문·표를 추출했다. 차트 이미지 안의 값은 **복원하지 않았다.**
- `[DERIVED]` 12MF EPS 산식: `KOSPI ÷ 12MF PER`. 반올림 PER로 인한 범위를 함께 적었다.
- 언론 기사는 본문 전문을 확인한 뒤 인용했다. 자동 생성 요약문은 인용에서 제외했다.
- 발행일 이후 확정된 값을 당시 판단에 역삽입하지 않았다.
- 조사 중 확인했으나 **수치를 등록하지 않은 문서**: 삼성증권 2026-04 한국 전략, 미래에셋 2026 하반기 전망(수치 미인쇄 차트), KRX 기업가치제고 백서 — 모두 필요한 정의의 수치가 없었다.
