from django.urls import path, include
from my_app import views


# Syantax for writing class based view as views
'''
Url patterns contains a nice swagger documentation. Swagger can be accessed through the
first link. If you want to download the schemas json you can download it with
localhost:800/api/v1/swagger.json
'''

urlpatterns = [
    # Swagger API Documentation
    path('', include('my_app.swagger_urls')),

    # These both urls have been cached
    path('customer_info/', views.customer_cache, name='customer_cache'),
    path('product_info/', views.product_cache, name='product_cache'),
    # This is the default template without any rendering.
    path('cart_info/', views.cart_page, name='cart_page'),

    # URL's For crud operation

    # This is for crud of customer, Pk is the primary key
    path('customer/', views.customer_list, name='customers'),
    path('customer/<pk>/', views.customer_detail, name='customer'),
    # This is for crud of product, Pk is the primary key
    path('product/', views.product_list, name='products'),
    path('product/<pk>/', views.product_detail, name='product'),
    # This is for crud of customer, Pk is the primary key
    path('cart/', views.cart_list, name='carts'),
    path('cart/<pk>/', views.cart_detail, name='cart'),
]
