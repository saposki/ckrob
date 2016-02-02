# Create your views here.
from django.http import HttpResponse

def dashBoardView(request):
     return HttpResponse('<html><body>Dash Board</body></html>')
