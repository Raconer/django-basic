import datetime
from django.http import response

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question
# Create your tests here.
''' 
    테스트용 Question 생성 함수
    question_text와 days를 입력받아 Question Object를 생성한다.
'''
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
    
# Question Model 테스트
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)
        
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    
# Question View Test
class QuestionIndexViewTests(TestCase):
    # 호출된 Question이 없을시 해당 메시지가 출력된다. 
    def test_no_questions(self):
        # index 데이터 호출
        response = self.client.get(reverse('polls:index'))
        # 상태 코드를 비교한다.
        self.assertEqual(response.status_code, 200) 
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # 호출된 Question의 pub_date가 과거라면 데이터와 함께 index페이지에 출력된다.
    def test_past_question(self):
        # 과거 데이터 생성
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    # 호출된 QUestion의 pub_date 가 미래라면 데이터와 함께 index페이지로 이동한다.
    def test_future_question(self):
        # 미래 데이터 생성
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    # 과거, 미래 데이터가 동시에 존재 하더라도 과거 데이터만 출력됩니다.  
    def test_furture_question_and_past_question(self):
        # 과거 데이터 생성
        question = create_question(question_text="Past question.", days=-30)
        # 미래 데이터 생성
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question],
        )

    # 2개(다수) 과거 Question 데이터 출력
    def test_two_past_questions(self):
        # 과거 Question 1
        question1 = create_question(question_text="Past question 1.", days=-30)
         # 과거 Question 2
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1],
        )

# Question Detail View Test
class QuestionDetailViewTests(TestCase):
    # Future pub_date일 경우 404 를 Return 합니다.
    def test_future_question(self):
        # 미래 데이터 생성
        future_question = create_question(question_text="Future question.", days=5)
        # detail에 future id를 args로 Get Req를 한다.
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    # 과거 pub_date안 Qusetion Text 가 출력됩니다. 
    def test_past_question(self):
        past_question = create_question(question_text='Past Question.', days=-5)
        url = reverse('polls:detail', args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
        
        