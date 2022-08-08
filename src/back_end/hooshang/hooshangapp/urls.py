from django.conf.urls import url,include
from django.shortcuts import render
from django.urls import path , re_path
from hooshangapp import views
from django.views.generic import TemplateView

urlpatterns = [
    re_path('reqpub', views.ReqpubCommandController.as_view()), # The URL to push emotion commands on
    re_path('reqcli', views.HooshangCommandController.as_view()), # The URL to get emotion commands from
    re_path('', TemplateView.as_view(template_name='index.html')) # The URL to load the index.html page
]




