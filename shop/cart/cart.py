from decimal import Decimal
from django.conf import settings
from shoppainting.models import Painting #(Product)

#Класс корзина
class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    #Добавление товара в корзину
    def add(self,painting, quantity=1, update_quantity = False ):
        painting_id = str(painting.id)
        if painting_id not in self.cart:
            self.cart[painting_id] = {'quantity':1,'price':str(painting.price)}
        elif painting_id in self.cart:
            self.cart[painting_id]['quantity'] +=1
        self.save()
    #Удаление товара из корзины
    def remove(self, painting):
        painting_id = str(painting.id)
        if painting_id in self.cart:
            del self.cart[painting_id]
        self.save()
    #Сохранение корзины
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
    #Перебор товаров в корзине
    def __iter__(self):
        painting_cart = self.cart.keys()
        paintings = Painting.objects.filter(id__in=painting_cart)
        for painting in paintings:
            self.cart[str(painting.id)]['id'] = painting.id
            self.cart[str(painting.id)]['painting'] = painting
            self.cart[str(painting.id)]['imagePainting'] = painting.imagePainting
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    #Кол-во товаров в корзине
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    #Общая сумма
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in
                   self.cart.values())
    # Общая сумма
    def get_total_len(self):
        count = 0
        for item in self.cart.values():
            print(item['quantity'])
            count +=int(item['quantity'])
        return count
    # удаление корзины из сессии
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True