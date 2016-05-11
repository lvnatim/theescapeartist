from . import views
from django.conf.urls import url, include


app_name = "home"

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^(?P<num>\d+)', views.homeslide, name="homeslide"),
]
