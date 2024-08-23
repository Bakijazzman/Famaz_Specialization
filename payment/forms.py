from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Full Name (**required**)'}), required=True)
    shipping_email = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Email (**required**)'}), required=True)
    shipping_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Address1 (**required**)'}), required=True)
    shipping_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Address2 (**required**)'}), required=False)
    shipping_city = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'City (**required**)'}), required=True)
    shipping_state = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'State (**required**)'}), required=False)
    shipping_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Zipcode (**required**)'}), required=False)
    shipping_country =forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Country (**required**)'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ["shipping_full_name",
                  "shipping_email",
                  "shipping_address1",
                  "shipping_address2",
                  "shipping_city",
                  "shipping_state",
                  "shipping_zipcode",
                  "shipping_country",
                  ]
        exclude = ["user",]


class PaymentForm(forms.Form):
    card_name = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Card Name (**required**)'}), required=True)
    card_number = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Card Number (**required**)'}), required=True)
    card_exp_date = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Card Expiration Date (**required**)'}), required=True)
    card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'CVV Number (**required**)'}), required=True)
    card_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Billing Address1 (**required**)'}), required=True)
    card_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Billing Address2 (**required**)'}), required=False)
    card_city = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Billing City (**required**)'}), required=True)
    card_state = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Billing State (**required**)'}), required=True)
    card_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Billing Zipcode(**required**)'}), required=True)
    card_country = forms.CharField(label="", widget=forms.TextInput(attrs={"class": 'form-control', 'placeholder': 'Billing Country (**required**)'}), required=True)