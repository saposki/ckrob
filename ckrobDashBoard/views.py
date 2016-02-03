# Create your views here.
from ckrobDashBoard.models import Artifact, Container
from django.http import HttpResponse

import mongoengine
user = authenticate(username=username, password=password)
assert isintance(user, mongoengine.django.auth.User)

container = Container.objects(question__contains="What").first()
newPin = Artifact(description="Heart Disease" rating=10)
container.pin.append(newPin)
container.save()

print container.question

def homePageView(request):
    return HttpResponse('<html><body>Home</body></html>')
def dashBoardView(request):
    return HttpResponse('<html><body>Dash Board</body></html>')
def blogView(request):
    return HttpResponse('<html><body>Blog</body></html>')
