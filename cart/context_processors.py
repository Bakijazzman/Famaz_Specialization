from .cart import Cart

# create context processor so Cart can work on all pages
def cart(request):
    # Return default data from our cart
    return {'cart': Cart(request)}