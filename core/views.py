from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Announcement

def hello(request):
  return HttpResponse("Hello, World!")

def home(request):
  return render(request, 'home.html', {'title': 'Home'})

def about(request):
  return render(request, 'about.html', {'title': 'About'})

def announcements_list(request):
  announcements = Announcement.objects.all()
  return render(request, 'announcements/list.html', {
    'title': 'Announcements',
    'announcements': announcements
  })

def announcement_detail(request, id):
  try:
    announcement = get_object_or_404(Announcement, id=id)
    return render(request, 'announcements/detail.html', {
      'title': announcement.title,
      'announcement': announcement
    })
  except Http404:
    return render(request, '404.html', {'title': 'Page Not Found'}, status=404)

def custom_404(request, exception=None):
  return render(request, '404.html', {'title': 'Page Not Found'}, status=404)
