from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import library_item,magazine,journal,book_collection,author,Publisher,PersonExtend


cart_items=[]
cartlist=[]
sliplist=[]
# Create your views here.
@login_required(login_url='login')
def books(request):
    libraryitem = library_item.objects
    return render(request, 'books/books.html', {'libraryitem': libraryitem})

@login_required(login_url='login')
def allbooks(request):
    libraryitem1 = library_item.objects
    return render(request, 'books/allbooks.html', {'libraryitem1': libraryitem1})

@login_required(login_url='login')
def alljournals(request):
    libraryitem2 = library_item.objects
    return render(request, 'books/alljournals.html', {'libraryitem2': libraryitem2})

@login_required(login_url='login')
def allmagazines(request):
    libraryitem3 = library_item.objects
    return render(request, 'books/allmagazines.html', {'libraryitem3': libraryitem3})


@login_required(login_url='login')
def productsingle(request,product_id):
	product=get_object_or_404(library_item,pk=product_id)
	return render(request,'product-single.html',{'product':product, 'cartnum':len(cart_items)})

@login_required(login_url='login')
def addtocart(request,product_id):
    product=get_object_or_404(library_item,pk=product_id)
    if product.library_Id not in cart_items:
        cart_items.append(product_id)
        return redirect('/books/' + str(product_id),{'cartnum':len(cart_items)})
    else:
        return redirect('/books/' + str(product_id),{'cartnum':len(cart_items)})




@login_required(login_url='login')
def cart(request):
    cartlist.clear()
    a=0
    for item in cart_items:
        a=a+1
        cartlist.append(get_object_or_404(library_item,pk=item))
    return render(request,'cart.html',{'cartitems':cartlist})


@login_required(login_url='login')
def removeitem(request,product_id):
	product=get_object_or_404(library_item,pk=product_id)
	cart_items.remove(product_id)
	item = library_item.objects.get(library_Id=product_id)
	cartlist.remove(item)
	return redirect('/books/cart/',{'cartitems':cartlist})


@login_required(login_url='login')
def search(request):
	searchitem=request.GET['searchitem']
	search_items=library_item.objects.filter(title__icontains=searchitem)
	return render(request,'searchresult.html', {'libraryitem1': search_items})


@login_required(login_url='login')
def checkout(request):
    personinfo = PersonExtend.objects.filter(user= request.user)
    noitems=[]
    heading='ITEMS NOT AVAILABLE'

    for item in cart_items:
        zerocopy = library_item.objects.get(library_Id=item)
        if zerocopy.copies==0:
        	noitems.append(zerocopy)

    for a in cartlist:
        for b in noitems:
            if a==b:
                cartlist.remove(a)
    sliplist=cartlist
    if noitems:
    	return render(request, 'cart.html', {'notavailable': noitems, 'heading' : heading, 'cartitems':cartlist})

    return render(request,'Slip.html',{'sliplist': sliplist, 'personinfo': personinfo})
