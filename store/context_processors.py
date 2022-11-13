from django.shortcuts import render
from .models import Category
from cart.cart import Cart

def sidebar(request):
	categories = Category.objects.all()
	context = {
		"cat":categories
	}
	return context


def cart(request):
	cart = Cart(request)
	context = {
		"cart": cart
	}
	return context


	