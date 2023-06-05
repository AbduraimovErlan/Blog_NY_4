from django.http import HttpResponse
from django.shortcuts import redirect

""" MVC - Model View Controller """

def first_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello! its first view ;)')



def redirect_to_youtube_view(request): #перенаправление на существуеший адресс сайта
    if request.method == "GET":
        return redirect('https://www.youtube.com/')