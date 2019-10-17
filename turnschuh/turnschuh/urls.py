"""turnschuh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from turnschuh import views
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^connect$', views.connect, name='connect'),
    url(r'^connect/authorize', views.connect_authorize_onboard, name='connect-authorize')
    url(r'^download$', views.filedownload, name='download'),
    url(r'^abfrage$', views.abfrage, name='abfrage'),
    url(r'^delete$', views.delete, name='delete')


]
