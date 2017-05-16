# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
import logging

from django import template
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from django.template import loader
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

    def get(self, request):
        logging.debug(request.GET),
        context = {
            'auth_token': request.GET.get('auth_token'),
            'postBackURL':'https://easypaisa.herokuapp.com/postbackhandler'
        }
        return render(request, 'pay.html',context)

    def post(self, request):
        logging.debug(request.POST)
        return self.response


class PaymentView(View):
    def get(self, request):
        return render(request, 'index.html')
