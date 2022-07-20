from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return render(requst, 'index.html')

def reshka(requst):
    return HttpResponse("<h4>Что сегодня?</h4>")

def about(requst):
    return HttpResponse("<h4>About</h4>")