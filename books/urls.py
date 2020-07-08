from django.urls import path,include
from . import views
from django.urls import reverse


urlpatterns = [
    path('', views.books, name= 'shop'),
    path('allbooks/', views.allbooks, name= 'books'),
    path('alljournals/', views.alljournals, name= 'journals'),
    path('allmagazines/', views.allmagazines, name= 'magazines'),
    path("<int:product_id>",views.productsingle),
    path('alljournals/<int:product_id>', views.productsingle),
    path('allbooks/<int:product_id>', views.productsingle),
    path('allmagazines/<int:product_id>', views.productsingle),
    path("<int:product_id>/addtocart",views.addtocart,name='addtocart'),
    path("cart/",views.cart, name = 'cartname'),
    path("allbooks/<int:product_id>/addtocart",views.addtocart,name='addtocart'),
    path("alljournals/<int:product_id>/addtocart",views.addtocart,name='addtocart'),
    path("allmagazines/<int:product_id>/addtocart",views.addtocart,name='addtocart'),
    path("search",views.search,name='search'),
    path("checkout/",views.checkout,name='checkout'),
    path('cart/<int:product_id>/removeitem', views.removeitem, name='removeitem'),
]
