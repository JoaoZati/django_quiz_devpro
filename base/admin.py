from django.contrib import admin
from base.models import Question, Participant, Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'available', 'answers', 'right_answer')


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at')


@admin.register(Answer)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('id', 'participant', 'question', 'points', 'created_at')
