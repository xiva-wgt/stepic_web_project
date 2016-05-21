# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        pass

    def popular(self):
        pass


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default=0, max_length=255)
    text = models.TextField(default='')
    added_at = models.DateField(null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='user_to_likes')

    def __str__(self):
        return self.text

    #Question - вопрос
    #title - заголовок вопроса
    #text - полный текст вопроса
    #added_at - дата добавления вопроса
    #rating - рейтинг вопроса(число)
    #author - автор вопроса
    #likes - список пользователей, поставивших "лайк"


class Answer(models.Model):
    text = models.TextField(default='')
    added_at = models.DateField(null=True)
    question = models.OneToOneField(Question, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    #Answer - ответ
    #text - текст ответа
    #added_at - дата добавления ответа
    #question - вопрос, к которому относится ответ
    #author - автор ответа
