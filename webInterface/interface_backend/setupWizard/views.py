from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse, StreamingHttpResponse
from django.core.files.storage import Storage
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.template.response import TemplateResponse
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response 
from setupWizard.models import FeaturesConfig
# Create your views here.

class WizardWindow(APIView):
    model = FeaturesConfig()
    def get(self,request):
        return TemplateResponse(request, 
            'Modified_files/setupwizardrobot.html')
    
    def post(self, request):
        json = request.POST.items()
        for feature,value in json:
            setattr(self.model,feature,value)
        msg = {
            'msg':'success'
        }
        return JsonResponse(msg, status=201)
