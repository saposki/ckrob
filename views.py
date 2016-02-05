from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse


def home(request):
    return render(request, 'admin/base.html')
