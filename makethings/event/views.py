# -*- encoding: utf-8 -*-
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event, Website

def index(request, city):
	try:
		website = Website.objects.get(url=city)
	except Website.DoesNotExist:
		return redirect('index')

	return render(request, "event/index.html", {
		'website': website
	})