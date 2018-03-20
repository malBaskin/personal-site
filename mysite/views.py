
from django.shortcuts import render, redirect, render_to_response
from django.db import models

def hello(request):
	return render(request, 'home.html')

