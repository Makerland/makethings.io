# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
	
	return HttpResponse('global make things')

