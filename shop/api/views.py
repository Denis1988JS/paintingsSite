from django.shortcuts import render
from  rest_framework.response import Response
from rest_framework.decorators import api_view

from cart.cart import Cart
from shop import settings
from .serializers import PaintingSerializers, EmployeeSerializers, BuyerUserSerializers, CartSerializers
from shoppainting.models import Painting, Employee, BuyerUser
from rest_framework.permissions import IsAuthenticated

# Create your views here.

#Вывод всех картин
@api_view(['GET'])
def paintingsApi(request):
    if request.method == "GET":
        painting_api = Painting.objects.filter(avaliable = True)
        serializer = PaintingSerializers(painting_api, many=True)
        return Response(serializer.data)

#Детально одна картина
@api_view(['GET'])
def paintingsDetailApi(request,pk):
    if request.method == "GET":
        painting_api = Painting.objects.get(pk=pk)
        serializer = PaintingSerializers(painting_api)
        return Response(serializer.data)

#Список сотрудников
@api_view(['GET'])
def employeesApi(request):
    if request.method == "GET":
        painting_api = Employee.objects.all()
        serializer = EmployeeSerializers(painting_api, many=True)
        return Response(serializer.data)

#Сотрудник отдельно по id
@api_view(['GET'])
def employeeDetailApi(request, pk):
    if request.method == "GET":
        painting_api = Employee.objects.get(id=pk)
        serializer = EmployeeSerializers(painting_api)
        return Response(serializer.data)

#Сотрудник менеджеры id = 2,3,4
@api_view(['GET'])
def employeesMenegersApi(request,pk=1):
    if request.method == "GET":
        painting_api = Employee.objects.filter(JobTitle__id = pk)
        serializer = EmployeeSerializers(painting_api, many=True)
        return Response(serializer.data)

#Сотрудник художники id = 1
@api_view(['GET'])
def employeesArtistsApi(request,pk=2):
    if request.method == "GET":
        painting_api = Employee.objects.filter(JobTitle__id__gte = pk)
        serializer = EmployeeSerializers(painting_api, many=True)
        return Response(serializer.data)

#Картины по годам
@api_view(['GET'])
def paintingsYearApi(request,year):
    if request.method == "GET":
        painting_api = Painting.objects.filter(year = year)
        serializer = PaintingSerializers(painting_api, many=True)
        return Response(serializer.data)

#Картины по странам
@api_view(['GET'])
def paintingsCountryApi(request,country):
    if request.method == "GET":
        painting_api = Painting.objects.filter(countryPaint__name_country = country)
        serializer = PaintingSerializers(painting_api, many=True)
        return Response(serializer.data)

#Регистрация пользователя
from rest_framework.response import Response
from rest_framework.views import APIView

class BuyerUserApiRegister(APIView):
    def post(self,request):
        bUser = BuyerUser.objects.create(
            username = request.data["username"],
            first_name = request.data["first_name"],
            last_name = request.data["last_name"],
            email = request.data["email"],
            user_avatar = request.data["user_avatar"],
            phone_number = request.data["phone_number"],
            is_active = request.data["is_active"]
        )
        print(request)
        return Response({'user': BuyerUserSerializers(bUser).data})

# {
#     "username" : "seller_2",
#     "email" : "seller_2@mail.ru",
#     "first_name":"Марина",
#     "last_name":"Петрова",
#     "user_avatar" : "photos/users_avatar/2023/07/19/emp3.jpg",
#     "phone_number" : "+79335552619",
# }

#Личный кабинет
@api_view(['GET'])
def userProfileApi(request):
    if request.method == "GET":
        user_api = BuyerUser.objects.get(id = request.user.id)
        serializer = BuyerUserSerializers(user_api)
        return Response(serializer.data)

#Корзина покупок
# class CartApiView(APIView):
#     def get(self, request): #get - запрос
#         cartApiTup = {}
#         cartApi = Cart(request)
#         for i in cartApi:
#
#         print(cartApi, len(cartApi))
#         for i in cartApi:
#             print(i, type(i))
#         serializer = CartSerializers(cartApi, many=True)
#
#         return Response(serializer.data)