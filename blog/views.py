from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView
from django.utils import timezone

from .models import Post, UploadFile
from .forms import UploadForm



# from django.http import HttpResponse


# Uncomment to enable default home page view -
# Uncommnet corresponding url pattern in urls.py
# def home(request):
#     return render(request, './admin/base.html')

def postList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post.html', {'posts': posts})
def indexPage(request):
    return render(request, 'home/index.html')
def dashBoard(request):
    return render(request, 'dash/dash.html')
def uploadCsv(request):
    form = UploadForm()
    context = {
        "form": form,
    }
    return render(request, 'forms/upload.html', context)
    # if request.method == 'POST':
        # form = UploadForm(request.POST, request.FILES)

    # else:
        # form = UploadForm()
    # return render_to_reponse('upload.html', {'form': form})
