from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.show_all_orders, name='orders'),
    path('own/', views.show_own_orders, name='order'),
    path('create/', views.create_an_order, name='new_order'),
    path('del/', views.del_order_by_root, name='del_order'),
]