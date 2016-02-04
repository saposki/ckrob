from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('<html><body>Home</body></html>')
def dashBoardView(request):
    return HttpResponse('<html><body>Dash Board</body></html>')
def blogView(request):
    return HttpResponse('<html><body>Blog</body></html>')
