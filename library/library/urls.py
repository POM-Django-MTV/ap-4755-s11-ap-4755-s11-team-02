from django.contrib import admin
from django.urls import path, include

# Імпортуємо views ваших додатків
from order.views import order_page
from user.views import user_page

urlpatterns = [

    # Ваші маршрути
    path('order/', order_page, name='order_page'),
    path('user/', user_page, name='user_page'),
    path('book/', include('book.urls')),
    path('author/', include('author.urls')),
]