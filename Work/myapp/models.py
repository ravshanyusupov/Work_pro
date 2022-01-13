from django.db import models

# Create your models here.
from django.urls import reverse


class Product(models.Model):
    choises = (
        ('День', 'День'),
        ('Час', 'Час')
    )
    name = models.CharField(max_length=255)
    weight = models.IntegerField()
    quantity = models.IntegerField()
    origin_prize = models.DecimalField(max_digits=6, decimal_places=3)
    second_prize = models.DecimalField(max_digits=6, decimal_places=3)
    product_prize = models.DecimalField(max_digits=6, decimal_places=3)
    type = models.CharField(max_length=200, default='День', choices=choises)
    created_time = models.DateField(auto_now_add=True, blank=True, null=True)
    update_time = models.DateField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_quantity(self):
        quantity = self.quantity + sum([i.quantity for i in self.income.all()]) - sum([i.quantity for i in self.outcome.all()])
        return quantity

    def get_order_total(self):
        total = sum([i.quantity for i in self.lesa.all()])
        return total

    def get_total(self):
        total = self.get_order_total()
        sub_total = self.get_quantity() - total
        return sub_total


class User_Profile(models.Model):
    name = models.CharField(max_length=200)
    seria = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    debt = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_debt(self):
        order = sum([i.get_order() for i in self.customer.all()]) - sum([i.prize for i in self.customer_pay.all()])
        return order

    def get_paid_info(self):
        paid = False
        if self.get_debt() == 0:
            paid = True
        else:
            return paid
        return paid


class Order(models.Model):
    user_profile_id = models.ForeignKey(User_Profile, on_delete=models.CASCADE, related_name='customer', blank=True, null=True)
    deadline = models.IntegerField(blank=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lesa', blank=True, null=True)
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return str(f'{self.product_id} {self.user_profile_id}')

    def get_order_sum(self):
        total = sum(self.quantity)
        return total

    def get_order(self):
        sub_total = self.product_id.origin_prize
        total = self.quantity * sub_total
        return total

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})


class Income(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='income')
    date = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product_id)

    def overall(self):
        all = self.product_id.product_prize * self.quantity
        return all


class Outcome(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='outcome')
    quantity = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.product_id)

    def sum(self):
        all = self.quantity * self.product_id.product_prize
        return all


class Payment(models.Model):
    user_profile_id = models.ForeignKey(User_Profile, related_name='customer_pay', on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    method_id = models.ForeignKey('Type_of_payment', on_delete=models.CASCADE, related_name='payment')
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    prize = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return str(self.user_profile_id)


class Type_of_payment(models.Model):
    method = models.CharField(max_length=255)

    def __str__(self):
        return self.method

    def payment_all(self):
        total = sum([i.prize for i in self.payment.all()])
        return total
