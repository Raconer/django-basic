from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic


from .models import Choice, Question

""" 
    return 방법
    
    1. Text Return 
        
        return HttpResponse("Hello, world. Polls") 

    2. DB에서 Data 가져온후 TEXT로 출력
        
        # 5개의 Question 데이터를 불러온다.
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        # , 로 연결된 question 데이터를 Text화 시킨다.
        output = ', '.join([q.question_text for q in latest_question_list])
        return HttpResponse(output)

    3. DB에서 데이터를 가져온후 HTML로 출력

        # 5개의 Question 데이터를 불러온다.
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        # 넘길 html 위치 
        template = loader.get_template('polls/index.html')
        # 넘겨줄 데이터 
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))

    4. DB에서 데이터를 가져온후 HTML로 출력 간략화 (3번을 간략화 시킨 방법이다.)

        # 5개의 Question 데이터를 불러온다.
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        # 데이터를 Context에 넣어서 Response한다.
        context = {'latest_question_list': latest_question_list}
        # 3번과 달리 render를 사용하여 HTML을 출력한다.
        return render(request, 'polls/index.html', context)

"""

""" 
    404 ERROR 일으키기

    1. try except 사용

        try:
            question = Question.objects.get(pk=question_id)
        # 데이터가 존재 하지 않을 경우 except 실행된다.
        except Question.DoesNotExist:
            # 404 페이지로 이동한다.
            raise Http404("Question does not exist")
        return render(request, 'polls/detail.html', {'question': question}) 

    2. Short cut (방법 1을 간략화 시킨 방법)
        #  기존 try except를 사용하지 않고 get_object_or_404를 사용하여 페이지 이동을 시도했다.
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
"""
"""  
    Use Generic
"""
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # 현재 시간기준 이전 시간대 5개 출력
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        # pub_date가 미래인것들은 출력하지 않는다
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

""" 
    Not User Generic
"""
""" def index(request):
    
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# 404 에러 예제
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

"""

def vote(request, question_id):
    # Read Question Detail with pk
    question = get_object_or_404(Question, pk=question_id)
    try:
        # question.choice set get with pk
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # 예외 처리
        print("Vote Exception")
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        print("Vote Success")
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) 
        