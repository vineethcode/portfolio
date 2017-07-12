# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
	return render(request, 'profile_page/home.html')

def skills(request):
	return render(request,'profile_page/skills.html')

def about(request):
	return render(request,'profile_page/about.html')

def work(request):
	return render(request,'profile_page/work.html')

def blog(request):
	return render(request,'profile_page/blog.html')

def contact(request):
	return render(request,'profile_page/contact.html')

# Create your views here.
