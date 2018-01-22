from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^referee/',views.referee),
    url(r'^professional/',views.professional),
    url(r'^state/',views.state),
    url(r'^club/',views.club),
]
