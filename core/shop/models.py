from django.db import models
from decimal import Decimal
# Create your models here.


class ProductStatus(models.IntegerChoices):
    publish = 1, ("فعال")
    draft = 2, ("غیر فعال")


class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.PROTECT)
    category = models.ManyToManyField(ProductCategory)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode=True)
    image = models.ImageField(
        default='/defult/product-image.png', upload_to='product/img/')
    description = models.TextField()
    stock = models.PositiveIntegerField(default=0)
    price = models.DecimalField(default=True, max_digits=10, decimal_places=0)
    status = models.IntegerField(
        choices=ProductStatus.choices, default=ProductStatus.draft.value)
    discount = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_price(self):
        final_price = self.price - (self.price * Decimal(self.discount / 100))
        return '{:,}'.format(round(final_price))


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file = models.ImageField(upload_to='product/img/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
