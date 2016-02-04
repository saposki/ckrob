from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blogView(request):
    return HttpResponse('<html><body>Blog</body></html>')
