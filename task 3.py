# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023

@author: workk



Упражнение 61. Действительный номерной знак машины?
(Решено. 28 строк)
Допустим, в нашей стране старый формат номерных знаков автомобилей состоял из трех заглавных букв, следом за которыми шли три цифры.
После того как все возможные номера были использованы, формат был 
изменен на четыре цифры, предшествующие трем заглавным буквам.
Напишите программу, запрашивающую у пользователя номерной знак 
машины и оповещающую о том, для какого формата подходит данная последовательность символов: для старого или нового. Если введенная последовательность не соответствует ни одному из двух форматов, укажите
это в сообщении
"""

num = input('Введите номерной знак: ')

if len(num) == 6 and num[:3].isalpha() and num[3:].isdigit() and num[:3].isupper():
    print("Регистрационный номер соответствует старому формату")
elif len(num) == 7 and num[:4].isdigit() and num[4:].isalpha() and num[4:].isupper():
    print("Регистрационный номер соответствует новому формату")
else:
    print("Регистрационный номер не соответствует ни одному формату")
