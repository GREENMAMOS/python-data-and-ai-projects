# Data & AI Projects

### Materials × Data × AI

**공정과 소자를 이해하고, 데이터를 해석하며, AI로 문제 해결의 범위를 넓혀가는 엔지니어**

신소재공학을 기반으로 반도체 공정·소자를 이해하고,
Python을 활용해 데이터를 수집·전처리·분석하는 프로젝트를 수행했습니다.

또한 생성형 AI와 자동화 도구를 적극적으로 활용해
아이디어를 실제 서비스와 업무 흐름으로 구현하며 새로운 기술을 빠르게 학습하고 적용하고 있습니다.

📄 **[Portfolio PDF ↗](./Jiwon_Yoo_Portfolio.pdf)**

---

## Featured Project

### 🔬 [Semiconductor Process Data Analysis](https://github.com/GREENMAMOS/semiconductor-process-data-analysis)

반도체 증착 공정 데이터를 전처리하고, **센서 안정성·공정조건별 박막 두께·wafer 위치별 분포**를 분석한 프로젝트입니다.

단순 시각화보다 조건별 통계량과 산포를 비교하며  
**데이터를 근거로 공정 상태를 해석하고 개선 후보를 좁히는 과정**에 초점을 두었습니다.

#### 주요 분석

- Si2H6 센서 데이터의 ramp-up 구간과 안정 구간 분리
- Run별 평균·표준편차를 이용한 안정 구간 비교
- 25개 공정 조건의 박막 두께·Range·STD·Uniformity 분석
- Si2H6 유량, RF Power, 온도, 시간에 따른 결과 변화 비교
- 공정 Recipe와 wafer 계측 데이터를 조건별로 연결
- 49-point wafer map 기반 위치별 평균 절대편차 분석
- 목표 두께와 균일도를 고려한 후보 조건 비교
- 변경 Target에 대한 9개 Split 후속 평가안 설계
- 분석 결과와 함께 실험 검증이 필요한 범위를 명시

#### Tech

`Python` `pandas` `NumPy` `Matplotlib` `openpyxl` `Jupyter Notebook` `Excel`

> **Main Focus**  
> 공정 데이터를 전처리하고 변수별 차이와 산포를 분석하여  
> 데이터 기반으로 공정 상태를 이해하고 문제 해결 방향을 좁히는 역량을 보여주는 프로젝트입니다.

---

## Supporting Projects

반도체·제조 데이터 분석을 중심으로,
**Python 데이터 처리 → AI 활용 → 서비스 구현·자동화**까지 경험의 범위를 확장하고 있습니다.

| 프로젝트 | 목적 | 주요 기술 | 보여주는 역량 |
|---|---|---|---|
| 🔬 [Semiconductor Process Data Analysis](https://github.com/GREENMAMOS/semiconductor-process-data-analysis) | 증착 공정 조건·계측 데이터 분석 및 후속 평가 설계 | Python, pandas, Matplotlib, Excel | 제조 데이터 분석, 공정 해석, 실험 조건 설계 |
| ⭐ [사이별 · SHYSTAR ↗](https://github.com/GREENMAMOS/SHYSTAR) | 관계 데이터를 시각화하는 웹서비스 구현·배포 | React, TypeScript, Workers, D1 | 서비스 기획, API·DB 연동, AI 보조 개발, 배포 |
| 🎮 [ShieldDive](projects/shielddive/README.md) | 5인 팀 액션게임 제작 및 작업관리 자동화 | Unity, C#, ChatGPT, Apps Script | 프로젝트 기획, 협업, UI·사운드 구현, 업무 자동화 |
| 📚 [RISS 논문 정보 수집](projects/riss/README.md) | 목록·상세페이지 정보를 수집해 데이터셋 구축 | Python, requests, BeautifulSoup | 데이터 수집·파싱, 누락값 처리 |
| 🛒 [쇼핑몰 상품 데이터 수집](projects/shopping/README.md) | 동적 웹페이지 상품 데이터를 구조화 | Python, Selenium, BeautifulSoup, pandas | 브라우저 자동화, 데이터 정제·구조화 |
| 🎂 [개인화 생일 게임](projects/birthday-game/README.md) | 선택에 따라 결과가 달라지는 웹 인터랙션 구현 | HTML, CSS, JavaScript, 생성형 AI | AI 보조 개발, UI 구현, 상태 분기 |

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

## 🎮 ShieldDive

🔗 **[Play Game ↗](https://coleyoung-game.github.io/Web_ShieldDive/)**  
📁 **[Project Details](projects/shielddive/README.md)**

5인 팀으로 제작한 픽셀 액션게임 프로젝트입니다.

방패를 이용해 장애물을 공격·회피하며
목표 지점까지 내려가는 게임을 기획하고 제작했습니다.

### 담당 역할

- 5인 팀 기획팀장 및 보조개발
- 게임 규칙과 전체 플레이 흐름 기획
- 제작 일정 및 팀 진행 상황 관리
- 메인 화면 구현
- 게임 사운드 구현
- 팀 작업 등록·상태 확인·마감 공유 자동화 구성

핵심 플레이 로직과 일부 플레이 화면은 다른 팀원이 담당했으며,
저는 **기획·일정 관리와 메인 화면·사운드 개발**을 중심으로 참여했습니다.

### Team Workflow Automation

프로젝트 진행 중 반복되는
**작업 등록 → 진행 상태 확인 → 마감 안내** 흐름을 자동화 대상으로 정했습니다.

```text
자연어 작업 요청
        ↓
GPT로 작업 정보 구조화
        ↓
Google Apps Script
        ↓
Google Sheets 기록
        ↓
Discord Webhook 알림
```

---

## Python Data Collection

### 📚 RISS 논문 정보 수집
📁 [Project Details](projects/riss/README.md)

검색 결과 목록과 논문 상세페이지의 정보를 연결해  
필요한 데이터를 하나의 구조로 정리했습니다.

- HTTP 요청 파라미터 구성
- 검색 결과와 상세페이지 연결
- BeautifulSoup 기반 HTML 파싱
- 항목명을 기준으로 데이터 추출
- 누락 항목 예외 처리

### 🛒 쇼핑몰 상품 데이터 수집
📁 [Project Details](projects/shopping/README.md)

스크롤을 내려야 추가 상품이 로딩되는 동적 웹페이지에서  
상품 정보를 자동 수집하고 표 형태로 정리했습니다.

- Selenium 기반 브라우저 자동화
- 동적 페이지 스크롤 처리
- BeautifulSoup 기반 요소 추출
- 가격·공백 데이터 정제
- pandas DataFrame 구조화

---

## Personalized Birthday Game (AI-assisted Development)
📁 [Project Details](projects/birthday-game/README.md)
🔗 Live Demo ↗

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

### Semiconductor & Manufacturing

- 반도체 공정·소자 기초
- 공정 Recipe와 계측 데이터 연결
- 공정조건별 통계량 비교
- 평균·표준편차·Range·산포 분석
- wafer 위치 기반 데이터 분석
- 공정 결과를 기반으로 한 후속 평가 조건 검토

### Python & Data

`Python` `pandas` `NumPy` `Matplotlib` `BeautifulSoup` `Selenium` `requests` `openpyxl` `Jupyter Notebook`

- 데이터 수집
- 데이터 전처리·구조화
- 통계량 계산
- 시각화
- Excel 저장 및 자동화

### Web & Service Development

`HTML` `CSS` `JavaScript` `TypeScript` `React` `REST API` `Cloudflare Workers` `Cloudflare D1`

- 웹 UI 구현
- API·DB 연동
- 서비스 배포
- 반응형 화면 구현

### AI & Automation

- 생성형 AI 기반 코드 초안 작성
- 오류 원인 탐색 및 디버깅
- 새로운 기술·라이브러리 학습
- 코드 리뷰 및 개선
- 아이디어의 프로토타입 구현
- Google Apps Script 기반 업무 자동화
- Google Sheets · Discord Webhook 연동

---

## How I Work

```text
공정·소자에 대한 이해
        +
데이터 수집·전처리·분석
        +
AI·자동화를 활용한 빠른 구현
        ↓
새로운 기술을 빠르게 학습하고 적용하며,
결과를 검증하고 개선해
실제 문제해결로 연결하는 엔지니어
```
