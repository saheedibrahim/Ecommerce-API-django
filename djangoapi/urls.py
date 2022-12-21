from django.urls  import path
from .views import ListBook, DetailBook, ListCategory, DetailCategory, ListProduct, DetailProduct

urlpatterns = [
    path('categories/', ListCategory.as_view(), name="categories"),
    path('categories/<int:pk>/', DetailCategory.as_view(), name="singlecategory"),
    path('books/', ListBook.as_view(), name="books"),
    path('books/<int:pk>/', DetailBook.as_view(), name="singlebook"),
    path('product/', ListProduct.as_view(), name="products"),
    path('products/<int:pk>/', DetailProduct.as_view(), name="singleproduct")
]