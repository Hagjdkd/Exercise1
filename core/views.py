from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
  return HttpResponse("Hello, World!")

def home (request):
  return render(request ,'home.html',{'title':'Home'})

def about (request):
  return render(request ,'about.html',{'title':'About'})
# Create your views here.
