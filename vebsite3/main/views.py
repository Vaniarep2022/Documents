from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return HttpResponse("<h4>Hello</h4>")

def reshka(requst):
    return HttpResponse("<h4>Что сегодня?</h4>")
