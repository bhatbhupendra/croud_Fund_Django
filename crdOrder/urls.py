from django.urls import path
from . import views

app_name='crdOrder'

urlpatterns = [
    path('',views.productList, name='product_list'),
    path('<slug:slug>',views.productOrder, name='product_order'),
    path('summery/<slug:slug>',views.productSummery, name='product_summery'),
]
