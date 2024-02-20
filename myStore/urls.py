from django.urls import path
from .views import home_view,product_view,contact_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:pk>/', product_view, name='products'),
    path('contact/', contact_view, name='contact',)

]