# Create your views here.
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('<html><body>Home</body></html>')
def dashBoardView(request):
    return HttpResponse('<html><body>Dash Board</body></html>')
def blogView(request):
    return HttpResponse('<html><body>Blog</body></html>')
