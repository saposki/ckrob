from django.shortcuts import render
from django.utils import timezone
from .models import Post
# from django.http import HttpResponse

# Create your views here.
# def blogView(request):
#     return HttpResponse('<html><body>Blog</body></html>')

def postList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post.html', {})
