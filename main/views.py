# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import View
from rest_framework import serializers, viewsets

# Serializers define the API representation.



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PostbackHandler(ListView):
    response = HttpResponse('TEST DATA')
    def get(self,request):
        logging.debug(request.GET)
        return self.response

    def post(self,request):
        logging.debug(request.POST)
        return self.response
