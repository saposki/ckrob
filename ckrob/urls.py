"""ckrob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

# from blog.views import UploadFileView, ListView, UploadFileIndexView, FileDetailView

from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.home, name='home'), #default home url
    url(r'^$', views.indexPage, name='indexPage'),
    url(r'^dashboard/$', 'ckrobDashBoard.views.dashBoardView'),
    url(r'^dash/$', views.dashBoard, name='dashBoard'),
    url(r'^blog/$', 'blog.views.postList'),
    url(r'^upload/$', views.uploadCsv, name='uploadCsv'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
