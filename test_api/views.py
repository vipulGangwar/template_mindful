from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Test_form
from .serializers import Test_formSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
#from my_project.example.models import Profile
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.views import generic
from django.views.generic.edit import CreateView

class ProfileDetail(APIView):

    def get(self, request, pk):
        profile = get_object_or_404(Test_form, pk=pk)
        serializer = Test_formSerializer(profile)
        return Response(serializer.data)

    def post(self, request, pk):
        profile = get_object_or_404(Test_form, pk=pk)
        serializer = Test_formSerializer(profile, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'profile': profile})
        serializer.save()
        #return redirect('profile-list')

class FormCreate(CreateView):
    model = Test_form
    fields = ['first_name','last_name','email']
    template_name = 'index.html'
