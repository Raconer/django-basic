from django.contrib import admin

from .models import Question

# polls의 Question Model을 등록한다.
admin.site.register(Question)
