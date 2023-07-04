## ✨ Leaffit

> Generate Wendler Exercise Sheets based on your One Rep Max weights  
> 
> Visit the live site here https://kyeongsupchoi.pythonanywhere.com/wendler.html
> 
> Wendler Program explanation at https://www.t-nation.com/workouts/5-3-1-how-to-build-pure-strength/

## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- mysite/                               # Main app directory
   |    |
   |    |-- home/                            # Holds the html template files
   |    |    |-- wendler.html                # Wendler html file with Django tags and Bootstrap          
   |    |
   |    |-- asgi.py                          # ASGI config for mysite project.
   |    |-- forms.py                         # Define Wendler forms
   |    |-- models.py                        # Define Wendler models
   |    |-- settings.py                      # Define Global Settings
   |    |-- urls.py                          # Define URLs served by all apps/nodes 
   |    |-- views.py                         # Handles Wendler input and calculations
   |    |-- wsgi.py                          # Deploys app in production
   |    |
   |    |-- venv/                            # Virtual env directory
   |
   |-- db.sqlite3                            # SQLite storage
   |-- README.md                             # Standard readme documentation
   |-- requirements.txt                      # Development modules
   |-- manage.py                             # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## Libraries Used

- ✅ `Django` - Basic Web Framework and MVT design pattern
- ✅ `ReportLab` - Exporting in PDF format
- ✅ `Docx` Exporting in DOCX format for Word and Google Docs

## ✨ 리프핏

> One Rep Max 무게를 기반으로 Wendler 운동 시트 생성 웹앱
>
> 라이브 사이트 https://kyeongsupchoi.pythonanywhere.com/wendler.html
>
> Wendler 운동 프로그램 설명: https://www.t-nation.com/workouts/5-3-1-how-to-build-pure-strength/

## ✨ 코드 기반 구조

이 프로젝트는 아래에 제시된 간단하고 직관적인 구조를 사용하여 코딩됩니다.

```bash
<프로젝트 루트>
   |
   |-- mysite/                 # 기본 앱 디렉토리
   |    |
   |    |-- home/              # html 템플릿 파일 저장
   |    | |-- wendler.html     # 장고 태그와 부트스트랩이 포함된 Wendler html 파일
   |    |
   |    |-- asgi.py            # mysite 프로젝트에 대한 ASGI 구성.
   |    |-- forms.py           # Wendler 양식 정의
   |    |-- models.py          # Wendler 모델 정의
   |    |-- settings.py        # 전역 설정 정의
   |    |-- urls.py            # 모든 앱/노드에서 제공하는 URL 정의
   |    |-- views.py           # Wendler 무게 입력 및 계산 처리
   |    |-- wsgi.py            # 프로덕션 환경에서 앱 배포
   |    |
   |    |-- venv/              # 가상 환경 디렉토리
   |
   |-- db.sqlite3              # SQLite 데이터베이스
   |-- README.md               # 표준 readme 문서
   |-- requirements.txt        # 개발 모듈
   |-- manage.py               # 앱 시작 - Django 기본 시작 스크립트
   |
   |-- ************************************************************************
```

<br />

## 사용된 라이브러리

- ✅ `Django` - 기본 웹 프레임워크 및 MVT 디자인 패턴
- ✅ `ReportLab` - PDF 형식으로 다운로드
- ✅ `Docx` Word 및 Google 문서용 DOCX 형식으로 다운로드
