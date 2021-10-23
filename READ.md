# 참고 유투브 
https://www.youtube.com/watch?v=-Nmtakm70Ro

# Django Document
https://docs.djangoproject.com/en/3.2/

# 프로젝트 목적

1. 사람들이 설문 내용을 보고 직접 투표할 수있는 개방된 사이트
2. 관리자가 설문을 추가, 변경, 삭제할 수 있는 관리용 사이트

## View 페이지 구성

* 질문 《색인》 페이지 – 최근의 질문들을 표시합니다.
* 질문 《세부》 페이지 – 질문 내용과, 투표할 수 있는 서식을 표시합니다.
* 질문 《결과》 페이지 – 특정 질문에 대한 결과를 표시합니다
* 투표 기능 – 특정 질문에 대해 특정 선택을 할 수 있는 투표 기능을 제공합니다.

# 기본 단어
1. Project vs App
    * Project 는 App을 묶음이다.
    * 따라서 App은 기능이라고 생각 하면된다.

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

1. django 프로젝트 생성
    * django-admin startproject mysite

1. django 서버 실행
    * py manage.py runserver

1. app 생성
    * py manage.py startapp polls

1. 데이터 베이스 테이블 생성 명령어
    * py manage.py migrate

1. 명시된 models.py를 DB에 설계 하도록 명시 하는 명령어
    * py manage.py makemigrations 'App name' 
    * ex) py manage.py makemigrations polls -> polls에 명시된 model을 DB에 설계 명시한다.
        * 실행시 polls\migrations\0001_initial.py 에 model이 명시 되었다고 출력이 되며 파일에 접근하면 확인할수있다.

# API 명령어
1. API Shell 접근
    * py manage.py shell

1. Import Models
    <!--  polls의 models에 있는 Choice.class와 Question.class 를 Import한다.  -->
    * from polls.models import Choice, Question

1. Model 안 데이터 출력 (DB 테이블 출력이라고 생각 하면된다.)
    <!-- Question table 출력 -->
    * Question.objects.all()  

1. Select Data with where
    <!-- id 가 1인 데이터 -->
    * Question.objects.filter(id=1)
    <!--question_text 시작 Text 가 What 일때. --> 
    * Q
    <!-- 올해 데이터 출력 (Not Working)-->
    * Question.objects.get(pub_date__year=current_year) 

1. Insert Data 
    <!-- Class 생성자 입력하듯시 사용한다. -->
    * q = Question(question_text="What's new?", pub_date=timezone.now())
    * q.save() 를 해야 저장 완료

1. Update Data
    * 기존 Insert된 Data 기준으로
    * question_text update시 -> q.question_text="update Text" 작성
    * pub_date update시 -> q.pub_date=timezone.now() 작성
    * 마찬가지로 q.save()를 해야 DB에 저장이 된다.

1. Delete Data
    * q.delete()

1. FK 셋팅된 Choice 테이블 생성
    * Default : q = Question.objects.get(pk=1)
    <!-- Question pk가 1인 Choice 생성 -->
    * q.choice_set.all() 

1. 같은 FK 테이블 데이터 입력
    * q.choice_set.create(choice_text='Not much', votes=0)

1. FK 관련 Choice 데이터 출력
    *  q.choice_set.all()
    <!-- 갯수 출력 -->
    * q.choice_set.count() 

1. Test 명령어
    *  py manage.py test polls


# 각 폴더 기능
* Basic은 root path이다. 
* manage.py: Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인의 유틸리티 입니다. manage.py 에 대한 자세한 정보는 django-admin and manage.py 에서 확인할 수 있습니다.
* mysite/ 디렉토리 내부에는 프로젝트를 위한 실제 Python 패키지들이 저장됩니다. 이 디렉토리 내의 이름을 이용하여, (mysite.urls 와 같은 식으로) 프로젝트의 어디서나 Python 패키지들을 임포트할 수 있습니다.
    * __init__.py: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일입니다. Python 초심자라면, Python 공식 홈페이지의 패키지를 읽어보세요.
    * settings.py: 현재 Django 프로젝트의 환경 및 구성을 저장합니다. Django settings에서 환경 설정이 어떻게 동작하는지 확인할 수 있습니다.
    * urls.py: 현재 Django project 의 URL 선언을 저장합니다. Django 로 작성된 사이트의 《목차》 라고 할 수 있습니다. URL dispatcher 에서 URL 에 대한 자세한 내용을 읽어보세요.
    * asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See ASGI를 사용하여 배포하는 방법 for more details.
    * wsgi.py: 현재 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점입니다. WSGI를 사용하여 배포하는 방법를 읽어보세요.

# 기본 App

기본적으로는, basic > setting.py > INSTALLED_APPS는 Django와 함께 딸려오는 다음의 앱들을 포함합니다.
(polls App 도 사용하기 위해 setting.py에 'polls.apps.PollsConfig'을 명시한다.)

1. django.contrib.admin :   관리용 사이트. 곧 사용하게 될 겁니다.
2. django.contrib.auth  :    인증 시스템.
3. django.contrib.contenttypes  :   컨텐츠 타입을 위한 프레임워크.
4. django.contrib.sessions  :   세션 프레임워크.
5. django.contrib.messages  :   메세징 프레임워크.
6. django.contrib.staticfiles   :   정적 파일을 관리하는 프레임워크.

# Django 

![djangocycle](https://user-images.githubusercontent.com/26734934/138220855-bb934e58-cd82-4e3b-9839-824d93108a23.jpg)

# Flow

client -> domain -> basic > urls.py -> polls >urls.py -> views.py 이동

# urls.py
1. Not use generic
    * ```python 
      app_name='polls'
      urlpatterns = [
        # ex: /polls/
        path('', views.index, name='index'),
        # ex: /polls/5/
        path('<int:question_id>/', views.detail, name='detail'),
        # ex: /polls/5/results/
        path('<int:question_id>/results/', views.results, name='results'),
        # ex: /polls/5/vote/
        path('<int:question_id>/vote/', views.vote, name='vote'),
      ]
      ```

# DataBase

basic >  settings.py 의 DATABASES 데이터 변경(Default sqlite3)

* django.db.backends.sqlite3
* django.db.backends.postgresql
* django.db.backends.mysql
* django.db.backends.oracle

## 서버에서 DB 출력
* Question.objects.order_by('-pub_date')[:5]
    * Question 테이블에서 pub_date 를 출력한다. 5개 씩

# Model 

각 App별 models.py 에 생성

# Admin App/관리자 페이지

## 명령어

1. 관리자 계정 생성
    * py manage.py createsuperuser
    * username : admin, pw: 1q2w3e4r, email:admin@admin.com

## 관리자 페이지 에서 App 관리 하기 

1. App 내부에 admin.py 파일 생성
    * ex) polls > admin.py 파일 생성
    * admin.site.register(Question) 하여 Question Model을 Admin 에 등록한다.

# Django HTML

1. Text 출력
    * ```python
        {{ question.question_text }}
        ```
2. For 문 출력
    * ```python
        {% for choice in question.choice_set.all %}
            <li>{{ choice.choice_text }}</li>
        {% endfor %}
        ```
3. URL 
    1. ```python
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
        ```  
    2.  ```python
        # 1. 하단 href="{% url 'detail' question.id %}" 중 'detail'은 polls > urls.py의 path name 이다.
        #  2. detail은 다른 template 에서도 사용할수 있으므로 urls.py 에서 app_name을 지정하여 사용한다. (사용후 'polls:detail' 로 사용한다..)
        <li><a href="{% url ''polls:detail' question.id %}">{{ question.question_text }}</a></li>
        ```  

4. 단수 복수 처리
    * ```python 
      {{ choice.votes|pluralize }}
      ```
# VIEW

HTML view는 App > templates > App > index.html 순으로 만들어 진다.

## 1. HTML 페이지 이동 방법
    
1. Text Return 
    * ```python 
      return HttpResponse("Hello, world. Polls")
        ```

2. DB에서 Data 가져온후 TEXT로 출력
    *   ```python       
        # 5개의 Question 데이터를 불러온다.
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        # , 로 연결된 question 데이터를 Text화 시킨다.
        output = ', '.join([q.question_text for q in latest_question_list])
        return HttpResponse(output)
        ```

3. DB에서 데이터를 가져온후 HTML로 출력
    *   ```python 
        # 5개의 Question 데이터를 불러온다.
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        # 넘길 html 위치 
        template = loader.get_template('polls/index.html')
        # 넘겨줄 데이터 
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))
        ```

4. DB에서 데이터를 가져온후 HTML로 출력 간략화 (3번을 간략화 시킨 방법이다.)
    *   ```python 
        # 5개의 Question 데이터를 불러온다.
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        # 데이터를 Context에 넣어서 Response한다.
        context = {'latest_question_list': latest_question_list}
        # 3번과 달리 render를 사용하여 HTML을 출력한다.
        return render(request, 'polls/index.html', context)
        ```
5. Redirect
    * ```python
      return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        ```

## 2. 404 ERROR 일으키기

1. try except 사용
    * ```python 
      try:
        question = Question.objects.get(pk=question_id)
      # 데이터가 존재 하지 않을 경우 except 실행된다.
      except Question.DoesNotExist:
      # 404 페이지로 이동한다.
      raise Http404("Question does not exist")

      return render(request, 'polls/detail.html', {'question': question}) 
        ```

2. Short cut (방법 1을 간략화 시킨 방법)
    * ```python 
      #  기존 try except를 사용하지 않고 get_object_or_404를 사용하여 페이지 이동을 시도했다.
      question = get_object_or_404(Question, pk=question_id)
      return render(request, 'polls/detail.html', {'question': question})
        ```

# Test

테스트 코드를 작성하기 위해서는 App > tests.py에 테스트 코드를 작성하면된다.

## 테스트 명령어 

* py manage.py test polls

## 테스트 방식

0. 공통 테스트 환경
    * Shell API 환경에서 테스트 한다.
    * ```python
        py manage.py shell
      ```

1. 뷰 테스트 
    * 뷰 테스트는 app > tests.py 에서 테스트 코드들로 views.py를 실행시켜 테스트 코드를 실행한다.

2. 클라이언트 테스트
    * client에서 req 해서 테스트 하는 방식
    * 테스트 순서
        1.  ```python
            # 테스트 환경 구축 ( Reponse와 같은 속성을 사용할수있게 된다.)
            # Test Util 에서 Test 환경을 import 시킨다.
            from django.test.utils import setup_test_environment
            # Test 환경을 셋팅 시킨다. 
            setup_test_environment()
            ```
        2.  ```python
            # 테스트 클라이언트 
            # Client Class를 Import 한다.
            from django.test import Client
            # 클라이언트 Class를 설정한다.
            client = Client()
            ```
        3. ```python
           # '/' Get 방식으로 Request 한다.
           response = client.get('/') # >> Not Found: / : 찾을수 없다는 Text가 뜬다.(실제로 구현되어 있지 않음)
           response.status_code # 404 : 상태코드 확인 가능
           from django.urls import reverse # reserve 를 사용하여 polls >  url name 을 사용할수있다.
           response = client.get(reverse('polls:index')) # polls > url name사용하여 호출하였다.
           response.status_code # 200 : 성공 상태 코드가 출력되었다.
           response.content # Response 한 데이터가 출력된다. (HTML 코드가 출력 되었다.)
           response.context['latest_question_list'] # Context 데이터를 출력 할수가 있다.
           ```
