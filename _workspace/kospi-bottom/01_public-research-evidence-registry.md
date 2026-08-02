# Public Research Evidence Registry — KOSPI 이익·밸류에이션 하강 사이클

- 작성 기준일: 2026-08-01 (Asia/Seoul)
- 범위: 공개 원문에서 재현 가능한 KOSPI 12MF EPS, PER/PBR, 가격–EPS 저점 시차 및 반등 순서
- 결론 배제: 이 문서는 관측값과 자료 한계만 정리하며 투자 의견·목표지수·매매 결론을 제시하지 않는다.
- 핵심 판정: **KOSPI 12MF EPS의 세 하강 사건은 확보했지만 모두 동일한 Refinitiv 계열이다.** 따라서 아래 -32%~-37%와 9~14개월을 이 문서에서는 **“역사적 임계값”이라 부르지 않고, 단일 source-family 관측 범위**로만 기록한다.

## 0. Coverage summary

| 묶음 | 원문 보고서/공식 문서 n | 독립 source family n | 사용 가능 범위 | 판정 |
|---|---:|---:|---|---|
| KOSPI 12MF EPS 고점→저점(2008/2018/2022) | 1 (동일 표 재수록본 1건은 중복) | 1 (`REFINITIV_KOSPI_12MF_EPS`) | 사건별 관측값·단일계열 범위 | **독립성 요건 미충족; 역사적 임계값 산출 금지** |
| KOSPI 가격 저점 | 한국은행 공식 문서 + KRX 일별 원자료 | 2 (`KRX_KOSPI_PRICE_VIA_BOK`, `KRX_KOSPI_PRICE_DAILY`) | 2007년 이후 종가·저점·회복기간 | KRX 직접 원자료로 승격 |
| EPS revision breadth / 단기 변화 | 2 | 2 (`FACTSET_MSCI_EPS`, `BLOOMBERG_KOSPI_BREADTH`) | 사건 당시 단기 방향·폭 | 지수/정의가 달라 EPS 레벨과 합산 금지 |
| PER/PBR | 보고서 4건 + KRX 일별 원자료 | 5 (`KIS_UNIVERSE_FWD_VAL`, `FNGUIDE_KOSPI_VAL`, `YUANTA_KOSPI_PBR`, `DAISHIN_PBR_VIA_MEDIA`, `KRX_KOSPI_VALUATION_DAILY`) | KRX 정의의 2007년 이후 장기 분포와 저점일 비교 | KRX 정의 안에서만 분포 계산 가능; 12MF와 합산 금지 |
| 정책·거시 트리거 | 4 | 2 (`BOK_POLICY_AND_MARKETS`, `KCMI_MARKET_REVIEW`) | 사건 순서 확인 | 인과효과 크기는 추정하지 않음 |

전체 고유 문서·원자료 묶음은 11개(기존 10개 + KRX 일별 자료 묶음), 전체 source family는 10개다. 단, 이 숫자는 서로 정의가 다른 지표를 합친 커버리지일 뿐이며, **EPS 하강 분포의 유효 표본은 사건 n=3 / source family n=1**이다.

### 0-1. 2026-08-01 KRX 원자료 추가

**KRX-PRICE-DAILY-01**

- `metric_definition`: KOSPI 일별 종가·시가·고가·저가·거래량·거래대금·시가총액
- `observation_start`: 2007-01-02
- `observation_end`: 2026-07-31
- `frequency`: 거래일
- `source`: 한국거래소 `[11003] 개별지수 시세 추이`
- `url`: https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010103
- `evidence_grade`: `[OFFICIAL]`
- `source_family_id`: `KRX_KOSPI_PRICE_DAILY`
- `methodology_notes`: 분기 단위 조회 후 경계 중복 41건을 날짜 기준으로 제거. 최종 4,828거래일. `00_input/krx_kospi_price_daily_2007_2026.csv`에 보존.

**KRX-VALUATION-DAILY-01**

- `metric_definition`: KRX 화면 정의의 KOSPI 일별 PER·PBR·배당수익률
- `observation_start`: 2007-01-02
- `observation_end`: 2026-07-31
- `frequency`: 거래일
- `source`: 한국거래소 `[11007] PER/PBR/배당수익률 > 개별지수`
- `url`: https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010107
- `evidence_grade`: `[OFFICIAL]`
- `source_family_id`: `KRX_KOSPI_VALUATION_DAILY`
- `methodology_notes`: 가격 계열과 같은 4,828개 날짜를 확인. KRX 정의 안에서 과거 저점·백분위 비교에 사용. FnGuide·Refinitiv의 12MF PER/EPS로 재명명하거나 합산하지 않음. `00_input/krx_kospi_per_pbr_daily_2007_2026.csv`에 보존.

## 1. Claim registry

아래 각 레코드는 프로토콜의 필드 전체를 포함한다. `page`의 “PDF p.”는 PDF 파일의 1-based 페이지이며, 웹 화면은 화면명/표 번호를 적었다.

### EPS cycle claims

**EPS-2008-01**

- `claim_id`: EPS-2008-01
- `event`: 2008 글로벌 금융위기
- `market`: KOSPI
- `metric_definition`: KOSPI 12개월 선행 EPS, Refinitiv 집계, 월말 관측
- `observation_start`: 2008-06-30
- `observation_end`: 2009-03-31
- `value_start`: 164.5p
- `value_end`: 103.6p
- `reported_change`: -37%
- `frequency`: 월말
- `report_publisher`: 유진투자증권
- `report_date`: 2026-03-04
- `report_title`: 「KOSPI 지지선, 변동성지수: VKOSPI 코멘트」
- `url`: https://file.alphasquare.co.kr/media/pdfs/market-report/KOSPI20260305%EC%9C%A0%EC%A7%84%ED%88%AC%EC%9E%90%EC%A6%9D%EA%B6%8C.
- `page`: PDF p.3, 표 1
- `original_data_provider`: Refinitiv
- `methodology_notes`: 보고서 표의 월말 Max/Min을 그대로 전사. 재계산 `103.6 / 164.5 - 1 = -37.02%`; 보고서의 정수 반올림 -37%와 일치. 발행일 시점에 완결된 과거 자료.
- `evidence_grade`: `[REPORT-A]`
- `source_family_id`: `REFINITIV_KOSPI_12MF_EPS`

**EPS-2018-01**

- `claim_id`: EPS-2018-01
- `event`: 2018~2019 미중 무역분쟁·반도체 이익 하강
- `market`: KOSPI
- `metric_definition`: KOSPI 12개월 선행 EPS, Refinitiv 집계, 월말 관측
- `observation_start`: 2018-06-29
- `observation_end`: 2019-08-30
- `value_start`: 266.6p
- `value_end`: 182.2p
- `reported_change`: -32%
- `frequency`: 월말
- `report_publisher`: 유진투자증권
- `report_date`: 2026-03-04
- `report_title`: 「KOSPI 지지선, 변동성지수: VKOSPI 코멘트」
- `url`: 위 EPS-2008-01과 동일
- `page`: PDF p.3, 표 1
- `original_data_provider`: Refinitiv
- `methodology_notes`: 재계산 `182.2 / 266.6 - 1 = -31.66%`; 정수 반올림 -32%. 2018-06-29~2019-08-30은 약 14개월.
- `evidence_grade`: `[REPORT-A]`
- `source_family_id`: `REFINITIV_KOSPI_12MF_EPS`

**EPS-2022-01**

- `claim_id`: EPS-2022-01
- `event`: 2022~2023 긴축·반도체 이익 하강
- `market`: KOSPI
- `metric_definition`: KOSPI 12개월 선행 EPS, Refinitiv 집계, 월말 관측
- `observation_start`: 2022-01-31
- `observation_end`: 2023-03-31
- `value_start`: 275.9p
- `value_end`: 184.3p
- `reported_change`: -33%
- `frequency`: 월말
- `report_publisher`: 유진투자증권
- `report_date`: 2026-03-04
- `report_title`: 「KOSPI 지지선, 변동성지수: VKOSPI 코멘트」
- `url`: 위 EPS-2008-01과 동일
- `page`: PDF p.3, 표 1
- `original_data_provider`: Refinitiv
- `methodology_notes`: 재계산 `184.3 / 275.9 - 1 = -33.20%`; 정수 반올림 -33%. 2022-01-31~2023-03-31은 약 14개월.
- `evidence_grade`: `[REPORT-A]`
- `source_family_id`: `REFINITIV_KOSPI_12MF_EPS`

**EPS-2022-02**

- `claim_id`: EPS-2022-02
- `event`: 2022 긴축 국면 진행 중
- `market`: MSCI Korea (KOSPI와 동일 지표 아님)
- `metric_definition`: 국가별 12MF EPS 1개월 변화율, FactSet/MSCI 분류
- `observation_start`: 2022-11월 초
- `observation_end`: 2022-12-02
- `value_start`: 100(변화율 기준)
- `value_end`: 95.7(변화율 환산)
- `reported_change`: -4.3% (1M)
- `frequency`: 월간 변화율
- `report_publisher`: 미래에셋증권
- `report_date`: 2022-12-05
- `report_title`: 「Earnings Revision (12월 둘째주)」
- `url`: https://securities.miraeasset.com/bbs/download/2098058.pdf?attachmentId=2098058
- `page`: PDF p.2, 그림 4
- `original_data_provider`: FactSet, MSCI
- `methodology_notes`: KOSPI EPS 레벨이 아닌 MSCI Korea 변화율. EPS-2022-01의 독립 교차 “방향” 확인에만 쓰고 레벨·하강률 합산 금지.
- `evidence_grade`: `[REPORT-A]`
- `source_family_id`: `FACTSET_MSCI_EPS`

**BREADTH-2013-01**

- `claim_id`: BREADTH-2013-01
- `event`: 2013 이익 하향 집중 국면
- `market`: KOSPI / MSCI Korea 병기
- `metric_definition`: KOSPI 2013년 예상 EPS 1개월 변화 및 실적전망 상향/하향 종목 수 비율
- `observation_start`: 2013-01월 말경
- `observation_end`: 2013-02월 말경
- `value_start`: 미제시
- `value_end`: KOSPI 2013E EPS -2.5%; 상향/하향 종목 수 비율 28%
- `reported_change`: -2.5% (1M); breadth 28%
- `frequency`: 1개월
- `report_publisher`: 미래에셋증권
- `report_date`: 2013년 2월(원문 메타데이터상 주간 코멘트)
- `report_title`: 「Weekly comment — 실적 하향 조정 강도, 금융위기 이후 최대」
- `url`: https://securities.miraeasset.com/bbs/board/message/file.do?attachmentId=2035584
- `page`: 원문 차트 페이지(검색 원문상 KOSPI 12MF EPS / 상향·하향 비율 도표; 정적 페이지 번호 확인 불가)
- `original_data_provider`: Bloomberg
- `methodology_notes`: 차트 전체 시계열의 정확한 좌표는 복원하지 않음. 본문 명시값만 기록. “금융위기 최저 22.5%에 근접”은 동일 보고서의 역사 비교이나 원표 미확보로 B.
- `evidence_grade`: `[REPORT-B]`
- `source_family_id`: `BLOOMBERG_KOSPI_BREADTH`

### Price-low and lag claims

**PRICE-2008-01**

- `claim_id`: PRICE-2008-01
- `event`: 2008 글로벌 금융위기
- `market`: KOSPI
- `metric_definition`: 종가 기준 연중 저점
- `observation_start`: 2008-10-24
- `observation_end`: 2008-10-24
- `value_start`: 938.8p
- `value_end`: 938.8p
- `reported_change`: 해당 없음
- `frequency`: 일간 종가
- `report_publisher`: 한국은행
- `report_date`: 2008-12
- `report_title`: 「Quarterly Bulletin, December 2008」
- `url`: https://file-cdn.bok.or.kr/portal/b728e8a8dd39a6943610475c37ced691/1/FILE_201803300852280351.pdf
- `page`: p.18
- `original_data_provider`: KOSPI/한국거래소 가격, 한국은행 재공표
- `methodology_notes`: 한국은행은 10/24 938.8을 2008년 저점으로 명시. EPS 저점(2009-03-31)까지 `[DERIVED from OFFICIAL + REPORT-A]` 158일, 약 5.2개월. 장중 저점과 혼용하지 않음.
- `evidence_grade`: `[OFFICIAL]`; 시차는 `[DERIVED]`
- `source_family_id`: `KRX_KOSPI_PRICE_VIA_BOK`

**PRICE-2018-01**

- `claim_id`: PRICE-2018-01
- `event`: 2018~2019 미중 무역분쟁·반도체 이익 하강
- `market`: KOSPI
- `metric_definition`: 종가 기준 2018년 연중 저점
- `observation_start`: 2018-10-29
- `observation_end`: 2018-10-29
- `value_start`: 1,996p (공식 간행물 반올림)
- `value_end`: 1,996p
- `reported_change`: 해당 없음
- `frequency`: 일간 종가
- `report_publisher`: 한국은행
- `report_date`: 2019년 1분기 간행물
- `report_title`: 「Quarterly Bulletin」(2018년 4분기 금융시장)
- `url`: https://file-cdn.bok.or.kr/eng/5774778c8418e247cc66dd3e191378e0/1/201905270613395670.pdf
- `page`: 주식시장 동향 절(검색 가능한 원문 본문; 정적 인쇄 페이지 미확인)
- `original_data_provider`: KOSPI/한국거래소 가격, 한국은행 재공표
- `methodology_notes`: EPS 저점(2019-08-30)까지 `[DERIVED]` 305일, 약 10.0개월. 가격은 EPS보다 먼저 저점. 월말 EPS와 일간 가격의 주기 차이를 유지.
- `evidence_grade`: `[OFFICIAL]`; 시차는 `[DERIVED]`
- `source_family_id`: `KRX_KOSPI_PRICE_VIA_BOK`

**PRICE-2022-01**

- `claim_id`: PRICE-2022-01
- `event`: 2022~2023 긴축·반도체 이익 하강
- `market`: KOSPI
- `metric_definition`: 2022년 하락 국면 종가 저점 후보
- `observation_start`: 2022-09-30
- `observation_end`: 2022-09-30
- `value_start`: 2,155.49p
- `value_end`: 2,155.49p
- `reported_change`: 해당 없음
- `frequency`: 일간 종가
- `report_publisher`: 한국거래소 데이터시스템(조회 화면)
- `report_date`: 조회일 2026-08-01
- `report_title`: 「주가지수 월별 추이」 화면 [41001]
- `url`: https://data.krx.co.kr/contents/MDC/EASY/main/MDCEASY001.jsp
- `page`: 화면 [41001], KOSPI/2022-09 조회
- `original_data_provider`: 한국거래소
- `methodology_notes`: 정적 다운로드 파일을 보존하지 못해 공식 조회 재현 경로만 기록. EPS 저점(2023-03-31)까지 `[DERIVED]` 182일, 약 6.0개월. 이 값이 최종 전 구간 저점인지 재검증용 CSV가 필요하므로 시차는 B 취급.
- `evidence_grade`: `[OFFICIAL-B]`; 시차는 `[DERIVED from OFFICIAL-B + REPORT-A]`
- `source_family_id`: `KRX_KOSPI_PRICE_VIA_BOK`

### Valuation claims

**VAL-2018-01**

- `claim_id`: VAL-2018-01
- `event`: 2018 무역분쟁 진행 중
- `market`: 한국투자증권 KOSPI 유니버스
- `metric_definition`: 제시 KOSPI 밴드에 대응하는 12MF PER/PBR
- `observation_start`: 2018-08-27
- `observation_end`: 2018-09 전망
- `value_start`: PER 8.72x / PBR 0.94x
- `value_end`: PER 9.42x / PBR 1.01x
- `reported_change`: 해당 없음
- `frequency`: 월간 전략 밴드
- `report_publisher`: 한국투자증권
- `report_date`: 2018-08-27
- `report_title`: 「9월 전략: 상승 5파는 가능한가」
- `url`: https://file.mk.co.kr/imss/write/20180827143037__00.pdf
- `page`: PDF p.1
- `original_data_provider`: 한국투자증권 유니버스 추정실적
- `methodology_notes`: 실제 저점 관측값이 아니라 전망 KOSPI 밴드 2,250~2,430에 대응하는 배수. 역사 저점 표본에서 제외하고 가정 격리.
- `evidence_grade`: `[REPORT-D][ASSUMPTION]`
- `source_family_id`: `KIS_UNIVERSE_FWD_VAL`

**VAL-2022-01**

- `claim_id`: VAL-2022-01
- `event`: 2022 긴축 국면
- `market`: KOSPI
- `metric_definition`: KOSPI PBR
- `observation_start`: 2022-06-15
- `observation_end`: 2022-06-16
- `value_start`: 1.0x 하회
- `value_end`: 1.0x 하회
- `reported_change`: 정확 수치 미제시
- `frequency`: 일간 스냅숏
- `report_publisher`: 유안타증권
- `report_date`: 2022-06-16
- `report_title`: 「단기 하락세 진정 가능성」
- `url`: https://www.myasset.com/myasset/research/rs_list/rs_view.cmd?SEQ=180692&cd006=&cd007=RB01&cd008=RB01A
- `page`: 웹 본문 2절; 첨부 PDF 링크 제공
- `original_data_provider`: 보고서에 별도 표기 확인 불가
- `methodology_notes`: “1배 하회”만 사용. 2008년 말 및 2018-10~2020년 중반에도 크게 하회했다는 정성 비교는 수치 분포 계산에서 제외.
- `evidence_grade`: `[REPORT-B]`
- `source_family_id`: `YUANTA_KOSPI_PBR`

**VAL-2020-01**

- `claim_id`: VAL-2020-01
- `event`: 2020 코로나 급락
- `market`: KOSPI
- `metric_definition`: 확정실적 기준 PBR
- `observation_start`: 2020-03-23
- `observation_end`: 2020-03-23
- `value_start`: 0.586x
- `value_end`: 0.586x
- `reported_change`: 2000년 이후 최저라는 대신증권 코멘트
- `frequency`: 일간 스냅숏
- `report_publisher`: 아시아경제(대신증권 발언 재인용)
- `report_date`: 2020-03-23
- `report_title`: 「Korean Stock Market Below Liquidation Value...」
- `url`: https://www.asiae.co.kr/en/article/2020032309212223230
- `page`: 웹 기사
- `original_data_provider`: 대신증권 추정; 원 데이터 제공자 미확인
- `methodology_notes`: 증권사 원문 보고서 미확보. 단독 임계값·정밀 비교에 사용 금지.
- `evidence_grade`: `[REPORT-C]`
- `source_family_id`: `DAISHIN_PBR_VIA_MEDIA`

**VAL-2026-01**

- `claim_id`: VAL-2026-01
- `event`: 2026-01 현재 스냅숏
- `market`: KOSPI
- `metric_definition`: KOSPI 12MF PER 및 TTM PBR
- `observation_start`: 2026-01-16(보고서 직전 시장일)
- `observation_end`: 2026-01-19
- `value_start`: KOSPI 4,798p
- `value_end`: 12MF PER 10.3x / PBR(TTM) 1.54x
- `reported_change`: 3년 평균 PER 10.3x, PBR 0.97x 대비 위치 제시
- `frequency`: 주간
- `report_publisher`: 미래에셋증권
- `report_date`: 2026-01-19
- `report_title`: 「Earnings Revision (1월 4주차) — 한국 기업들의 이익 변화와 밸류에이션」
- `url`: https://securities.miraeasset.com/bbs/download/2141753.pdf?attachmentId=2141753
- `page`: PDF p.9, 그림 39~40
- `original_data_provider`: FnGuide
- `methodology_notes`: PER은 12MF, PBR은 TTM이라 분모 시점이 다름. 과거 저점과 직접 합산하지 않음.
- `evidence_grade`: `[REPORT-A]`
- `source_family_id`: `FNGUIDE_KOSPI_VAL`

### Trigger claims

**TRIGGER-2008-01**

- `claim_id`: TRIGGER-2008-01
- `event`: 2008 글로벌 금융위기
- `market`: 한국 통화·주식시장
- `metric_definition`: 정책 실행 날짜와 KOSPI 종가 저점/반등 순서
- `observation_start`: 2008-10-09
- `observation_end`: 2008-10-30
- `value_start`: 기준금리 -25bp(10/9)
- `value_end`: 기준금리 -75bp(10/27), 한미 통화스왑 발표(10/30)
- `reported_change`: KOSPI 10/24 939p 저점 후 반등
- `frequency`: 사건일
- `report_publisher`: 한국은행·기획재정부·금융위원회
- `report_date`: 2008-11-07 주간보
- `report_title`: 「Weekly Economy Bulletin — October Financial Market Trends」
- `url`: https://file-cdn.bok.or.kr/eng/e7ed4616dd97a4b9aa1e57344c96c4ed/1/FILE_201803300852344291.pdf
- `page`: 주간보의 BOK ‘October Financial Market Trends’ 절
- `original_data_provider`: 한국은행
- `methodology_notes`: 날짜 순서는 `금리인하(10/9) → 주가 종가저점(10/24) → 75bp 인하(10/27) → 통화스왑 발표(10/30) → EPS 저점(2009/3/31)`. 보고서가 반등 요인으로 금리 인하·스왑을 서술하지만 개별 기여율은 측정하지 않음.
- `evidence_grade`: `[OFFICIAL]`
- `source_family_id`: `BOK_POLICY_AND_MARKETS`

**TRIGGER-2018-01**

- `claim_id`: TRIGGER-2018-01
- `event`: 2018~2019 무역분쟁
- `market`: KOSPI
- `metric_definition`: 주가 저점 이후 반등 당시 거시·정책 재료
- `observation_start`: 2018-10-29
- `observation_end`: 2019-03
- `value_start`: KOSPI 1,996p(10/29 저점)
- `value_end`: 2019년 초 회복
- `reported_change`: Fed 정상화 속도 조정 기대와 미중 협상 진전 기대가 높아지며 회복
- `frequency`: 분기
- `report_publisher`: 한국은행
- `report_date`: 2019년 1분기 간행물
- `report_title`: 「Quarterly Bulletin」
- `url`: https://file-cdn.bok.or.kr/eng/5774778c8418e247cc66dd3e191378e0/1/201905270613395670.pdf
- `page`: 주식시장 동향 절
- `original_data_provider`: 한국은행/한국거래소
- `methodology_notes`: 순서 `주가저점(2018/10/29) → 정책·협상 기대에 2019년 초 가격 회복 → EPS저점(2019/8/30)`. 기대 형성의 정확한 사건일과 기여도는 공백.
- `evidence_grade`: `[OFFICIAL-B]`
- `source_family_id`: `BOK_POLICY_AND_MARKETS`

**TRIGGER-2022-01**

- `claim_id`: TRIGGER-2022-01
- `event`: 2022 긴축
- `market`: KOSPI / MSCI Korea
- `metric_definition`: 가격 저점 뒤 이익 하향 지속 여부
- `observation_start`: 2022-09-30
- `observation_end`: 2022-12-02
- `value_start`: KOSPI 종가 저점 후보 2,155.49p
- `value_end`: MSCI Korea 12MF EPS 1M -4.3%
- `reported_change`: 가격 저점 후보 뒤에도 이익 전망 하향 지속
- `frequency`: 일간 가격 / 월간 EPS
- `report_publisher`: 한국거래소·미래에셋증권
- `report_date`: 2022-12-05(EPS 보고서)
- `report_title`: 「Earnings Revision (12월 둘째주)」
- `url`: https://securities.miraeasset.com/bbs/download/2098058.pdf?attachmentId=2098058
- `page`: PDF p.2
- `original_data_provider`: 한국거래소; FactSet/MSCI
- `methodology_notes`: 가격과 EPS의 시장 정의가 KOSPI/MSCI Korea로 다르므로 방향 순서만 사용. EPS-2022-01의 KOSPI EPS 저점은 2023-03-31.
- `evidence_grade`: `[DERIVED from OFFICIAL-B + REPORT-A]`
- `source_family_id`: `KRX_KOSPI_PRICE_VIA_BOK+FACTSET_MSCI_EPS`

## 2. Historical EPS cycle table

| 사건 | EPS 고점 | EPS 저점 | 하락률 | 하향 기간 | 종가 기준 주가 저점 | 주가→EPS 저점 시차 | 증거 |
|---|---:|---:|---:|---:|---|---:|---|
| 2008 금융위기 | 164.5 (2008-06-30) | 103.6 (2009-03-31) | -37.0% | 약 9개월 | 938.8 (2008-10-24) | +158일, 약 5.2개월 | EPS `[REPORT-A]` Refinitiv; 가격 `[OFFICIAL]` BOK/KRX |
| 2018~2019 무역·반도체 하강 | 266.6 (2018-06-29) | 182.2 (2019-08-30) | -31.7% | 약 14개월 | 1,996 (2018-10-29) | +305일, 약 10.0개월 | EPS `[REPORT-A]` Refinitiv; 가격 `[OFFICIAL]` BOK/KRX |
| 2022~2023 긴축·반도체 하강 | 275.9 (2022-01-31) | 184.3 (2023-03-31) | -33.2% | 약 14개월 | 2,155.49 (2022-09-30, 후보) | +182일, 약 6.0개월 | EPS `[REPORT-A]` Refinitiv; 가격 `[OFFICIAL-B]` KRX 조회 |

관측 범위는 하락률 -31.7%~-37.0%, 기간 약 9~14개월, 가격 저점 선행 약 5~10개월이다. 그러나 EPS 세 사건이 모두 `REFINITIV_KOSPI_12MF_EPS` 한 계열이고, 시차의 가격축도 `KRX_KOSPI_PRICE_VIA_BOK` 한 계열이므로 **분포·백분위·역사적 임계값으로 승격하지 않는다.**

## 3. Trigger timeline evidence

| 사건 | 확인된 순서 | 관측 가능한 트리거 | 제한 |
|---|---|---|---|
| 2008 | 금리인하(10/9) → KOSPI 종가저점(10/24) → 75bp 추가 인하(10/27) → 한미 통화스왑 발표(10/30) → EPS 저점(2009/3/31) | 유동성·환율 안전판 및 급격한 정책완화 | 주가 저점은 후속 대책보다 먼저여서 단일 정책을 “저점 원인”으로 단정할 수 없음 |
| 2018~2019 | KOSPI 저점(2018/10/29) → Fed 정상화 속도 조정·미중 협상 진전 기대 속 2019년 초 회복 → EPS 저점(2019/8/30) | 할인율·무역갈등 기대 변화 | 기대의 최초 사건일, 외국인 수급 전환일, 신용스프레드 날짜 미확보 |
| 2022~2023 | KOSPI 저점 후보(2022/9/30) → MSCI Korea EPS 1M -4.3%(12/2) → KOSPI EPS 저점(2023/3/31) | 가격이 이익 하향 종료보다 선행 | 정책·신용·환율·수급의 동일 빈도 원자료 미확보; 단일 반등 트리거 특정 불가 |

공통적으로 확인되는 것은 “가격 저점이 EPS 저점보다 빨랐다”는 순서다. 이것은 세 사건의 관측 사실이지 미래 사건의 충분조건이 아니다.

## 4. Source-family map

| 발행사/문서 | 원 데이터 제공자 | `source_family_id` | 중복 판정 |
|---|---|---|---|
| 유진투자증권 2026-03-04 Spot Comment | Refinitiv | `REFINITIV_KOSPI_12MF_EPS` | EPS 3개 사건의 유일 계열 |
| 유진투자증권 2025-04-15 자료(동일 표 재수록) | Refinitiv | `REFINITIV_KOSPI_12MF_EPS` | **중복; 보고서 n 증가에 사용하지 않음** |
| 미래에셋증권 2022-12-05 | FactSet, MSCI | `FACTSET_MSCI_EPS` | 독립. 단 MSCI Korea라 KOSPI 레벨과 비동일 |
| 미래에셋증권 2013 Weekly comment | Bloomberg | `BLOOMBERG_KOSPI_BREADTH` | 독립. breadth/2013E 지표 |
| 한국은행 공식 간행물·KRX 조회 | KRX/KOSPI, BOK | `KRX_KOSPI_PRICE_VIA_BOK` | 가격 계열끼리는 동일 family |
| 한국은행 통화정책·시장 문서 | BOK | `BOK_POLICY_AND_MARKETS` | 정책 계열; 가격 계열과 목적상 분리 |
| 한국투자증권 2018-08-27 | 자체 유니버스 추정 | `KIS_UNIVERSE_FWD_VAL` | 독립이나 전망 밴드(D) |
| 미래에셋증권 2026-01-19 | FnGuide | `FNGUIDE_KOSPI_VAL` | 독립. 2026 스냅숏 |
| 유안타증권 2022-06-16 | 미표기 | `YUANTA_KOSPI_PBR` | 독립성 확인 불완전(B) |
| 아시아경제 2020-03-23의 대신증권 인용 | 대신증권 추정, 원 제공자 미확인 | `DAISHIN_PBR_VIA_MEDIA` | C; 원문 미확보 |
| 자본시장연구원 2019 시장 리뷰 | KCMI/시장자료 | `KCMI_MARKET_REVIEW` | 정성 트리거 보조, 수치 분포 미사용 |
| 미래에셋증권 「2026 하반기 전망」(2026-05-22) | FnGuide | `FNGUIDE_KOSPI_12MF_EPS` | 신규(2026-08-02 추가조사). Refinitiv와 독립 계열 존재는 확인, 수치는 차트 미인쇄로 미확보(B) |
| 신한투자증권 「2Q26 주식시장 전망」(2026-04-01) | 에프앤가이드/LSEG 혼용 | `FNGUIDE_KOSPI_12MF_EPS`(잠정) | 신규. 같은 보고서 안에서 제공자 표기가 혼재해 A가 아닌 B |
| Goldman Sachs 한국 전략 코멘트(2026-07초, 언론 재인용) | 미확인 | `GS_KOREA_TROUGH_STUDY` | 신규(C). 원 제공자 미확인이라 Refinitiv 계열과 중복 제거 불가 |
| 대신증권 「[AI Insight] KOSPI…」(2026-07-30, JAEMINI) | LSEG | `REFINITIV_KOSPI_12MF_EPS` | **중복**. AI 생성물 면책 명시로 B |
| 파이낸셜뉴스 2026-07-19 (에프앤가이드 집계) | FnGuide | `FNGUIDE_TARGETPRICE_REPORT_COUNT` | 신규(C). 목표주가 리포트 건수이며 이익추정 상향/하향 기업 수 아님 — breadth 대체 금지 |
| 하나증권 이재만 실장(fnnews 2026-08-02 재인용) | 미표기 | `HANA_KOSPI_VAL_VIA_MEDIA` | 신규(C). 원문 미확보, 저점 배수 6.3배가 Goldman 11.4배와 상충 |
| 이포커스/ZDNet Korea(2026-05~07, TrendForce 인용) | TrendForce/DRAMeXchange | `TRENDFORCE_DRAMEXCHANGE_CONTRACT` | 신규(C). DDR4 8Gb 등 월별 고정거래가 계열, 기존에 DRAM 계열 없었음 |
| 산업통상자원부 보도자료(2026-07-01, 대신 JAEMINI 재수록) | 산업부 자체 집계(TrendForce 재공표 추정) | `MOTIE_MEMORY_PRICE` | 신규(B). NAND 128Gb 값이 DRAMeXchange와 사실상 일치 → `TRENDFORCE_DRAMEXCHANGE_CONTRACT`와 동일 family로 취급 권고 |

## 5. Assumption quarantine

| 항목 | 격리 내용 | 등급 | 사용 금지 범위 |
|---|---|---|---|
| 2026 KOSPI 이익 -20% 하향 | 유진 보고서가 스트레스 계산을 위해 선택한 가정. 관측된 하향률 아님 | `[REPORT-D][ASSUMPTION]` | 현재 EPS 하락률·역사 임계값으로 표현 금지 |
| KOSPI ±500p 밴드 | 2020년 이후 적정지수 주변 평균 편차를 이용한 보고서 가정 | `[REPORT-D][ASSUMPTION]` | 가격 저점 확정값으로 사용 금지 |
| 2018년 9월 PER 8.72~9.42 / PBR 0.94~1.01 | 전망 지수밴드와 자체 유니버스 추정을 결합한 값 | `[REPORT-D][ASSUMPTION]` | 실제 2018 저점 배수로 사용 금지 |
| “EPS 10%/20% 하향” | 본 레지스트리에서 관측하지 않은 임의 민감도 | `[ASSUMPTION]` | 과거 실제 하향률, 트리거, 확률로 표현 금지 |
| 2008/2018/2022 단일계열 평균 약 -34% | 산술 계산은 가능하나 독립 family=1 | `[DERIVED—QUARANTINED]` | “평균적 하락” 또는 역사 임계값으로 사용 금지 |
| 가격→EPS 저점 시차 평균 | 빈도(일간/월말)와 사건 정의가 다르고 n=3 | `[DERIVED—QUARANTINED]` | 미래 저점 날짜 예측에 사용 금지 |

## 6. Coverage gaps

1. **독립 EPS 원계열 부재**: FnGuide·QuantiWise 또는 FactSet의 동일 정의 KOSPI 12MF EPS 장기 월말 시계열이 필요하다. 현재 Refinitiv 외 계열은 MSCI Korea 변화율이나 영업이익이라 동일 표본이 아니다.
2. **2020 KOSPI 12MF EPS 완결 사이클**: 코로나 국면의 KOSPI EPS 고점·저점·하락률·저점일을 공개 원문 표에서 확보하지 못했다. 글로벌 S&P 500 사례는 시장 불일치로 제외했다.
3. **저점 PER/PBR의 통일 정의**: 12MF PER, 12MF PBR, TTM PBR, 확정실적 PBR이 혼재한다. 2008/2018/2020/2022 각 가격 저점일의 동일 제공자·동일 정의 스냅숏이 필요하다.
4. **저점 이후 3·6·12개월 성과**: KRX 가격 원자료 CSV를 보존하지 못해 이 문서에서 계산하지 않았다. 조회 URL만으로 정밀 성과를 확정하지 않는다.
5. **2022 가격 저점 공식 정적 파일**: KRX 화면 재현은 가능하지만 다운로드 파일·조회 파라미터를 원장에 고정하지 못했다. 따라서 시차는 B로 낮췄다.
6. **정책/신용/환율/수급 동일 빈도 패널**: 2008은 정책 날짜가 확보됐으나, 2018·2022는 CDS·회사채 스프레드·원/달러·외국인 누적순매수 전환일이 같은 빈도로 정렬되지 않았다.
7. **이익수정 breadth 장기 분포**: 2013 Bloomberg 한 사례와 2022 FactSet 국가 EPS 변화만 확보됐다. 상향/하향 종목 수 비율의 2008·2018·2022 동일 정의 자료가 필요하다.
8. **원문 부재**: 2020 확정실적 PBR 0.586x는 대신증권 원문이 아니라 언론 재인용(C)이다. 원문 PDF 확보 전 단독 사용 금지.
9. **Goldman Sachs ‘6개 저점’ 요약**: 공개 검색에서 Goldman Sachs 원문 보고서·표·발행일·페이지·원 데이터 제공자를 확인하지 못했다. 제3자 요약값도 이 레지스트리에서 재현 가능한 형태로 확보하지 못했으므로 **C등급 수치로조차 등록하지 않고 원문 미확보 공백**으로 둔다. 향후 원문 또는 추적 가능한 재인용을 확보하더라도 Refinitiv/FactSet 등 원 제공자를 확인해 기존 family와 중복 제거해야 한다.

### 6-1. 2026-08-02 추가조사 결과 (상세는 `06_gap_research_followup.md`)

- 위 갭 #1(독립 EPS 원계열)은 **부분 진전**: FnGuide가 KOSPI 12MF EPS 장기 계열을 실제로 공표한다는 사실은 공개 PDF 차트로 확인됐다(`FNGUIDE_KOSPI_12MF_EPS`). 다만 차트에 수치가 인쇄돼 있지 않아 2008/2018/2022 하락률 계산에는 아직 투입할 수 없다. **공백의 성격이 "계열 부재"에서 "수치 공개본 부재"로 바뀌었을 뿐, 사건 n=3/독립 family n=1 제약은 유지된다.**
- Goldman Sachs 갭(#9)은 추적 가능한 언론 재인용(EPS -33%/-41%, 저점 선행 PER 11.4배)을 확보해 **C등급 등록까지는 도달**했으나 원 데이터 제공자 미표기로 여전히 Refinitiv 계열과 중복 제거 불가.
- 2026년 6~7월 동일 날짜 지수·PER 스냅숏(과거 §미확인 항목 2)은 **해소**됐다. 단 제공자·정의별로 12MF PER이 4.7~6.25배로 상충하므로 대시보드에는 단일값이 아니라 병기·NEEDS_CLARIFICATION으로 반영해야 한다.
- Breadth(상향/하향 기업 수 비율, 갭 #7)는 **여전히 미해소**. 목표주가 리포트 건수(`FNGUIDE_TARGETPRICE_REPORT_COUNT`)·3개월 이익추정 변화율·국가단위 EPS 변화율 3종 프록시만 확보했고 정의가 달라 `BREADTH-2013-01`과 이어붙일 수 없다.
- D램 고정거래가격은 신규 계열(`TRENDFORCE_DRAMEXCHANGE_CONTRACT`)로 **부분 해소**: DDR4 8Gb 등 4~6월 월별 데이터 확보. HBM 계약가와 2026년 7월 값은 여전히 미확보(8월 초 발표 예정).

## 7. Reproducibility notes and source list

- `[DERIVED]` 하락률 계산식: `value_end / value_start - 1`.
- 기간은 보고서의 월말 날짜 간 달력 개월을 근사했고, 시차 일수는 `EPS 저점일 - KOSPI 종가 저점일`이다.
- 가격은 종가 기준으로 통일했다. 장중 저점은 같은 표에 섞지 않았다.
- 차트 육안 복원값은 사용하지 않았다. 본문/표에 숫자가 없는 도표는 정성 증거로만 남겼다.
- 검색으로 확인한 유진투자증권 2025-04-15 자료는 같은 Refinitiv 표를 재수록하므로 독립 보고서나 family로 세지 않았다: https://www.eugenefn.com/common/files/amail/20250415_B_buykkang_175.pdf
- 한국은행 2008년 10월 27일 75bp 인하 원문: https://www.bok.or.kr/eng/bbs/E0000627/view.do?menuNo=400022&nttId=144756&pageIndex=15
- 한국은행의 위기 후 유동성 공급 정리(장기·비정례 RP, 담보/대상 확대 등): https://file-cdn.bok.or.kr/eng/57d39103d32d601c5d588183944be622/1/FILE_201803300855245411.pdf (p.113)
- 자본시장연구원 2019 시장 리뷰: https://www.kcmi.re.kr/publications/pub_detail_view?cno=5274&syear=2019&zcd=002001016&zno=1478

### Handoff constraint

후속 historical-market-analyst와 valuation-quant-analyst는 세 EPS 사건을 비교 사례로 사용할 수 있으나, 반드시 **“보고서 n=1, 사건 n=3, 독립 EPS source family n=1”**을 함께 표기해야 한다. 두 번째 동일 정의 독립 계열을 확보하기 전에는 -32%~-37%, 9~14개월, 5~10개월 시차를 “역사적 임계값/정상 범위/확률분포”로 부르지 않는다.
