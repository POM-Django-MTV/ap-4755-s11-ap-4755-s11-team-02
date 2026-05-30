from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def order_page(request):
    return render(request, 'order/order_page.html')
