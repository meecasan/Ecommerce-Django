from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User

# register the model on the main second thing
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

#create an OrderItem inline 
class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    extra = 0 

# extend our order model 
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_ordered"]
    fields = ["user", "full_name", "email", "shipping_address", "amount_paid", "date_ordered", "shipped", "date_shipped"]
    inlines = [OrderItemInLine]

# unregister order model 
admin.site.unregister(Order)

#Re-register our Order and OrderAdmin
admin.site.register(Order, OrderAdmin)
