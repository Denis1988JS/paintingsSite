from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import CartAddProductForm
from shop import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from shoppainting.models import *
# Create your views here.
from django.contrib.sessions.backends.db import SessionStore
#Корзина покупок
def cart(request):
    title = 'Корзина пользователя'
    france = CountryPainting.objects.get(id=1)
    countyList = CountryPainting.objects.all()
    cart = Cart(request)
    print(cart)
    for i in cart:
        print(i)
    data = {'title':title,'france':france,'cart':cart,'countyList':countyList}
    return render(request,'cart/cart.html', context=data)

#Добавление товара в корзину
@require_POST
def add_cart(request, paint_id):
    cart = Cart(request)
    painting = get_object_or_404(Painting, id=paint_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(painting=painting,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
        print(f'{painting} добавлен в кол-ве {cd["quantity"]}')
    return redirect('cart')

#Удаление товара из корзины
def cart_remove(request, paint_id):
    cart = Cart(request)
    painting = get_object_or_404(Painting, id=paint_id)
    cart.remove(painting)
    return redirect('cart')

