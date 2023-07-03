from django.contrib import admin

from .models import Recipt, Budget
    # Category, Product
# Register your models here.


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ["id", "name"]


@admin.register(Recipt)
class ReciptAdmin(admin.ModelAdmin):
    list_display = ["id","device_id", "store", "amount", "address"]
    # list_display = ["id", "device_id", "category", "store", "amount", "address", "year", "month"]

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ["id", "device_id", "living_expenses"]

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ["id", "recipt", "name", "price", "amount"]
