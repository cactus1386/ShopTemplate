from django.core.management.base import BaseCommand
from faker import Faker
from shop.models import ProductCategory
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Generate fake product categories'

    def handle(self, *args, **kwargs):
        fake = Faker(locale='fa_IR')
        for _ in range(10):
            title = fake.word()
            slug = slugify(title, allow_unicode=True)
            ProductCategory.objects.get_or_create(title=title, slug=slug)
        self.stdout.write(self.style.SUCCESS(
            'Successfully generated fake product categories'))
