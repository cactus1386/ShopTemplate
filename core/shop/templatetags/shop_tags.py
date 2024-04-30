from django import template
from ..models import Product, ProductStatus

register = template.Library()


@register.inclusion_tag('includes/lastest-products.html')
def show_last_product():
    last_products = Product.objects.filter(
        status=ProductStatus.publish.value).order_by('-created_at')[:4]
    return {'last_products': last_products}


@register.inclusion_tag('includes/similar-products.html')
def show_similar_product(product):
    all_categories = product.category.all()
    similar_products = Product.objects.filter(
        status=ProductStatus.publish.value, category__in=all_categories).order_by('-created_at')[:4]
    return {'similar_products': similar_products}
