from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dashBoardView(request):
    return HttpResponse('<html><body>Dash Board</body></html>')


# from django.shortcuts import render
#
#
# def home(request):
#     return render(request, 'home/index.html', {})
