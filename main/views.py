# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
import logging
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import View
from rest_framework import serializers, viewsets
from easypaisa.settings import STORE_ID, PAYMEN_TEMPLATE, PAY_TEMPLATE, EASYPAISA_POST_BACK_URL, EASYPAISA_SERVER_URL


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
    def get(self, request):
        logging.debug(request.GET)
        loopcount = int(request.GET.get('loopcount', 0)) + 1
        if(loopcount==1):
            context = {
                'auth_token': request.GET.get('auth_token'),
                'postBackURL': '%s?loopcount=%s' % (EASYPAISA_POST_BACK_URL, loopcount),
                'EASYPAISA_SERVER_URL': EASYPAISA_SERVER_URL
            }
        if loopcount==2:
            context={
                'status':request.GET.get('status',''),
                'desc':request.GET.get('desc',''),
                'orderRefNumber':request.GET.get('orderRefNumber',''),
            }
        return render(request, PAY_TEMPLATE, context)


class PaymentView(View):
    def get(self, request):
        context = {'store_id': STORE_ID, 'EASYPAISA_SERVER_URL': EASYPAISA_SERVER_URL}
        return render(request, PAYMEN_TEMPLATE, context)
