from django.urls import path
from .views import *
urlpatterns = [
    path('', base, name='base'),


    path('income_product/', income, name='income'),
    path('outcome_product/', outcome, name='outcome'),
    path('user/', user, name='user'),
    path('order/', order, name='order'),
    path('payment/', payment, name='payment'),
    path('overall_pay/', overall_pay, name='overall_pay'),
    path('overall_name/', overall_name, name='overall_name'),
    path('order_detail/<str:pk>/', order_detail, name='order_detail'),


    path('product_create/', productCreate.as_view(), name='product_create'),
    path('income_create/', Income_create.as_view(), name='income_create'),
    path('outcome_create/', Outcome_create.as_view(), name='outcome_create'),
    path('user_create/', user_create.as_view(), name='user_create'),
    path('order_create/', order_create.as_view(), name='order_create'),
    path('payment_create/', payment_create.as_view(), name='payment_create'),
]