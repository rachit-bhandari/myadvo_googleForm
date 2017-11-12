# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Form(models.Model):
    form_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    def __str__(self):
    	return self.form_name + ' - ' + self.user_name

class Choice(models.Model):
    choice_name = models.CharField(max_length=200)

    def __str__(self):
    	return self.choice_name

class Question(models.Model):
    form_id = models.IntegerField() 
    ques_id = models.IntegerField()
    question = models.CharField(max_length=255)

    def __str__(self):
    	return self.ques_id + ' - ' + self.question

class Answer(models.Model):
    ques_id = models.IntegerField()
    answer = models.CharField(max_length=255)
