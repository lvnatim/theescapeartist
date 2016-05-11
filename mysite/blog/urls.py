from . import views
from django.conf.urls import url, include

app_name = "blog"

urlpatterns = [

    url(r'^$', views.blog, name='blog'),
]
