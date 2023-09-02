from .models import *
from cart.forms import CartAddProductForm
class DataMixin:

    def get_user_context(self,**kwargs):
        context = kwargs
        artist = Employee.objects.filter(JobTitle__id=1)
        country = CountryPainting.objects.all()
        france =  CountryPainting.objects.get(id=1)
        context['artist'] = artist
        context['countyList'] = country
        context['france'] = france
        context['cart_product_form'] = CartAddProductForm()
        return context