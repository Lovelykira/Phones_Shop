from django.contrib import admin
from django.db.models import Sum, F


from .models import *


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdmin,)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdmin,)
    list_display = ('display_name', 'date',)

    def display_name(self, obj):
        return "{} {}".format(obj.client_id.name, obj.client_id.surname)

    def display_sum(self, obj):
        obj_id = obj.id
        price_sum = OrderItem.objects.filter(order_id = obj.id).aggregate(Sum('total_cost'))
        return "{}".format(price_sum['price__sum'])


class ClientAdmin(admin.ModelAdmin):
    list_display = ('display',)

    def display(self, obj):
        return "{} {}".format(obj.name, obj.surname)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name','site')


class PhoneModelAdmin(admin.ModelAdmin):
    pass


#admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(PhoneModel, PhoneModelAdmin)