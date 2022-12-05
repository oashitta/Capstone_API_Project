from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from django.utils.timezone import datetime

class Category (models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        
    name = models.CharField(max_length=255, null=True)
    
    def __str__(self):
            return self.name

class Quizzes (models.Model):

    class Meta:
        verbose_name = _("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ['id']

# change title from new quiz. dont like that.
    title = models.CharField(max_length=250, default = _("New Quiz"), verbose_name= _("Quiz Title"))
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.title
    

class Updated(models.Model):

    date_updated = models.DateTimeField(verbose_name= _("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class Question (Updated):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']
    
    LEVEL = (
        (0, _('Foundation')),
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advanced')),
        (4, _('Expert'))
    )

    TYPE = (
        (0, _('Multiple Choice')),
        (1, _('Fill in the Gap')),
        (2, _('Short Answer')),
        (3, _('True or False')),

    )
    
    quiz = models.ForeignKey(
    Quizzes, related_name='question', on_delete=models.DO_NOTHING
   )
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Question Type"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    body = models.TextField(blank=True, null=True)
    difficulty = models.IntegerField(choices=LEVEL, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title


class Answer (Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']
        
    question = models.ForeignKey(Question, related_name ='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_correct = models.BooleanField(default=False)
        
    def __str__(self):
        return self.answer_text
