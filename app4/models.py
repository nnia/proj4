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
