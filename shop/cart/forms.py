from django import forms

class CartAddProductForm(forms.Form):
    quantity = forms.CharField(empty_value=1, widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

