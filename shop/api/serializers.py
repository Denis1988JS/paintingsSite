from rest_framework import serializers

from cart.cart import Cart
from shoppainting.models import Painting,Employee,BuyerUser

from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

#Список всех картин
class PaintingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['name','slug','autor','year','price','formPaint','countryPaint','imagePainting']

#Детализация выбранной картины
class PaintingDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = ['name', 'slug', 'autor', 'year', 'price', 'formPaint', 'countryPaint', 'imagePainting']

#Список сотрудников - общий весь
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name', 'slug', 'second_name', 'thirt_name', 'phone_number', 'employee_avatar', 'employee_content', 'JobTitle']

# #Модель данных
# class NewModel:
#     def __init__(self, username, password1,first_name,last_name,email,user_avatar,phone_number):
#         self.username = username
#         self.password1 = password1
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.user_avatar = user_avatar
#         self.phone_number = phone_number

#Пользователи - покупатели BuyerUser для регистрации
class BuyerUserSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField(required=True)
    user_avatar = serializers.ImageField(required=True)
    is_active = serializers.BooleanField(default=True)
    phone_number = serializers.CharField(max_length=20)

# def encode():#кодирование через сериолайзер информации в JSON строку
#     model = NewModel
#     model_sr = BuyerUserSerializers(model)
#     print(model_sr.data, type(model_sr))
#     json = JSONRenderer().render(model_sr.data)

#Корзина покупок
class CartSerializers(serializers.Serializer):
        model = Cart
        fields = ['quantity', 'price', 'id', 'painting', 'imagePainting', 'phone_number', 'total_price']
