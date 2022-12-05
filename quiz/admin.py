from django.contrib import admin
from django.contrib.auth import get_user_model
from . import models


@admin.register(models.Category)
class CatAdmin(admin.ModelAdmin):
	list_display = [
        'name',
        ]

@admin.register(models.Quizzes)
class QuizAdmin(admin.ModelAdmin):
	list_display = [
        'id', 
        'title',
        ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text', 
        'is_correct'
        ]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
        'body',
        ]
    list_display = [
        'title', 
        'quiz',
        'date_updated'
        ]
    inlines = [
        AnswerInlineModel, 
        ] 

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text', 
        'is_correct', 
        'question'
        ]