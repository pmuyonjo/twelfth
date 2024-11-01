from django.http import HttpResponse
from django.shortcuts import render
from .models import Pictures


def index(request):
    pixs = Pictures.objects.all()
    return render(request, 'index.html', {'pixs': pixs}) #HttpResponse("Hello")
