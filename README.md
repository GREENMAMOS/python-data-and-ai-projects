# Python Data Collection & AI-assisted Projects

필요한 정보를 수집·정리하고, 생성형 AI를 활용해 아이디어를 작동하는 도구로 구현한 개인 프로젝트 모음입니다. Python 데이터 수집과 HTML·CSS·JavaScript 기반 화면 구현을 구분해 소개합니다.

## 프로젝트

| 프로젝트 | 해결하려던 문제 | 주요 기술 | 결과와 근거 |
|---|---|---|---|
| [RISS 논문 정보 수집](projects/riss/README.md) | 검색 목록과 상세페이지의 정보를 함께 비교하기 | Python, requests, BeautifulSoup | 요청 파라미터 구성, 항목명 기반 추출, 누락 주제어 처리 |
| [쇼핑몰 상품 데이터 수집](projects/shopping/README.md) | 스크롤로 추가되는 상품을 표 형태로 정리하기 | Selenium, BeautifulSoup, pandas | 원본 엑셀 120행·5개 항목, 가격 문자열 정리 |
| [생일 축하 미니게임](projects/birthday-game/README.md) | 축하 메시지를 선택형 콘텐츠로 전달하기 | HTML, CSS, JavaScript, 생성형 AI | 선택 상태, 3개 엔딩, 반응형 화면, 다시 시작 |
| [반도체 공정 데이터 분석](https://github.com/GREENMAMOS/semiconductor-process-data-analysis) | 공정 조건과 계측 결과를 비교하기 | Python, Excel, 통계·시각화 | 별도 저장소에서 공정 데이터 해석 역량 소개 |

## 내가 한 일과 AI의 역할

개인 작업으로 필요한 기능과 방향을 정하고, 코드를 실행하며 결과를 확인했습니다. 생성형 AI는 코드 생성·리뷰, 라이브러리 사용법 학습, HTML 구조 이해와 오류 원인 탐색에 활용했습니다. 크롤링은 교육 실습을 바탕으로 수행했으며, 독자적인 크롤링 프레임워크 개발을 주장하지 않습니다. 게임의 디자인·코드 초안에도 AI의 도움을 받았고, 직접 문구와 배치 등을 수정했습니다.

공개용 파일 정리에는 AI 코딩 도구를 추가 활용했습니다. 오프라인 예시, 함수 분리, 검증 코드와 개인정보 제거는 **이번 포트폴리오 정리 단계에서 추가**한 내용이며, 최초 프로젝트에서 수행한 내용과 각 설명에서 구분했습니다. 원본 저장 파일만으로 확인되지 않는 개발 기간·처리시간 절감률·모델 정확도는 기재하지 않았습니다.

## 빠르게 확인하기

- Python: `python -m pip install -r requirements.txt` 후 `python scripts/offline_demo.py`
- 검증: `python -m unittest discover -s tests -v`
- 게임: `projects/birthday-game/index.html`을 브라우저에서 열기

검증 결과와 범위는 [검증 기록](docs/verification.md), 면접에서 설명할 내용은 [설명 가이드](docs/interview-notes.md)에 정리했습니다.

Python 데모는 저장된 **합성 HTML 예시**만 읽습니다. 실제 사이트 수집 성능이나 현재 접속 성공을 입증하는 테스트가 아닙니다. 원본 쇼핑 데이터의 행 수·필드 구성은 [결과 요약](projects/shopping/result-summary.json)으로 별도 제시합니다.

## 코드에서 볼 수 있는 역량

1. 검색 요청 파라미터를 딕셔너리로 구성하고 목록·상세페이지를 연결하는 방식
2. 항목 순서에 의존하는 추출과 항목명 기반 추출의 차이, 누락 항목 처리
3. 동적 페이지의 스크롤 수집과 가격·공백 정리, 표 구조로의 변환
4. 화면 너비에 따른 CSS 레이아웃과 선택 상태에 따른 JavaScript 분기

크롤링 프로젝트는 수집·전처리 역량의 근거입니다. 통계적 분석·해석은 연결된 반도체 공정 분석 저장소에서 다룹니다. ML 예측 모델이나 AI Agent를 구현한 프로젝트는 아닙니다.

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
