from django import forms
from .models import Product, Wishlist
from .models import Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'material', 'dimensions', 'color', 'image_url']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']

    rating = forms.ChoiceField(choices=[
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ])
    comment = forms.CharField(widget=forms.Textarea, max_length=500, required=True)

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['products']  # เลือกเฉพาะสินค้าที่จะเพิ่มลงใน Wishlist