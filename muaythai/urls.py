"""Championship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
import home.views
urlpatterns = [
    url(r'^$',home.views.index),
    url(r'^addhome/',home.views.addhome),
    url(r'^listhome/',home.views.listhome),
    url(r'^filterhome/',home.views.filterhome),
    url(r'^committee/',home.views.committee),
    url(r'^admin/', admin.site.urls),
    url(r'^$',include('home.urls')),
    url(r'^list/',include('list.urls')),
    url(r'^professional/',include('professional.urls')),
    url(r'^filter/',include('filter.urls')),

]
