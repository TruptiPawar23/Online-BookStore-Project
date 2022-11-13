#from django.shortcuts import render, redirect, get_object_or_404
#from ..models import Category, Writer, Book
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Sum
from django.utils.safestring import mark_safe
from django import template
register = template.Library()

shippingConst = 100


@register.filter(name='text_short')
def text_short(value):
	temp = value[0:50]
	return temp

@register.filter(name='shipping')
def shipping(value):
	return shippingConst
	
@register.filter(name='payabletotal')
def  payabletotal(value):
	return value+shippingConst


@register.filter(name='averagerating')
def averagerating(value, args):
	temp = value / args
	if int(temp + 0.5) > int(temp):
		temp = int(temp + 0.5)
	else:
		temp = int(temp)

	if temp > 5:
		temp = 5
		
	if temp == 1:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span>"
	elif temp == 2:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span>"
	elif temp == 3:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star'></span> <span class='fa fa-star'></span>"
	elif temp == 4:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star'></span>"
	else:
		temp1 = "<span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span> <span class='fa fa-star checked'></span>"

	return mark_safe(temp1)

@register.filter(name='subtotal')
def subtotal(value, args):
	return value*args
