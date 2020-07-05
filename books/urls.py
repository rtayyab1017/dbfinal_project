from django.urls import path
from . import views


urlpatterns = [
    path('', views.books, name= 'shop'),
    path('allbooks/', views.allbooks, name= 'books'),
    path('alljournals/', views.alljournals, name= 'journals'),
    path("<int:product_id>",views.productsingle),
    path('alljournals/<int:product_id>', views.productsingle),
    path('allbooks/<int:product_id>', views.productsingle),
    path("<int:product_id>/addtocart",views.addtocart,name='addtocart'),
    path("cart/",views.cart, name = 'cartname'),
    path("allbooks/<int:product_id>/addtocart",views.addtocart,name='addtocart'),
    path("search",views.search,name='search'),
]
