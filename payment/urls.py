from .views import payment_success, checkout
from django.urls import path


urlpatterns = [
    path('payment_success', payment_success, name="payment_success"),
    path('checkout', checkout, name="checkout"),
]