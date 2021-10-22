from django.contrib import admin

from .models import Question, Choice

# polls의 Question Model을 등록한다.
admin.site.register(Question)
admin.site.register(Choice)
