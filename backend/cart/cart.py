from decimal import Decimal

from backend.shop.models import Product


class Cart:
    """Class processing main cart methods"""

    def __init__(self, session):
        """
        Initialize a cart
        """
        self.session = session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        """
        product_ids: [] = self.cart.keys()
        products = Product.query.filter(Product.id.in_(product_ids))

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart
        :return: int
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add product to the cart or update its quantity
        :param product: Product instance
        :param quantity: int
        :param override_quantity: bool
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        :param product: Product instance
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        # remove cart from the session
        del self.session['cart']
        self.save()

    def get_total_price(self):
        """
        Return total cost of the cart
        :return: Decimal
        """
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
