from .views import payment_success
from django.urls import path


urlpatterns = [
    path('payment_success', payment_success, name="payment_success"),
]