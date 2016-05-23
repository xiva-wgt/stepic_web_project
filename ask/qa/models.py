# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.


class QuestionManager(models.Manager):
    def new(self):
        qs = self.order_by('-id')
        return qs

    def popular(self):
        qs = self.order_by('-rating')
        return qs


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(default=0, max_length=255)
    text = models.TextField(default='')
    added_at = models.DateField(null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, default=1)
    likes = models.ManyToManyField(User, related_name='user_to_likes')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    def get_url(self):
        return "/question/{0}/".format(self.id)

    def get_absolute_url(self):
        return reverse('question', kwargs={'pk_question': self.pk})

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
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, default=1, on_delete=models.SET_NULL)

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.text

    #Answer - ответ
    #text - текст ответа
    #added_at - дата добавления ответа
    #question - вопрос, к которому относится ответ
    #author - автор ответа
