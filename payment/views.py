from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm,PaymentForm
from payment.models import ShippingAddress
from django.contrib import messages

# Create your views here.
def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prod
        quantities = cart.get_quants
        totals = cart.cart_total()

        if request.user.is_authenticated:
            billing_form = PaymentForm()
            shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
            shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
            return render(request, "billing_info.html", {"cart_products":cart_products,
             "quantities":quantities,
              "totals":totals,
               "shipping_form":request.POST,
               "billing_form":billing_form
               })
        else:
            shipping_form = ShippingForm(request.POST or None)
            return render(request, "billing_info.html", {"cart_products":cart_products,
             "quantities":quantities,
              "totals":totals,
               "shipping_form":request.POST,
               "billing_form":billing_form})
    else:
        billing_form = PaymentForm()
        messages.success(request, "Access Denied")
        return redirect("index")    

def payment_success(request):
    return render(request, "payment_success.html", {})


def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prod
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    else:
        shipping_form = ShippingForm(request.POST or None)
        return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
    