# Data & AI Projects

반도체·제조 데이터 분석을 중심으로, **Python 기반 데이터 수집·전처리와 생성형 AI를 활용한 서비스 구현 경험**을 정리한 개인 프로젝트 포트폴리오입니다.

공정 데이터를 정리하고 통계·시각화를 통해 의미를 해석하는 것을 핵심 역량으로 두고 있으며,  
데이터 수집과 웹서비스 개발 프로젝트를 통해 **데이터 처리부터 실제 서비스 구현·배포까지** 경험했습니다.

---

## Featured Project

### 🔬 [Semiconductor Process Data Analysis](https://github.com/GREENMAMOS/semiconductor-process-data-analysis)

반도체 증착 공정 데이터를 전처리하고, **센서 안정성·공정조건별 박막 두께·wafer 위치별 분포**를 분석한 프로젝트입니다.

단순 시각화보다 조건별 통계량과 산포를 비교하며  
**데이터를 근거로 공정 상태를 해석하고 개선 후보를 좁히는 과정**에 초점을 두었습니다.

#### 주요 분석

- 세 번의 Run에서 Si2H6 유량 안정성 비교
- 초기 ramp-up 구간과 안정 구간 분리
- 안정 구간 평균·표준편차 비교
- 총 25개 공정조건의 박막 두께 통계량 분석
- Si2H6 유량, RF power, 온도, 시간에 따른 두께 변화 비교
- 특정 조건군에서 Si2H6 유량과 평균 두께의 상관관계 확인 (`r = 0.904`)
- 대표 wafer의 49개 측정 위치 기반 thickness map 시각화
- 평균·산포만으로 최적 조건을 단정하지 않고 분석 한계 명시

#### Tech

`Python` `pandas` `NumPy` `Matplotlib` `openpyxl` `Jupyter Notebook` `Excel`

> **Main Focus**  
> 공정 데이터를 전처리하고 변수별 차이와 산포를 분석하여  
> 데이터 기반으로 공정 상태를 이해하고 문제 해결 방향을 좁히는 역량을 보여주는 프로젝트입니다.

---

## Supporting Projects

메인 프로젝트의 **제조 데이터 분석 역량**을 중심으로,  
Python 데이터 수집·서비스 구현·생성형 AI 활용 경험을 보조 프로젝트로 확장했습니다.

| 프로젝트 | 목적 | 주요 기술 | 보여주는 역량 |
|---|---|---|---|
| ⭐ [사이별 MBTI (SHYSTAR)](https://shystar.greenmamos.workers.dev) | 친구들의 MBTI 관계를 별자리처럼 시각화하고 궁합을 제공하는 웹서비스 구현 | TypeScript, React, Cloudflare Workers, D1 | 서비스 기획, API·DB 연동, 풀스택 구현, 배포 |
| 📚 [RISS 논문 정보 수집](projects/riss/README.md) | 검색 결과와 상세페이지의 정보를 함께 수집·정리 | Python, requests, BeautifulSoup | 요청 파라미터 구성, 데이터 수집·파싱, 누락값 처리 |
| 🛒 [쇼핑몰 상품 데이터 수집](projects/shopping/README.md) | 동적으로 로딩되는 상품 데이터를 표 형태로 정리 | Python, Selenium, BeautifulSoup, pandas | 동적 웹 수집, 데이터 정제, 구조화 |
| 🎂 [생일 축하 미니게임](projects/birthday-game/README.md) | 선택에 따라 결과가 달라지는 웹 인터랙션 구현 | HTML, CSS, JavaScript, 생성형 AI | UI 구현, 상태 분기, 반응형 화면 |

---

## ⭐ 사이별 MBTI · SHYSTAR

친구들의 MBTI 관계를 별자리처럼 시각화하고,  
친구별 관계와 궁합 점수를 확인할 수 있도록 만든 웹서비스입니다.

🔗 **Live Service**  
https://shystar.greenmamos.workers.dev

🔗 **Repository**  
https://github.com/GREENMAMOS/SHYSTAR

### 구현 내용

- 별명·MBTI 기반 관계 지도 생성
- 친구 추가 및 관계 데이터 저장
- MBTI 기반 케미 점수 계산 및 순위 표시
- 관계 데이터를 별자리 형태로 시각화
- 공유 가능한 관계 지도 URL 제공
- Cloudflare D1 기반 데이터 저장
- Cloudflare Workers 환경에 실제 서비스 배포
- 모바일·데스크톱 반응형 UI 구현

### AI 활용

서비스의 기능과 사용자 흐름은 직접 설계한 뒤,  
생성형 AI를 **코드 초안 작성·구현 방법 탐색·디버깅·코드 리뷰**에 활용했습니다.
AI가 생성한 결과를 실행하고 오류를 확인하면서 필요/요구사항에 맞게 수정·검증했습니다.

---

## Python Data Collection

### 📚 RISS 논문 정보 수집

검색 결과 목록과 논문 상세페이지의 정보를 연결해  
필요한 데이터를 하나의 구조로 정리했습니다.

- HTTP 요청 파라미터 구성
- 검색 결과와 상세페이지 연결
- BeautifulSoup 기반 HTML 파싱
- 항목명을 기준으로 데이터 추출
- 누락 항목 예외 처리

### 🛒 쇼핑몰 상품 데이터 수집

스크롤을 내려야 추가 상품이 로딩되는 동적 웹페이지에서  
상품 정보를 자동 수집하고 표 형태로 정리했습니다.

- Selenium 기반 브라우저 자동화
- 동적 페이지 스크롤 처리
- BeautifulSoup 기반 요소 추출
- 가격·공백 데이터 정제
- pandas DataFrame 구조화

---

## AI-assisted Development

생성형 AI를 결과 생성 도구가 아니라  
**개발과 학습 과정의 보조 도구**로 활용했습니다.

- 코드 초안 작성
- 오류 원인 탐색 및 디버깅
- 새로운 라이브러리·API 사용법 학습
- 코드 구조 개선 아이디어 탐색
- 웹 UI 구현 보조
- 구현 결과 리뷰 및 수정

프로젝트의 목적과 기능 요구사항은 직접 정하고,  
AI가 제안한 코드는 실제 실행과 검증을 거쳐 필요한 부분을 수정했습니다.

---

## Core Skills

### Semiconductor & Manufacturing Data Analysis

- 공정 데이터 전처리
- 공정조건별 통계량 비교
- 평균·표준편차·산포 분석
- 변수 간 관계 탐색
- wafer 위치 기반 데이터 시각화
- 분석 결과의 한계와 해석 범위 구분

### Python & Data

`Python` `pandas` `NumPy` `Matplotlib` `BeautifulSoup` `Selenium` `requests` `openpyxl` `Jupyter Notebook`

### Web & Service Development

`HTML` `CSS` `JavaScript` `TypeScript` `React` `REST API` `Cloudflare Workers` `Cloudflare D1`

### AI-assisted Workflow

- 생성형 AI 기반 코드 초안 작성
- 디버깅 및 오류 원인 탐색
- 라이브러리·프레임워크 학습
- 코드 리뷰 및 개선
- 아이디어의 프로토타입 구현

---

## How the Projects Connect

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
생성형 AI를 활용한 개발 보조
      ↓
실제 서비스 구현 및 배포
