# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PaymentStatusModel(models.Model):
    status=models.CharField(max_length=100)
    desc=models.CharField(max_length=1000)
    orderRefNumber=models.IntegerField();