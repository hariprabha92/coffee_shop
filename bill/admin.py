from django.contrib import admin
from .models import Order,Order_detail
class OrderAdmin(admin.ModelAdmin):
    list_display = ("bill_id", "total_amount", "date")

admin.site.register(Order)
admin.site.register(Order_detail)

