class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())
