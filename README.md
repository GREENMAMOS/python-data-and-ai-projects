# Data & AI Projects

반도체·제조 데이터 분석을 중심으로, **Python 데이터 수집·전처리와 생성형 AI를 활용한 실제 서비스 구현 경험**을 정리한 개인 프로젝트 포트폴리오입니다.

공정 데이터를 전처리하고 통계·시각화를 통해 의미를 해석하는 것을 핵심 역량으로 두고 있으며,  
Python 기반 데이터 수집과 웹서비스 개발 프로젝트를 통해 **데이터를 수집하고 분석하는 과정부터 실제로 작동하는 결과물로 구현하는 과정**까지 경험했습니다.

---

## Featured Project

### 🔬 [반도체 공정 데이터 분석](https://github.com/GREENMAMOS/semiconductor-process-data-analysis)

반도체 증착 공정 데이터를 전처리하고, **센서 안정성·공정조건별 박막 두께·wafer 위치별 분포**를 분석한 프로젝트입니다.

공정 데이터를 단순 시각화하는 데 그치지 않고, 조건별 통계량과 산포를 비교하며  
**데이터를 근거로 공정 상태를 해석하고 개선 후보를 좁히는 과정**에 초점을 두었습니다.

**주요 내용**

- 공정 센서 Run별 안정 구간 비교
- 평균·표준편차를 활용한 센서 안정성 분석
- Si2H6 유량, RF Power, 온도, 시간에 따른 박막 두께 비교
- 공정조건별 평균·최솟값·최댓값·범위·표준편차 분석
- 공정 변수와 박막 두께 간 상관관계 확인
- 49개 측정 위치 기반 wafer thickness map 시각화
- Jupyter Notebook 기반 분석 과정 재현

**Tech**

`Python` `pandas` `NumPy` `Matplotlib` `openpyxl` `Jupyter Notebook` `Excel`

> **Main Focus**  
> 반도체·제조 데이터를 전처리하고 변수별 차이와 산포를 분석하여,  
> 데이터 기반으로 공정 상태를 이해하고 문제 해결 방향을 좁히는 역량을 보여주는 프로젝트입니다.

---

## Supporting Projects

메인 프로젝트에서 보여주는 **제조 데이터 분석 역량**을 중심으로,  
데이터 수집·서비스 구현·생성형 AI 활용 경험을 보조 프로젝트로 확장했습니다.

| 프로젝트 | 프로젝트 목적 | 주요 기술 | 보여주는 역량 |
|---|---|---|---|
| ⭐ [사이별 MBTI (SHYSTAR)](https://shystar.greenmamos.workers.dev) | 친구들의 MBTI 관계를 별자리 형태로 시각화하고 관계 궁합을 제공하는 웹서비스 구현 | TypeScript, React, Cloudflare Workers, D1, 생성형 AI | 서비스 기획, API·DB 연동, 풀스택 구현, 배포 |
| 📚 [RISS 논문 정보 수집](projects/riss/README.md) | 검색 목록과 상세페이지의 정보를 함께 수집·비교하기 | Python, requests, BeautifulSoup | 요청 파라미터 구성, 웹 데이터 수집, 파싱, 누락값 처리 |
| 🛒 [쇼핑몰 상품 데이터 수집](projects/shopping/README.md) | 스크롤로 추가되는 상품 데이터를 표 형태로 정리하기 | Python, Selenium, BeautifulSoup, pandas | 동적 웹 수집, 데이터 정제, 구조화 |
| 🎂 [생일 축하 미니게임](projects/birthday-game/README.md) | 선택에 따라 결과가 달라지는 웹 인터랙션 구현 | HTML, CSS, JavaScript, 생성형 AI | UI 구현, 상태 분기, 반응형 화면 |

---

## ⭐ 사이별 MBTI · SHYSTAR

**SHYSTAR(사이별 MBTI)**는 친구들의 MBTI 관계를 별자리처럼 시각화하고,  
친구별 관계와 궁합 점수를 확인할 수 있도록 만든 개인 웹서비스입니다.

🔗 **Live Service:**  
https://shystar.greenmamos.workers.dev

🔗 **Repository:**  
https://github.com/GREENMAMOS/SHYSTAR

### 구현 내용

- 사용자 별명·MBTI 기반 관계 지도 생성
- 친구 추가 및 관계 데이터 저장
- MBTI 기반 케미 점수 계산 및 순위 표시
- 관계 데이터를 별자리 형태로 시각화
- 공유 가능한 관계 지도 URL 제공
- Cloudflare D1 기반 데이터 저장
- Cloudflare Workers 환경에 실제 서비스 배포
- 모바일·데스크톱 반응형 UI 구현

### AI 활용

서비스의 기능과 사용자 흐름을 직접 정하고,  
생성형 AI를 **코드 초안 작성, 구현 방법 탐색, 디버깅, 코드 리뷰**에 활용했습니다.

AI가 생성한 결과를 그대로 사용하는 것이 아니라 직접 실행하고 오류를 확인하면서  
기능 요구사항에 맞게 수정하고 반복적으로 검증했습니다.

> SHYSTAR는 단순 코드 예제가 아니라  
> **기획 → 구현 → 데이터베이스 연동 → 디버깅 → 실제 배포**까지 경험한 서비스 프로젝트입니다.

---

## Python Data Collection

### 📚 RISS 논문 정보 수집

검색 결과 목록과 각 논문의 상세페이지에서 필요한 정보를 수집하고  
하나의 데이터 구조로 정리하는 과정을 구현했습니다.

**주요 경험**

- HTTP 요청 파라미터 구성
- 검색 결과와 상세페이지 연결
- BeautifulSoup 기반 HTML 파싱
- 항목명을 기준으로 필요한 정보 추출
- 누락 데이터 예외 처리
- 수집 결과를 재사용 가능한 구조로 정리

---

### 🛒 쇼핑몰 상품 데이터 수집

스크롤을 내려야 추가 상품이 로딩되는 동적 웹페이지를 대상으로  
상품 정보를 자동 수집하고 표 형태로 정리했습니다.

**주요 경험**

- Selenium 기반 브라우저 자동화
- 동적 페이지 스크롤 처리
- BeautifulSoup 기반 요소 추출
- 가격 문자열 및 공백 정제
- pandas DataFrame 구조화
- Excel 형태의 결과 데이터 생성

---

## AI-assisted Development

생성형 AI를 단순 결과 생성 도구가 아니라  
**개발과 학습 과정의 보조 도구**로 활용했습니다.

주로 다음 과정에 활용했습니다.

- 코드 초안 작성
- 오류 원인 탐색 및 디버깅
- 새로운 라이브러리와 API 사용법 학습
- 코드 구조 개선 아이디어 탐색
- 웹 UI 구현 보조
- 구현 결과 리뷰 및 수정

프로젝트의 목적과 기능 요구사항을 직접 정하고,  
AI가 제안한 코드를 실제로 실행·검증하면서 필요한 부분을 수정하는 방식으로 작업했습니다.

이를 통해 새로운 기술을 빠르게 학습하고  
아이디어를 **실행 가능한 데이터 분석 코드와 웹서비스로 구현하는 경험**을 쌓았습니다.

---

## Core Skills

### Semiconductor & Manufacturing Data Analysis

- 공정 데이터 전처리 및 정리
- 공정조건별 통계량 비교
- 평균·표준편차·산포 분석
- 변수 간 관계 탐색
- wafer 위치 기반 데이터 시각화
- 분석 결과의 한계와 해석 범위 구분

### Python & Data

- Python
- pandas
- NumPy
- Matplotlib
- BeautifulSoup
- Selenium
- requests
- Excel / openpyxl
- Jupyter Notebook

### Web & Service Development

- HTML / CSS / JavaScript
- TypeScript
- React
- REST API
- Cloudflare Workers
- Cloudflare D1
- 서비스 배포 및 운영

### AI-assisted Workflow

- 생성형 AI 기반 코드 초안 작성
- 디버깅 및 오류 원인 탐색
- 라이브러리·프레임워크 학습
- 코드 리뷰 및 개선
- 아이디어의 프로토타입 구현

---

## How the Projects Connect

각 프로젝트를 서로 독립적인 경험으로 나열하기보다,  
다음과 같은 하나의 흐름으로 발전시키고 있습니다.

```text
웹·데이터 소스
      ↓
Python 데이터 수집
      ↓
전처리 및 구조화
      ↓
데이터 분석·시각화
      ↓
반도체·제조 데이터 해석
      ↓
AI를 활용한 개발·자동화
      ↓
실제 서비스 구현 및 배포
