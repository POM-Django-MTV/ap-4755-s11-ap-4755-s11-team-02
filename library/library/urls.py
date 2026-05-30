from django.contrib import admin
from django.urls import path


from order.views import order_page
from user.views import user_page

urlpatterns = [
    path('admin/', admin.site.urls),

    # Ваші маршрути
    path('order/', order_page, name='order_page'),
    path('user/', user_page, name='user_page'),
]