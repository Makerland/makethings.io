# -*- encoding: utf-8 -*-
from django.shortcuts import render

def index(request):
	
	return render(request, "core/index.html", {})

def inyourcity(request):

	return render(request, "core/inyourcity.html", {})