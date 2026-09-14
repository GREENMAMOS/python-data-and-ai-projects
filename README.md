# Data & AI Projects

반도체·제조 데이터 분석을 중심으로, Python을 활용한 데이터 수집·전처리와 AI-assisted 개발 프로젝트를 정리한 포트폴리오입니다.

주요 관심 분야는 제조 데이터 분석이며, 그 외 프로젝트는 데이터 수집·웹 구현·생성형 AI 활용 역량을 보조적으로 보여줍니다.

## Featured Project

### [반도체 공정 데이터 분석](https://github.com/GREENMAMOS/semiconductor-process-data-analysis)

공정 조건과 계측 결과를 비교·분석하며 반도체 제조 데이터 해석 역량을 정리한 프로젝트입니다.

- Python 기반 데이터 전처리
- 공정 변수 비교 및 시각화
- 통계적 데이터 해석
- 제조·공정 데이터 분석 관점의 결과 정리

---

## Supporting Projects

| 프로젝트 | 목적 | 주요 기술 | 보여주는 역량 |
|---|---|---|---|
| [사이별 MBTI (SHYSTAR)](https://shystar.greenmamos.workers.dev) | 친구들의 MBTI 관계를 지도처럼 시각화하고 궁합 점수를 제공하는 웹서비스 | TypeScript, React, Cloudflare Workers, D1, 생성형 AI | 서비스 기획, 풀스택 구현, DB 연동, 배포 |
| [RISS 논문 정보 수집](projects/riss/README.md) | 검색 목록과 상세페이지의 정보를 함께 비교하기 | Python, requests, BeautifulSoup | 요청 파라미터 구성, 데이터 수집·파싱, 누락값 처리 |
| [쇼핑몰 상품 데이터 수집](projects/shopping/README.md) | 동적으로 로딩되는 상품 데이터를 표 형태로 정리하기 | Selenium, BeautifulSoup, pandas | 동적 웹 수집, 데이터 정제, 표 구조화 |
| [생일 축하 미니게임](projects/birthday-game/README.md) | 선택형 콘텐츠를 웹 인터랙션으로 구현하기 | HTML, CSS, JavaScript, 생성형 AI | UI 구현, 상태 분기, 반응형 화면 |

## AI 활용 범위

생성형 AI를 코드 초안, 디버깅 및 라이브러리 사용법 확인에 활용했습니다. 직접 요구사항을 정의하고 코드를 실행·수정하며 데이터 추출 결과와 화면 동작을 검증했습니다.

## 빠르게 확인하기

- Python: `python -m pip install -r requirements.txt` 후 `python scripts/offline_demo.py`
- 검증: `python -m unittest discover -s tests -v`
- 게임: `projects/birthday-game/index.html`을 브라우저에서 열기

검증 결과와 범위는 [검증 기록](docs/verification.md), 설명 내용은 [설명 가이드](docs/interview-notes.md)에 정리했습니다.

Python 데모는 저장된 **합성 HTML 예시**만 읽습니다. 실제 사이트 수집 성능이나 현재 접속 성공을 입증하는 테스트가 아닙니다. 원본 쇼핑 데이터의 행 수·필드 구성은 [결과 요약](projects/shopping/result-summary.json)으로 별도 제시합니다.

## 코드에서 볼 수 있는 역량

1. 검색 요청 파라미터를 딕셔너리로 구성하고 목록·상세페이지를 연결하는 방식
2. 항목 순서에 의존하는 추출과 항목명 기반 추출의 차이, 누락 항목 처리
3. 동적 페이지의 스크롤 수집과 가격·공백 정리, 표 구조로의 변환
4. 화면 너비에 따른 CSS 레이아웃과 선택 상태에 따른 JavaScript 분기

크롤링 프로젝트는 수집·전처리 역량의 근거입니다. 통계적 분석·해석은 연결된 반도체 공정 분석 저장소에서 다룹니다.

## 구성

```text
projects/riss/           요청·파싱 코드와 합성 HTML 예시
projects/shopping/       수집 코드, 합성 예시, 원본 결과의 집계
projects/birthday-game/  개인정보를 일반 이야기로 바꾼 게임
scripts/                오프라인 실행 예시
tests/                  파싱 결과와 예외 처리 검증
docs/                   정리 범위와 면접 설명 가이드
```

원본 강의 노트북 전체, 로그인·메일 자동화 코드, 계정 정보, 개인 사진·음원은 포함하지 않았습니다. 실제 웹 수집은 대상 서비스의 이용 조건과 접근 범위를 확인한 뒤 사용해야 하며, 화면 구조가 바뀌면 선택자 수정이 필요합니다.
