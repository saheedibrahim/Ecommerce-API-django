from rest_framework import serializers
from .models import Category, Book, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'category', 'isbn', 'pages', 'price', 'stock', 'description', 'iamgeURL', 'status', 'date_created')
        model = Book

class ProductSerializer(serializers.ModelSerializer):
    fields = ('id', 'product_tag', 'category', 'name', 'price', 'stock', 'description', 'iamgeURL', 'status', 'date_created')
    model = Product
