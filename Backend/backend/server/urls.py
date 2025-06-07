from django.urls import path
from . import views

urlpatterns = [
    path("server",views.server_status, name="server_status"),
    path('categories/', views.get_categories, name='get_categories'),
    path('categories/<int:pk>/', views.category_detail, name='api_category_detail'),
    path('products/', views.get_products, name='get_products'),
    path('products/<int:pk>/', views.product_detail, name='api_product_detail'),
    path('suppliers/', views.get_suppliers, name='get_suppliers'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='api_supplier_detail'),
    path('payments/', views.get_payments, name='get_payments'),
    path('payments/<int:pk>/', views.payment_detail, name='api_payment_detail'),
    # path('payments/<int:pk>/product/', views.payment_product_detail, name='api_payment_product_detail'),
]