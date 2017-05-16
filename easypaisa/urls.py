"""easypaisa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from main.views import UserViewSet, PostbackHandler, PaymentView, PaymentStatusViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'paymentStatus', PaymentStatusViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^postbackhandler/$',csrf_exempt(PostbackHandler.as_view())),
    url(r'^payment/$',PaymentView.as_view())
]
