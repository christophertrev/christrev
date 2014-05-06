from django.shortcuts import render
from django.http import HttpResponse



def index(request):


	return render(request, 'startpage/index.html')
    #return HttpResponse("Rango says hello world!")


def cover(request):


	return render(request, 'startpage/cover.html')

# Create your views here.
