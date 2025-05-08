"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from base.views.products_view import get_all_sneakers, get_sneaker_by_id
from base.views.orders_view import get_orders_by_user, delete_order, delete_order_item, update_order, create_order

urlpatterns = [
    # Маршруты для кроссовок
    path('sneakers/', get_all_sneakers, name='get_all_sneakers'),
    path('sneakers/<int:pk>/', get_sneaker_by_id, name='get_sneaker_by_id'),
    # Маршруты для заказов
    path('sneakers/orders/<int:user_id>/', get_orders_by_user, name='get_orders_by_user'),
    path('sneakers/orders/delete/<int:cart_id>/', delete_order, name='delete_order'),  # Новый путь
    path('sneakers/orders/<int:cart_id>/items/<int:item_id>/', delete_order_item, name='delete_order_item'),
    path('sneakers/orders/<int:cart_id>/update/', update_order, name='update_order'),
    path('sneakers/orders/create/', create_order, name='create_order'),
]
