from django.urls import path
from django.conf.urls import url
from . import views
#from .views import
from rest_framework.views import APIView
from django.views.generic import ListView

urlpatterns = [
    url(r'^$',views.FormCreate.as_view(), name='index'),
    url(r'^test_form/(?P<pk>[0-9]+)/$',views.ProfileDetail.as_view(), name='profile-detail'),
]
