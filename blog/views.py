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
def upLoadFile(request):
    return render(request, 'forms/upload.html')

class UploadFileView(FormView):
    templateName = 'forms/upload.html'
    formClass = UploadForm

    def formValid(self, form):
        dataSetEntry = UploadFile(
            dataSet=self.get_from_kwargs().get('files')['dataSet'])
        dataSet.save()
        self.id = dataSet.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('dataSet', kwargs={'pk':self.id})

class FileDetailView(DetailView):
    model = UploadFile
    templateName = 'dash/detail.html'
    contextObjectName = 'file'

class UploadFileIndexView(ListView):
    model = UploadFile
    templateName = 'dash/uploaded.html'
    contextObjectName = 'files'
