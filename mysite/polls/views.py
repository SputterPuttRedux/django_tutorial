from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("POLLS index, biyatch!")

# Create your views here.
