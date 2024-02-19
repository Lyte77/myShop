from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'myStore\home.html' )


def product_view(request):
    return render(request,'myStore\product.html' )
