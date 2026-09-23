# Data & AI Projects

### Materials × Data × AI

**신소재공학을 기반으로 반도체 공정 데이터를 분석하고, 새로운 기술 흐름에 맞춰 AI 자동화 도구와 웹서비스를 직접 구현·검증하며 AX 역량을 쌓아온 엔지니어**

Python으로 데이터 수집과 반복 작업을 자동화했습니다.

웹서비스 개발에서는 화면·서버 API·데이터베이스·테스트 결제를 연결했습니다.
각 프로젝트에서 직접 정한 요구사항과 설계 판단, 실행 결과와 검증 근거를 함께 정리했습니다.

📄 **[Portfolio PDF ↗](./Jiwon_Yoo_Portfolio.pdf)**

---

## 결과 요약


| 프로젝트 | 구현·분석 결과 | 기술적 판단 | 바로 보기 |
|---|---|---|---|
| **반도체 공정 데이터 분석** | 공정 실행 **25건**, wafer **49개 위치** 분석, 후속 **9개 Split** 설계 | 조건 번호 기반 연결, 결측 보존, 유효 측정 수를 고려한 후보 선정 | [코드·분석](https://github.com/GREENMAMOS/semiconductor-process-data-analysis) |
| **SHYSTAR · 사이별** | 관계지도·공유·D1 저장·테스트 결제 구현, **2,048개 보고서 조합** 검사 | 서버 금액 검증, 구매자 권한 분리, 중복 승인 방지 | [서비스](https://shystar.greenmamos.workers.dev/) · [코드](https://github.com/GREENMAMOS/SHYSTAR) · [분석 샘플](https://shystar.greenmamos.workers.dev/analysis-sample) |
| **카카오톡 음악 동기화** | 음악 링크 추출·중복 제거·신규 곡 반영 자동화, 기존 실행에서 **77건 추출** 확인 | 메시지 형식에 독립적인 URL 추출, 상태 파일 기반 이력 비교, 부분 실패 분리 | [코드·실행 방법](https://github.com/GREENMAMOS/kakao-to-ytmusic) |

25건은 공정 실행 기록 수이며 서로 다른 Recipe 수가 아닙니다. 2,048개는 보고서 입력 조합 수입니다. 77건은 기존 실행 기록이며 시간 단축과 실제 추가 성공률은 별도로 측정하지 않았습니다.


[검증 기록](docs/verification.md)

## Featured Project

### 🔬 [Semiconductor Process Data Analysis](https://github.com/GREENMAMOS/semiconductor-process-data-analysis)

반도체 증착 공정 데이터를 전처리하고, **센서 안정성·공정조건별 박막 두께·wafer 위치별 분포**를 분석한 프로젝트입니다.

단순 시각화보다 조건별 통계량과 산포를 비교하며  
**데이터를 근거로 공정 상태를 해석하고 개선 후보를 좁히는 과정**에 초점을 두었습니다.

#### 주요 분석

- Si2H6 센서 데이터의 ramp-up 구간과 안정 구간 분리
- Run별 평균·표준편차를 이용한 안정 구간 비교
- Pre 반복 기록을 포함한 25개 공정 실행 기록의 박막 두께·Range·STD·Uniformity 분석
- Si2H6 유량, RF Power, 온도, 시간에 따른 결과 변화 비교
- 공정 Recipe와 wafer 계측 데이터를 조건별로 연결
- 49-point wafer map 기반 위치별 평균 절대편차 분석
- 목표 두께와 균일도를 고려한 후보 조건 비교
- 변경 Target에 대한 9개 Split 후속 평가안 설계
- 분석 결과와 함께 실험 검증이 필요한 범위를 명시

#### 결과와 판단 근거

- 반복되는 WF 번호 대신 조건 번호로 공정 Recipe와 계측 데이터를 연결했습니다.
- 두께 결측 9개를 0으로 대체하지 않고, 유효 측정값과 측정 개수를 기준으로 분석했습니다.
- 초기 규격 후보로 선정한 Run23은 유효 측정 45/49개 위치 기준이며, 결측 위치의 재계측이 필요합니다.
- 9개 Split 후속 평가안을 설계했습니다. 제안 조건의 예상 두께는 가정에 따른 계산값입니다.

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
| 🎵 [카카오톡 음악 링크 자동화](https://github.com/GREENMAMOS/kakao-to-ytmusic) | 대화 파일의 음악 링크를 수집해 YouTube Music에 반영 | Python, ytmusicapi, 정규표현식 | URL 파싱, 이력 관리, API 연동, 예외 처리 |
| 🎮 [ShieldDive](projects/shielddive/README.md) | 5인 팀 액션게임 제작 및 작업관리 자동화 | Unity, C#, ChatGPT, Apps Script | 프로젝트 기획, 협업, UI·사운드 구현, 업무 자동화 |
| 📚 [RISS 논문 정보 수집](projects/riss/README.md) | 목록·상세페이지 정보를 수집해 데이터셋 구축 | Python, requests, BeautifulSoup | 데이터 수집·파싱, 누락값 처리 |
| 🛒 [쇼핑몰 상품 데이터 수집](projects/shopping/README.md) | 동적 웹페이지 상품 데이터를 구조화 | Python, Selenium, BeautifulSoup, pandas | 브라우저 자동화, 데이터 정제·구조화 |
| 🎂 [개인화 생일 게임](projects/birthday-game/README.md) | 선택에 따라 결과가 달라지는 웹 인터랙션 구현 | HTML, CSS, JavaScript, 생성형 AI | AI 보조 개발, UI 구현, 상태 분기 |

---

## ⭐ 사이별 MBTI · SHYSTAR

🔗 [공개 서비스](https://shystar.greenmamos.workers.dev/) · [분석 샘플](https://shystar.greenmamos.workers.dev/analysis-sample) · [코드](https://github.com/GREENMAMOS/SHYSTAR)

MBTI 관계지도 생성·공유부터 관계별 분석 콘텐츠, D1 데이터 저장, 토스페이먼츠 테스트 결제까지 연결한 개인 풀스택 웹서비스입니다. 서버의 주문·금액·상태 검증, 구매자 접근 권한 분리, 중복 승인 방지를 구현하고 2,048개 보고서 구성을 검사하는 자동화 테스트를 작성했습니다. 생성형 AI는 코드 초안·디버깅에 활용했고, 기능·흐름·검증 시나리오는 직접 설계했습니다.

구현 내용, 설계 판단, 검증 범위와 한계는 [프로젝트 README](https://github.com/GREENMAMOS/SHYSTAR)에서 자세히 볼 수 있습니다.

---

## 🎵 카카오톡 음악 링크 → YouTube Music 자동화

🔗 [코드와 실행 방법](https://github.com/GREENMAMOS/kakao-to-ytmusic)

카카오톡 대화 내보내기 파일에서 음악 링크를 추출해 YouTube Music 플레이리스트에 반영하는 Python CLI 도구입니다. 메시지 형식에 의존하지 않는 URL 추출과 상태 파일 기반 이력 비교로 신규 곡만 반영하도록 구현했으며, 기존 실행 기록에서 영상 링크 77건 추출을 확인했습니다.

설계 판단과 검증 범위는 [프로젝트 README](https://github.com/GREENMAMOS/kakao-to-ytmusic)에서 자세히 볼 수 있습니다.

---

## 🎮 ShieldDive

🔗 [Play Game ↗](https://coleyoung-game.github.io/Web_ShieldDive/) · [Project Details](projects/shielddive/README.md)

5인 팀 픽셀 액션게임에 기획팀장 겸 보조개발로 참여해 게임 규칙·플레이 흐름 기획, 일정 관리, 메인 화면·사운드 구현을 담당했습니다. 팀의 작업 등록·진행 확인·마감 공유 흐름은 GPT로 요청을 구조화해 Google Apps Script·Sheets·Discord Webhook과 연결하는 방식으로 자동화했습니다. 핵심 플레이 로직은 다른 팀원이 담당했습니다.

담당 역할과 자동화 구조는 [프로젝트 상세](projects/shielddive/README.md)에서 자세히 볼 수 있습니다.

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
🔗 [Live Demo ↗](https://iridescent-croquembouche-2e6aa8.netlify.app/)

선택 상태에 따라 세 가지 엔딩으로 이어지는 HTML·CSS·JavaScript를 사용한 미니게임입니다.

- 선택값 저장과 엔딩 분기
- 다시 시작할 때 상태 초기화
- PC·모바일 화면에 맞춘 반응형 배치
- 엔딩 결과 복사 기능

이야기와 기능 요구사항을 직접 정하고, AI가 제안한 UI·코드 초안을 수정하며 완성했습니다.
공개본은 개인 이름·사진·대화를 일반 이야기로 대체했습니다.

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
