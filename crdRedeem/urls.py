from django.urls import path
from . import views

app_name='crdRedeem'

urlpatterns = [
    path('',views.redeemDetail, name='redeem-detail'),
    path('redeemReq',views.redeemRequest, name='redeem-request'),
]

