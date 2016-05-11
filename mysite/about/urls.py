from . import views
from django.conf.urls import url, include


app_name = "about"

urlpatterns = [
    url(r'^$', views.about, name="about"),
]
