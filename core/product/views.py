from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.


def product(request):
    product = Product.objects.all().values()
    template = loader.get_template('')
    return HttpResponse(template.render())
