from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url, include
from rest_framework import routers

from easypaisa_module.views import PostbackHandler, PaymentView, PaymentStatusViewSet

router = routers.DefaultRouter()
router.register(r'status', PaymentStatusViewSet)
urlpatterns=[
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^postbackhandler/$',csrf_exempt(PostbackHandler.as_view())),
    url(r'^start/$',PaymentView.as_view())
]