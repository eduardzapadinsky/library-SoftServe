"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication import views as views_u
from book import views as views_b
from order import views as views_o
from author import views as views_a
from rest_framework import routers


router = routers.DefaultRouter()
router.register("order", views_o.OrderView)
router.register("book", views_b.BookView)
router.register("author", views_a.AuthorView)
router.register("user", views_u.UserView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls', 'book')),
    path('authentication/', include(('authentication.urls', 'authentication'),
                                    namespace='authentication')),
    path('author/', include(('author.urls', 'author'), namespace='author')),
    path('order/', include(('order.urls', 'order'), namespace="order")),
    path('', include(('authentication.urls', 'main_page'),
                     namespace='main_page')),
    path('api/v1/', include(router.urls)),

]
