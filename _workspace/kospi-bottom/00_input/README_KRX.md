# KRX 코스피 일별 원자료

## 들어 있는 파일

- `krx_kospi_price_daily_2007_2026.csv`: 코스피 일별 시세
- `krx_kospi_per_pbr_daily_2007_2026.csv`: 같은 날짜의 코스피 PER·PBR·배당수익률
- `krx_kospi_price_per_pbr_daily_2007_2026.xlsx`: 위 두 CSV와 출처 설명을 한 파일에 묶은 검토용 문서

## 범위와 출처

- 기간: 2007-01-02 ~ 2026-07-31
- 거래일: 4,828일
- 시세 화면: <https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010103>
- PER·PBR 화면: <https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010107>
- 수집일: 2026-08-01

KRX의 한 번 조회 가능 기간 제한을 지키기 위해 분기 단위로 조회했다. 각 분기 첫날에 직전 거래일이 함께 반환되는 경우가 있어 날짜가 같은 41개 행을 제거했다. 두 CSV의 날짜는 모두 일치한다.

## 단위

- `change_pct`, `dividend_yield_pct`: 퍼센트 숫자. 예: `-1.25`는 `-1.25%`.
- `volume_thousand_shares`: 천 주.
- `trading_value_million_krw`, `market_cap_million_krw`: 백만 원.

## 꼭 지킬 점

이 파일의 `per`는 KRX `[11007] PER/PBR/배당수익률` 화면이 제공한 값이다. FnGuide·QuantiWise·FactSet의 `12MF PER` 또는 `12MF EPS`로 바꾸어 부르거나 두 계열을 그대로 이어 붙이면 안 된다. 이 원자료는 다음 용도로 쓴다.

- 같은 KRX 정의 안에서 과거 저점의 PER·PBR 비교
- 가격 저점일과 가치평가 값의 날짜 일치 확인
- KRX 정의의 장기 분포 계산

앞으로 12개월 예상이익을 쓰는 분석에는 별도의 `12MF EPS/PER` 자료가 여전히 필요하다.

## 대표 확인값

| 날짜 | 코스피 종가 | PER | PBR | 배당수익률(%) |
|---|---:|---:|---:|---:|
| 2008-10-24 | 938.75 | 7.40 | 0.78 | 3.15 |
| 2020-03-19 | 1,457.64 | 12.09 | 0.59 | 3.03 |
| 2022-09-30 | 2,155.49 | 9.26 | 0.83 | 2.30 |
| 2026-07-30 | 5,593.56 | 15.28 | 1.60 | 1.13 |
| 2026-07-31 | 6,595.45 | 18.03 | 1.88 | 0.96 |
