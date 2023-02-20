from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.OrderDetail)


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('users/all/', views.show_all_users, name='users'),
    path('users/', views.role_of_user, name='specific_user'),
    path('', views.main, name='main'),
    path('api/v1/user/<int:user_id>/order/', include(router.urls)),

]
