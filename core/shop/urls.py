from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('product/list/', views.ProductListView.as_view(), name='product-list'),
    path('product/<slug:slug>/detail/',
         views.ProductDetailView.as_view(), name='product-detail'),
]
