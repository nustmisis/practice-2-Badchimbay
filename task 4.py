# -*- coding: utf-8 -*-
"""
Взгляните на показанный ниже
код, в котором используется цикл while и флаг found
для поиска в списке степеней двойки значение двойки, возведённое в пятую степень

@author: workk
"""


def start():
    L = [1, 2, 4, 8, 16, 32, 64]
    X = 5
    found = False
    i = 0
    while not found and i < len(L):
        if 2 ** X == L[i]:
            found = True
        else:
            i = i + 1

    if found:
        print('at index', i)
    else:
        print(X, 'not found')


'''
Код явно написан с использование альтернативной логики.
Попробуйте оптимизировать код c использование рекомендаций, они являются не обязательными, но помогут понять основные ошибки.
а)Сначала перепишите код с конструкцией else цикла while, чтобы избавиться от флага found и финального оператора if.
б) Затем перепишите код для использования цикла for с конструкцией else,
чтобы избавиться от явной логики индексации списка. (Подсказка: для получения индекса элемента применяйте списковый метод index — L. index (X)
возвращает смещение первого элемента X в списке L.)
в) Далее полностью устраните цикл, переписав код с использованием простого
выражения с операцией членства in. (За дополнительными сведениями обращайтесь в главу 8 или наберите для тестирования 2 in [1,2,3].)
г) Наконец примените цикл for и списковый метод append для генерации списка степеней 2 (L) вместо жесткого кодирования спискового литерала.
Ниже приведены более глубокие рассуждения.
д) Как вы думаете, улучшит ли производительность перенос выражения 2 ** X
за пределы циклов? Каким образом вы представили бы это в коде?
е)  Python содержит инструмент тар (функция, список), который также способен генерировать список степеней 2:. Каким образом можно его задать ? 
    
'''

def task(x):
    # Решение для пункта а)
    if x == 'а':
        L = [1, 2, 4, 8, 16, 32, 64]
        X = 5
        i = 0

        while i < len(L):
            if 2 ** X == L[i]:
                print('at index', i)
                break
            i = i + 1
        else:
            print(X, 'not found')
    # Решение для пункта б)
    elif x == 'б':
        L = [1, 2, 4, 8, 16, 32, 64]
        X = 5

        for i, num in enumerate(L):
            if 2 ** X == num:
                print('at index', i)
                break
        else:
            print(X, 'not found')
    # Решение для пункта в)
    elif x == 'в':
        L = [1, 2, 4, 8, 16, 32, 64]
        X = 5

        if 2 ** X in L:
            print('at index', L.index((2 ** X)))
        else:
            print(X, 'not found')
    # Решение для пункта г)
    elif x == 'г':
        L = []
        for i in range(7):
            L.append(2 ** i)
        X = 5

        if 2 ** X in L:
            print('at index', L.index((2 ** X)))
        else:
            print(X, 'not found')
    else:
        print('Введите корректный пункт задачи')

# д
'''
Перемещение выражения 2 ** X за пределы цикла не приведет к существенному улучшению производительности в данном
случае, поскольку это простой расчет.Однако, если расчет был бы более сложным или затратным по времени, было бы
полезно вычислить его один раз перед циклом и сохранить результат в переменной.
'''

# е
'''
L = [2 ** i for i in range(7)]
print(L)
'''

task(input('Введите подпункт задачи: '))
