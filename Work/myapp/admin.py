from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(User_Profile)
admin.site.register(Income)
admin.site.register(Outcome)
admin.site.register(Payment)
admin.site.register(Type_of_payment)