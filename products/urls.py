from django.urls import path
from .views import ProductListCreateView, ProductDetailView, hello_products
from .views import health_check

urlpatterns = [
    path('', hello_products, name="hello_products"),  # test endpoint
    path('products/', ProductListCreateView.as_view(), name="product-list-create"),
    path('products/<int:pk>/', ProductDetailView.as_view(), name="product-detail"),
    path('health/', health_check, name='health-check'),
]
