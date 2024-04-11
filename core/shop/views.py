from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Product, ProductStatus, ProductCategory

# Create your views here.


class ProductListView(ListView):
    template_name = 'shop/product-list.html'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.filter(status=ProductStatus.publish.value)
        search_q = self.request.GET.get('q')
        category_id = self.request.GET.get('category_id')
        if search_q:
            queryset = queryset.filter(title__icontains=search_q)

        if category_id:
            queryset = queryset.filter(category__id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_items'] = self.get_queryset().count()
        context['categories'] = ProductCategory.objects.all()

        return context


class ProductDetailView(DetailView):
    template_name = 'shop/product-detail.html'
    queryset = Product.objects.filter(status=ProductStatus.publish.value)
