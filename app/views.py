from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Category, Products
from .serializers import CategorySerializer, ProductsSerializer

class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many =True)
        
        return Response({'description': serializer.data})


class ProductView(APIView):
    def get(self, request):
        product = Products.objects.all()
        serializer = ProductsSerializer(product, many =True)
        return Response({'product_cart': serializer.data})