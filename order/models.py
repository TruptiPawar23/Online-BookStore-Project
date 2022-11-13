from django.db import models
from store.models import Book
from django.contrib.auth.models import User


class Order(models.Model):
	customer = models.ForeignKey(User, on_delete = models.CASCADE)
	name = models.CharField(max_length=30)
	email = models.EmailField()
	phone = models.CharField(max_length=10)
	address = models.CharField(max_length=150)
	division = models.CharField(max_length=20)
	district = models.CharField(max_length=30)
	zip_code = models.CharField(max_length = 6)
	payment_method = models.CharField(max_length = 20)
	account_no = models.CharField(max_length = 12)
	transaction_id = models.IntegerField()
	payable = models.IntegerField()
	totalbook = models.IntegerField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created', )

	def __str__(self):
		return 'Order {}'.format(self.id)

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
