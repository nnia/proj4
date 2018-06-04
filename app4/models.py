# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Person(models.Model):
	id = models.IntegerField(primary_key=True)
	surname = models.CharField(max_length=25)
	name = models.CharField(max_length=25)
	age = models.IntegerField(default=0)
	result = models.IntegerField(default=0)
	def __str__(self):
		return ' '.join([
		self.id,
		self.surname,
		self.name,
		self.age,
		self.result,
	])

class QuestionSet(models.Model):
	id = models.IntegerField(primary_key=True)
	question = models.CharField(max_length=127)
	nAnswers = models.IntegerField(default=3)
	answer1 = models.CharField(max_length=127)
	answer2 = models.CharField(max_length=127)
	answer3 = models.CharField(max_length=127)
	rightAnswer = models.IntegerField(default=1)
	ageMin = models.IntegerField(default=0)
	ageMax = models.IntegerField(default=100)
	choice = models.IntegerField(default=100)
	def __str__(self):
		return ' '.join([
		self.id,
		self.question,
		self.nAnswers,
		self.answer1,
		self.answer2,
		self.answer3,
		self.rightAnswer,
		self.ageMin,		
		self.ageMax,
		self.choice,
	])