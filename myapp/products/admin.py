# admin.py
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_url')  # เลือกฟิลด์ที่ต้องการแสดงในรายการ
    search_fields = ('name',)  # ทำให้สามารถค้นหาสินค้าตามชื่อได้
