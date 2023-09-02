from django.db import models
from shoppainting.models import BuyerUser
from django.urls import reverse, reverse_lazy
from datetime import datetime
#Модель офромленный заказ

class Order(models.Model):
    user_order = models.ForeignKey(BuyerUser,on_delete=models.PROTECT, related_name='order', verbose_name='Заказчик')
    order_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления заказа')
    order_number = models.CharField(max_length=50,verbose_name='Номер заказа')
