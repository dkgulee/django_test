from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
import datetime

# Create your views here.
def hello_world(request):
    return HttpResponse("이득규")
def chee(request):
    return HttpResponse("ㅅㄷㄴㅅㄴㅅ")
def crrunt_datetime(requst):
    try:
        now = datetime.datetime.now()
        html = "<html><body> 지금 시각은:{}시{}분{}초입니다.</body></html>".format(now.hour, now.second, now.minute)
        return HttpResponse(html)
    except HttpResponseNotFound as h:
        return HttpResponseNotFound('<h1>{}</h1>'.format(h))