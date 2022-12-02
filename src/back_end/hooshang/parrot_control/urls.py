from django.conf.urls import url,include
from django.urls import path, re_path
from parrot_control import views
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register('parrot/control',views.ParrotCommandController,'Parrot')

urlpatterns = [
    re_path('', views.ParrotCommandController.as_view()), # The URL to load the index.html page
    # url('', include(router.urls)),
]
