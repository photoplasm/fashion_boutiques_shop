from django.db import models
from django.core.exceptions import ValidationError
from django.db.models import Avg 
from django.contrib.auth.models import User
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default='No description provided.')  # Default description
    material = models.CharField(max_length=255, default='Unknown')  # Default material
    dimensions = models.CharField(max_length=100, default='Not specified')  # Default dimensions
    color = models.CharField(max_length=50, default='White')  # Default value is "White"
    image_url = models.URLField()  # Image URL of the product
    stock = models.PositiveIntegerField(default=0)  # เพิ่มฟิลด์นี้
    
    def average_rating(self):
        reviews = self.reviews.all()  # ดึงรีวิวทั้งหมดของผลิตภัณฑ์
        if reviews.exists():
            return reviews.aggregate(Avg('rating'))['rating__avg']  # คำนวณคะแนนเฉลี่ย
        return 0  # ถ้าไม่มีรีวิว คืนค่าเป็น 0
    def __str__(self):
        return self.name
    
def validate_rating(value):
    if value < 1 or value > 5:
        raise ValidationError('Rating must be between 1 and 5.')
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.rating} stars"
    

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField('Product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"รายการโปรดของ {self.user.username}"