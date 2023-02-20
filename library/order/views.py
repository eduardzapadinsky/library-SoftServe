from django.shortcuts import render, redirect
from .models import Order
from authentication.models import CustomUser
from book.models import Book
import datetime
from . import forms
from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.response import Response


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


def show_all_orders(request):
    if request.user.is_authenticated and request.user.role:
        data = Order.get_all()
        context = {'list_of_order': data}
        return render(request, 'order/order_all.html', context)

    return render(request, 'order/order_all.html', {})


def show_own_orders(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        if user_id:
            try:
                data = list(Order.get_all_by_user_id(user_id))
                context = {'order_by_id': data}
                return render(request, 'order/order_own_list.html', context)
            except:
                return render(request, 'order/order_own_list.html', {'order_by_id': "None order"})

    return render(request, 'order/order_own_list.html')


def create_an_order(request):
    if request.user.is_authenticated:
        if request.user.role:
            createform = forms.UserBookSelectForm()
            if request.method == 'POST':
                data = request.POST
                term = datetime.datetime.now() + datetime.timedelta(days=int(data['date_end']))
                order = Order.create(data['users'], data['books'], term)
                try:
                    return render(request, 'order/order_create.html', {'form': createform,
                                                                       'resolt': f"Order # {str(order.id)} created"})
                except AttributeError:
                    return render(request, 'order/order_create.html', {'form': createform,
                                                                       'resolt': f"Choose other book"})
            return render(request, 'order/order_create.html', {'form': createform})
        else:
            createform = forms.BookSelectForm()
            if request.method == 'POST':
                data = request.POST
                user = CustomUser.objects.get(pk=request.user.id)
                term = datetime.datetime.now() + datetime.timedelta(days=int(data['date_end']))
                order = Order.create(user.id, data['books'], term)
                try:
                    return render(request, 'order/order_create.html', {'form': createform,
                                                                       'resolt': f"Order # {str(order.id)} created"})
                except AttributeError:
                    return render(request, 'order/order_create.html', {'form': createform,
                                                                       'resolt': f"Choose other book"})
            return render(request, 'order/order_create.html', {'form': createform})
    return redirect(request.path)


def del_order_by_root(request):
    if request.user.is_authenticated and request.user.role:
        form0 = forms.OrderDelFormUser()
        form1 = forms.OrderDelForm()
        if request.method == 'POST':
            c = request.POST
            try:
                orders = list(Order.get_all_by_user_id(request.POST['users']))
                return render(request, 'order/del_order.html', {'form0': form0,
                                                                'form1': form1,
                                                                'orders': orders})
            except:
                Order.delete_by_id(order_id=request.POST['order'])
                return render(request, 'order/del_order.html', {'form0': form0})

        return render(request, 'order/del_order.html', {'form0': form0})
