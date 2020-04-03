from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
# /products -> index
# Map a URL (uniform resource locator)


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def new_end_point(request):
    return HttpResponse("You are in the NEW page - under construction!")


