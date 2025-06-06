from django.shortcuts import render
from store.models import Product
def home(request):
    return  render (request,'home.html')

def store(request):
    products = Product.objects.all().filter(is_available=True)

   
    context = {
        "products":products,
    }
    
    return  render (request,'home.html',context)
