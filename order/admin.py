from django.contrib import admin
from .models import Order, OrderItem

class OrderItemList(admin.TabularInline):
	model = OrderItem
	extra = 0

class OrderList(admin.ModelAdmin):
	list_display = ['id','name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method', 'account_no', 'totalbook', 'created', 'updated', 'paid']
	list_filter = ['paid']
	exclude = ['name', 'email', 'phone']
	inlines = [OrderItemList]
	class Meta:
		Model = Order

admin.site.register(Order, OrderList)