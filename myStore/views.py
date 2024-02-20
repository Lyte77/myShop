from django.shortcuts import render, get_object_or_404
from myStore.models import Categories, Products

# Create your views here.
def home_view(request):
    products = Products.objects.filter(is_sold=False)[0:6]
    categories = Categories.objects.all()
    return render(request,'myStore\home.html',{
        'categories': categories,
        'products': products, 
    } )


def product_view(request, pk):
    product = get_object_or_404(Products, pk=pk)
    related_item = Products.objects.filter(categories=product.categories,is_sold=False).exclude(pk=pk)[0:3]


    return render(request,'myStore\product.html', {
        'product' : product,
        'related_item':related_item,
    })

def contact_view(request):
    return render(request, 'myStore\contact.html')
