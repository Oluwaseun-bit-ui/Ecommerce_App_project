from rest_framework import generics, permissions
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse

# List all products / Create new product
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Retrieve a single product by ID
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Optional: a simple test view
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def hello_products(request):
    return Response({"message": "Hello Products API is working!"})


def home(request):
    return JsonResponse({"message": "Welcome to Ecommerce API 🚀"})

def health_check(request):
    return JsonResponse({"status": "ok", "message": "API is running 🚀"})