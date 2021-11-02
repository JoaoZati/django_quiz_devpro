from django.contrib import admin
from base.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', 'available', 'answers', 'right_answer')
