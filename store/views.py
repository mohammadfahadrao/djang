import pdb
from django.shortcuts import render

from store.models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request,'store/index.html',{'products': products})