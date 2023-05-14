#ДЗ 9

# Первый вариант решения
from random import sample

list_numbers = sample(range(1,2**28),(10))
print(list_numbers)

#Второй вариант решения
from random import randint

list_numbers = [randint(1,2**28)for i in range(10)]
print(list_numbers)

#Третий вариант решения
import random

list_numbers = [i for i in range(1,2**28)]
sampling = random.choices(list_numbers, k=10)
print(sampling)

#Линейный поиск
def line_search(list_numbers, n, key): # Назначаем переменные: n - длина списка, key - индекс, который мы ищем
    for i in range(0, n): # Перебираем элементы из списка
        if (list_numbers[i]== key):
            return i
        return -1

list_numbers = [123214899, 118686286, 99748545, 217963979, 79550644, 235162193, 217493053, 199649654, 93175296, 22219652]
key = 123214899

n = len(list_numbers)
number = line_search(list_numbers, n, key)
if (number == -1):
    print('Индекс не найден')
else:
    print('Индекс:', number)

# Бинарный поиск
def binary_search(list_numbers2, key):
    left = 0
    right = len(list_numbers2) - 1
    index = -1
    while (left <= right) and (index == -1):
        middle = (left + right) // 2
        if list_numbers2[middle] == key:
            index = middle
        else:
            if key < list_numbers2[middle]:
                right = middle - 1
            else:
                left = middle + 1
    return index


list_numbers2 = [123214870, 123214880, 123214890, 123214900, 123214910, 123214920]
key = 123214890

result = binary_search(list_numbers2, key)
if (result == -1):
    print('Индекс не найден')
else:
    print('Индекс:', result)


