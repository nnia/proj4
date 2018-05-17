# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, loader

# Create your views here.
from django.http import HttpResponse
from app4.models import Person

import datetime

#def index(request):
#    return HttpResponse("Hello, world1. ")
# Функции представления

def indef(request):
    return HttpResponse("Hello World1!")

def index(request):
    return render(request, "index.html")

#-----------------------------------------------------

def hello(request):     
	return HttpResponse("Hello world 4!")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)


#-----------------------------------------------------
# My pages with separate URLs

def defaultf(request):
	return render(request, "defaultf.html")	

def coding(request):
	return render(request, "coding.html")

def testbase(request):
	person = Person.objects.all()
	return render(request, "testbase.html", {"person": person})

def enfant(request):
	return render(request, "enfant.html")

def answer(request):
	print("-----answer-----")
	#person = Person.objects.get(id=0)
	#person = Person.objects.order_by('age')
	
	#Person.surname = "surname1"	
	#person = Person.objects.all()
	person = Person.objects.all()
	
	#print(e.age for e in person)
	p = Person.objects.values_list('id', 'surname')

	#print(person.query.__str__())
	print p

	#print(Person.objects.filter(age='11').values)
	#print(person.get(age="11"))
	#for (item in person)
	

	print("---------------")
	return render(request, "answer.html", {"person": person})	
	#return render(request, "answer.html")	

	#template = loader.get_template('answer/answer.html')
	#return HttpResponse(template.render(request))
    

def header(request):
	print("((((((((((((((((((((((((((((((((((((((((((((")
	return render(request)



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