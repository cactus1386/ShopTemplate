from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, ProductStatus

# Create your views here.


class ProductListView(ListView):
    template_name = 'shop/product-list.html'
    queryset = Product.objects.filter(status=ProductStatus.publish.value)
