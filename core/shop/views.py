from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, ProductStatus

# Create your views here.


class ProductListView(ListView):
    template_name = 'shop/product-list.html'
    queryset = Product.objects.filter(status=ProductStatus.publish.value)
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_items'] = self.get_queryset().count()

        return context


class ProductDetailView(DetailView):
    template_name = 'shop/product-detail.html'
    queryset = Product.objects.filter(status=ProductStatus.publish.value)
