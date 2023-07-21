from django.conf.urls import url,include
from django.urls import path
from parrot_control import views

urlpatterns = [
    url(r'.*', views.front_static),
]
