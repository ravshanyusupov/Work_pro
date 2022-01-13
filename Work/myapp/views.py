from django.db.models import Sum
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .models import *
from django.http import Http404


def base(request):
    try:
        product = Product.objects.all()
    except:
        raise Http404
    context = {
        'product': product
    }
    return render(request, 'content.html', context=context)


class productCreate(CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_create.html'
    success_url = '/'


def income(request):
    try:
        income = Income.objects.all()
    except:
        raise Http404
    context = {
        'income': income
    }
    return render(request, 'income.html', context=context)


class Income_create(CreateView):
    model = Income
    fields = '__all__'
    template_name = 'income_create.html'
    success_url = reverse_lazy('income')


def outcome(request):
    try:
        outcome = Outcome.objects.all()
    except:
        raise Http404
    context = {
        'outcome': outcome
    }
    return render(request, 'outcome.html', context=context)


class Outcome_create(CreateView):
    model = Outcome
    fields = '__all__'
    template_name = 'out_come_create.html'
    success_url = reverse_lazy('outcome')


def user(request):
    try:
        user = User_Profile.objects.all()
    except:
        raise Http404
    context = {
        'user': user
    }
    return render(request, 'user.html', context=context)


class user_create(CreateView):
    model = User_Profile
    fields = '__all__'
    template_name = 'user_create.html'
    success_url = reverse_lazy('user')


def order(request):
    try:
        order = Order.objects.all()
    except:
        raise Http404
    context = {
        'order': order
    }
    return render(request, 'order.html', context=context)


class order_create(CreateView):
    model = Order
    fields = '__all__'
    template_name = 'order_create.html'
    success_url = reverse_lazy('order')


def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except:
        raise Http404
    context = {
        'order': order
    }
    return render(request, 'order_detail.html', context=context)




def payment(request):
    try:
        pay = Payment.objects.all()
        payment = list(Payment.objects.all().aggregate(Sum('prize')).values())[0]
    except:
        raise Http404
    context = {
        'pay': pay,
        'payment': payment
    }
    return render(request, 'payment.html', context=context)


class payment_create(CreateView):
    model = Payment
    fields = '__all__'
    template_name = 'payment_create.html'
    success_url = reverse_lazy('payment')


def overall_pay(request):
    try:
        pay = Type_of_payment.objects.all()
        payment = list(Payment.objects.all().aggregate(Sum('prize')).values())[0]
    except:
        raise Http404
    context = {
        'pay': pay,
        'payment': payment
    }
    return render(request, 'overall_pay.html', context=context)


def overall_name(request):
    try:
        user_profile = User_Profile.objects.all()
    except:
        raise Http404
    context = {
        'user_profile': user_profile
    }
    return render(request, 'overall_name.html', context=context)
