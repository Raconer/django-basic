# 프로젝트 목적

1. 사람들이 설문 내용을 보고 직접 투표할 수있는 개방된 사이트
2. 관리자가 설문을 추가, 변경, 삭제할 수 있는 관리용 사이트

# 기본 단어
1. Project vs App
    * Project 는 App을 묶음이다.
    *. 따라서 App은 기능이라고 생각 하면된다.

# 명령어

### Python 

1. 가상환경 설치
    * python -m venv "가상환경 이름"
    * ex) python -m venv venv

### pip
1. pip upgrade
    * pip install --upgrade pip

### Django
1. django 설치
    * py -m pip install Django

1. django 버전확인
    * python -m django --version

1. django 서버 실행
    * py manage.py runserver

1. app 생성
    * py manage.py startapp polls

# 각 폴더 기능
* Basic은 root path이다. 
* manage.py: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티 입니다. manage.py 에 대한 자세한 정보는 django-admin and manage.py 에서 확인할 수 있습니다.
* mysite/ 디렉토리 내부에는 프로젝트를 위한 실제 Python 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여, (mysite.urls 와 같은 식으로) 프로젝트의 어디서나 Python 패키지들을 임포트할 수 있습니다.
    * __init__.py: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일입니다. Python 초심자라면, Python 공식 홈페이지의 패키지를 읽어보세요.
    * settings.py: 현재 Django 프로젝트의 환경 및 구성을 저장합니다. Django settings에서 환경 설정이 어떻게 동작하는지 확인할 수 있습니다.
    * urls.py: 현재 Django project 의 URL 선언을 저장합니다. Django 로 작성된 사이트의 《목차》 라고 할 수 있습니다. URL dispatcher 에서 URL 에 대한 자세한 내용을 읽어보세요.
    * asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See ASGI를 사용하여 배포하는 방법 for more details.
    * wsgi.py: 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다. WSGI를 사용하여 배포하는 방법를 읽어보세요.

# Django 

![djangocycle](https://user-images.githubusercontent.com/26734934/138220855-bb934e58-cd82-4e3b-9839-824d93108a23.jpg)

# Flow

client -> domain -> basic > urls.py -> polls >urls.py -> views.py 이동