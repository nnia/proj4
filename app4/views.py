# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse
from app4.models import Person
from app4.models import QuestionSet


import datetime
import os



#def index(request):
#    return HttpResponse("Hello, world1. ")
# Функции представления
#-----------------------------------------------------
# Базовое

def indef(request):
    return HttpResponse("Hello World1!")

def index(request):
	#print os.path.abspath(__file__)
    return render(request, "index.html")

#-----------------------------------------------------
# Вспомогательные для неоднократного использования

def hello(request):     
	return HttpResponse("Hello world 4!")


def hello_world(request):
    return HttpResponse("Hello, World")

def header(request):
	txt = "<h1>Заголовок H1</h1>" 
	#return HttpResponse(request, {"txt":txt})
	return HttpResponse(txt)

def current_datetime(request):
	now1 = datetime.datetime.now()
	#html = "<html><body>It is now %s.</body></html>" % now
	return now1
	#return render(request, {"header": header(request)})


#-----------------------------------------------------
# Отдельные страницы целиком
# My pages with separate URLs

def defaultf(request):
	return render(request, "defaultf.html")	

def coding(request):
	return render(request, "coding.html")

def testbase(request):
	person = Person.objects.all()
	questionSet = QuestionSet.objects.all()
	return render(request, "testbase.html", 
		{"person": person, 
		"questionSet" : questionSet})

def best_dprk(request):
	return render(request, "best_dprk.html")


def enfant(request):
	#print os.path.dirname(__file__)
	#print os.path.abspath(os.path.join(__file__,"../.."))
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

	print BASE_DIR #os.path.join(BASE_DIR, '../db.sqlite3')
	print hello (request)
	return render(request, "enfant.html")

def answer(request):
	person = Person.objects.all()

#	newp = Person(surname = 'Valentinova', name = 'Valentina', age = 4, result = 56)
#	newp.save()
	
	#print(e.age for e in person)
	p = Person.objects.values_list('id', 'surname')

	#print(person.query.__str__())
	print p

	#print(Person.objects.filter(age='11').values)
	#print(person.get(age="11"))
	#for (item in person)

	current_datetime(request)
	print("---------------")
	return render(request, "answer.html", {
		"person": person, 
		"current_datetime": current_datetime(request),
		"header": header(request)  })	

def contact(request):
    errors = []
    form = {}
    if request.POST:
         
        form['name'] = request.POST.get('name')
        form['email'] = request.POST.get('email')
        form['message'] = request.POST.get('message')
         
        if not form['name']:
            errors.append('Заполните имя')
        if '@' not in form['email']:
            errors.append('Введите корректный e-mail')
        if not form['message']:
            errors.append('Введите сообщение')
             
        if not errors:
            # ... сохранение данных в базу
            return HttpResponse('Спасибо за ваше сообщение!')
         
    return render(request, 'contact.html', {'errors': errors, 'form':form})
