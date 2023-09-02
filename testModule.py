from datetime import datetime

import re
#Валидация формата картины - модель
def ValidateFormatPaintingSize(size):
    print('Проверка размера')
    pattern = r"^[0-9]{2,3}x[0-9]{2,3}$"
    p = re.compile(pattern)
    rezult = p.search(size)
    if not rezult:
        print('Введите значение согластно шаблона 00x00 или 000x000')
    else:
        print('Значение валидно')

#Тест запрос - последние 10 картин
list_paints = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
print(list_paints[-10::])