from turtle import title
from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

#Представление либо контроллер
def index(request) :
    context = {
        'title': 'Home',
        'content' : 'This is main page - Home',
        'list' : ['first','second'],
        'dict' : {'first' : 1},
        'is_auth' : False
    }

    return render(request,'main/index.html', context)

def about(request):
    return HttpResponse("About page")