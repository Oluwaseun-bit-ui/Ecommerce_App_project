from rest_framework import generics, permissions
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/products/categories/   -> List all categories
    POST /api/products/categories/   -> Create a new category (auth required)
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/products/categories/<id>/   -> Retrieve category
    PUT    /api/products/categories/<id>/   -> Update category (auth required)
    PATCH  /api/products/categories/<id>/   -> Partial update (auth required)
    DELETE /api/products/categories/<id>/   -> Delete category (auth required)
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductListCreateView(generics.ListCreateAPIView):
    """
    GET  /api/products/    -> List all products
    POST /api/products/    -> Create a new product (auth required)
    """
    queryset = Product.objects.all().order_by("-created_at")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/products/<id>/   -> Retrieve a product
    PUT    /api/products/<id>/   -> Update product (auth required)
    PATCH  /api/products/<id>/   -> Partial update (auth required)
    DELETE /api/products/<id>/   -> Delete product (auth required)
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
