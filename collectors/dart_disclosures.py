#!/usr/bin/env python3
"""DART(전자공시) 공시검색 API를 research_snapshot이 읽는 JSON 레코드로 변환하는 고정 어댑터.

사용 전 준비:
  1. https://opendart.fss.or.kr 에서 본인 명의로 API 키를 발급받는다 (무료, 이메일 인증).
  2. export DART_API_KEY="발급받은_키"   (절대 이 파일이나 request.json에 직접 쓰지 않는다)
  3. 조회할 기업의 DART corp_code(8자리, 종목코드와 다른 DART 전용 식별자)를 확인한다.
     DART 사이트에서 기업명으로 검색하거나, corpCode.xml 마스터 파일에서 찾는다.

이 스크립트는 stdout에 JSON 레코드 배열만 출력한다 (research_snapshot의 generated_json 계약).
진단 메시지는 stderr로만 보낸다.

주의: DART API 응답 필드명(report_nm, rcept_dt 등)은 공개 문서 기준으로 작성했으나,
실제 키로 첫 호출을 해본 뒤 아래 to_records()의 매핑을 반드시 재확인할 것.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request

API_URL = "https://opendart.fss.or.kr/api/list.json"


def fetch_disclosures(api_key: str, corp_code: str, bgn_de: str, end_de: str) -> list[dict]:
    params = {
        "crtfc_key": api_key,
        "corp_code": corp_code,
        "bgn_de": bgn_de,
        "end_de": end_de,
        "page_count": "100",
    }
    url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    request = urllib.request.Request(url, headers={"User-Agent": "research-snapshot/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))

    status = payload.get("status")
    if status != "000":
        raise RuntimeError(f"DART API error {status}: {payload.get('message')}")

    return payload.get("list", [])


def _format_date(yyyymmdd: str | None) -> str | None:
    if not yyyymmdd or len(yyyymmdd) != 8:
        return yyyymmdd
    return f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:]}"


def to_records(disclosures: list[dict]) -> list[dict]:
    records = []
    for item in disclosures:
        # research_snapshot treats (entity, metric, observed_at, source_id) as the
        # dedup key. A company can file several disclosures on the same day, so the
        # metric must carry the DART accession number (rcept_no) to stay unique --
        # a plain "disclosure" label collides across same-day filings.
        records.append(
            {
                "company": item.get("corp_name"),
                "metric": f"disclosure:{item.get('rcept_no')}",
                "value": item.get("report_nm"),
                "unit": "text",
                "observed_at": _format_date(item.get("rcept_dt")),
                "rcept_no": item.get("rcept_no"),
                "flr_nm": item.get("flr_nm"),
                "remark": item.get("rm"),
            }
        )
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corp-code", required=True, help="DART corp_code, 8자리 (종목코드 아님)")
    parser.add_argument("--bgn-de", required=True, help="조회 시작일 YYYYMMDD")
    parser.add_argument("--end-de", required=True, help="조회 종료일 YYYYMMDD")
    args = parser.parse_args()

    api_key = os.environ.get("DART_API_KEY")
    if not api_key:
        print("DART_API_KEY 환경변수가 설정돼 있지 않습니다.", file=sys.stderr)
        return 1

    try:
        disclosures = fetch_disclosures(api_key, args.corp_code, args.bgn_de, args.end_de)
    except Exception as error:  # noqa: BLE001 - collector must fail closed, never crash silently
        print(f"DART API 호출 실패: {error}", file=sys.stderr)
        return 1

    print(json.dumps(to_records(disclosures), ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
