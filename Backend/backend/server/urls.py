from django.urls import path
from . import views

urlpatterns = [
    path("server",views.server_status, name="server_status"),
    path('categories/', views.get_categories, name='get_categories'),
    path('categories/<int:pk>/', views.category_detail, name='api_category_detail'),
    path('products/', views.get_products, name='get_products'),
    path('products/<int:pk>/', views.product_detail, name='api_product_detail'),
]