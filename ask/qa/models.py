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
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User)

    #Question - вопрос
    #title - заголовок вопроса
    #text - полный текст вопроса
    #added_at - дата добавления вопроса
    #rating - рейтинг вопроса(число)
    #author - автор вопроса
    #likes - список пользователей, поставивших "лайк"


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.OneToOneField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    #Answer - ответ
    #text - текст ответа
    #added_at - дата добавления ответа
    #question - вопрос, к которому относится ответ
    #author - автор ответа
