from django.contrib import admin

from .models import Question, Choice

#  StackedInline, TabularInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1 # 여분의 Form 양식

## 재 정렬 Class
class QuestionAdmin(admin.ModelAdmin):
    # 출력 순서 입력 및 Title 입력
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']  
    search_fields = ['question_text']

# QuestionAmdin 을 args로 입력 하여 field 순서를 변경 할수있다.
# polls의 Question Model을 등록한다.
admin.site.register(Question, QuestionAdmin)


