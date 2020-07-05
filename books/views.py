from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import library_item,magazine,journal,book_collection,author,Publisher,Borrower,Borrows


cart_items=[]
# Create your views here.
def books(request):
    libraryitem = library_item.objects
    return render(request, 'books/books.html', {'libraryitem': libraryitem})

def allbooks(request):
    libraryitem1 = library_item.objects
    return render(request, 'books/allbooks.html', {'libraryitem1': libraryitem1})

def alljournals(request):
    libraryitem2 = library_item.objects
    return render(request, 'books/alljournals.html', {'libraryitem2': libraryitem2})

def productsingle(request,product_id):
	product=get_object_or_404(library_item,pk=product_id)
	return render(request,'product-single.html',{'product':product, 'cartnum':len(cart_items)})

def addtocart(request,product_id):
	product=get_object_or_404(library_item,pk=product_id)
	cart_items.append(product_id)
	return redirect('/books/' + str(product_id),{'cartnum':len(cart_items)})


def cart(request):
	a=0
	cartlist=[]
	for item in cart_items:
		a=a+1
		cartlist.append(get_object_or_404(library_item,pk=item))

	return render(request,'cart.html',{'cartitems':cartlist})



def search(request):
	searchitem=request.GET['searchitem']
	
	search_items=library_item.objects.filter(title__icontains=searchitem)
	return render(request,'allbooks.html', {'libraryitem1': search_items})