from . import views
from django.conf.urls import include, url

app_name = "guides"

urlpatterns = [
    url(r'^$', views.guides, name="guides")

]
