from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, Http404
from .models import *

menu = [{"title": 'Главная', 
         "name": "home"},
        {"title": 'Услуги', 
         "name":"services"},
        {"title": 'Наши клиенты', 
         "name":"clients"},
        {"title": 'Войти', 
         "name": "login"}
        ]

db = Services.objects.all()
data = {'title':'', 'menu': menu, 'services':db}

def index(request):
    # data = {'service':request.GET['service'],'access':request.GET['access']}
    # if(request.GET['service'] == 'sunbathing'):
    #     print(request.GET)
    #     raise Http404()
    # else:

    data["title"] = 'Главная'
    return render(request, 'skynet/test.html', context=data)

def services(request):
    data["title"] = "Услуги"
    return render(request, 'skynet/services.html', context=data)

def test(request):
    return render(request, "skynet/index.html", context=data)

def login(request):
    return render(request, "skynet/login.html", context=data)

def service(request, id):
    data["services"] = Services.objects.get(pk=id)
    data["title"] = data["services"].title
    if data["services"].is_published:
        return render(request, "skynet/article.html", context=data)
    else:
        return Http404
    # return HttpResponse(f"{id}")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Вам в Рай</h1>')