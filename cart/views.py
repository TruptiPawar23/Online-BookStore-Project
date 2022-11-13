from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Book, Category
from .cart import Cart

def cart_add(request, bookid):
	cart = Cart(request)  
	book = get_object_or_404(Book, id=bookid) 
	cart.add(book=book)

	return redirect('store:index')

def cart_update(request, bookid, quantity):
	cart = Cart(request) 
	book = get_object_or_404(Book, id=bookid) 
	cart.update(book=book, quantity=quantity)
	price = (book.price*quantity)

	return render(request, 'cart/price.html', {"price":price})

def cart_remove(request, bookid):
    cart = Cart(request)
    book = get_object_or_404(Book, id=bookid)
    cart.remove(book)
    return redirect('cart:cart_details')

def total_cart(request):
	return render(request, 'cart/totalcart.html')

def cart_summary(request):

	return render(request, 'cart/summary.html')

def cart_details(request):
	cart = Cart(request)
	context = {
		"cart": cart,
	}
	return render(request, 'cart/cart.html', context)

