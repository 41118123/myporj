from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def sayhello(request):
	return HttpResponse("Hello 666!")

def hello2(request, username):
	return HttpResponse("Hello " + username)

def hello3(request,username):
	now=datetime.now()
	return render(request,"hello3.html",locals())

def hello4(request,username):
	now=datetime.now()
	return render(request,"hello4.html",locals())