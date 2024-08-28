from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm,PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib import messages
from django.contrib.auth.models import User
from core.models import Product


# Create your views here.
def orders(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        order = Order.objects.get(id=pk)
        order_items = OrderItem.objects.filter(order=pk)
        return render(request, "orders.html", {"order":order, "order_items":order_items})
    else:
        messages.success(request, "Access Denied")
        return redirect("index")


def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=False)
        return render(request, "not_shipped_dash.html", {"orders":orders})
    else:
        messages.success(request, "Access Denied")
        return redirect("index")



def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        orders = Order.objects.filter(shipped=True)
        return render(request, "shipped_dash.html", {"orders":orders})
    else:
        messages.success(request, "Access Denied!!!")
        return redirect("index")




def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prod
        quantities = cart.get_quants
        totals = cart.cart_total()
        payment_form = PaymentForm(request.POST or None)
        my_shipping = request.session.get('my_shipping')
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        
        full_name = my_shipping['shipping_full_name']
        email = my_shipping['shipping_email']
        amount_paid = totals
        if request.user.is_authenticated:
            user = request.user
            create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            order_id = create_order.pk

            for product in cart_products():
                product_id = product.id
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for k,v in quantities().items():
                    if int(k) == product.id:
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=v, price=price, user=user)
                        create_order_item.save()

            for key in list(request.session.keys()):
                if key == "session_key":
                    del request.session[key]

            messages.success(request, "Order Placed!!!")
            return redirect("index")

        else:
            create_order = Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
            create_order.save()
            for product in cart_products():
                product_id = product.id
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for k,v in quantities().items():
                    if int(k) == product.id:
                        create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=v, price=price)
                        create_order_item.save()
            
            for key in list(request.session.keys()):
                if key == "session_key":
                    del request.session[key]
            messages.success(request, "Order Placed!!!")
            return redirect("index")

    else:
        messages.success(request, "Access Denied")
        return redirect("index")


def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prod
        quantities = cart.get_quants
        totals = cart.cart_total()
        my_shipping = request.POST
        request.session['my_shipping'] = my_shipping
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
            billing_form = PaymentForm()
            shipping_form = ShippingForm(request.POST or None)
            return render(request, "billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":request.POST, "billing_form":billing_form})
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
    