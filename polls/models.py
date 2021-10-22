import datetime

from django.db import models
from django.utils import timezone

""" 
    Question.class 1 : N Choice.class
    models.ForeignKey로 연결 되어 있기 때문이다.
"""

# 질문 Class
class Question(models.Model):
    # 질문
    question_text = models.CharField(max_length=200) 
    # 게시 날자
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        # 현재로 부터 하루 전을 뺀 조건의 데이터만 출력
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        

# 선택 Class
class Choice(models.Model):
    # 선택지에 관한 질문 
    # on_delete=models.CASCADE -> Question.class 데이터 삭제시 question 데이터도 삭제 된다.
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    # 선택 Text
    choice_text = models.CharField(max_length=200) 
    # 투표 집계
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
        
