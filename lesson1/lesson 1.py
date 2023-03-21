


# Небольшие заметки на полях в процессе изучения материала первого практического занятия:

"""
isdigit - cодержит ли текст цифры
for i in inn:
[] - корджедж, [1:5:] - перечисление с одного элемента до следующего,
[::2] - каждый элемент по последовательности,
[-1:-2:] - в обратную сторону
append - добавить в пустой список значения
person.update - ({"bank": "Сбер"})
dict() - cоздать словарь
input() - запросить данные у пользователя
text.split - разбивка массива на отдельные значения
"""

#ДЗ_1

# Task_one
a = 1
b = 2.1
c = true

text = 'test'
inn = '212312312'

inns_1 = ['21231235', '21231234', '21231233', '21231232','21231232']
inns_2 = ('91231236', '81231237', '71231238', '61231239')


# Task_two

second = input("Введите данные:")
if second.isdigit():
    print("Спасибо за введенные цифры")
    second = int(second)
else:
    print("Вам необходимо ввести цифры")
    second = input("Введите данные:")

hour = second/3600
minute = hour/60

print(hour)
print(minute)
print(second)


# Task_three
a = int(input("Введите число от 1 до 9:"))
if a > 0 and a <= 9:
  print(str(a)+str(a+a)+str(a+a+a))


#ДЗ_2(дополнительное)

side_1 = {
    "name": 'ООО "Промторг"',
    "status": "Истец",
    "inn": "11111111"
}
side_2 = {
    "name": 'Иванов И.И.',
    "status": "Ответчик",
    "inn": "232323232323"

}

side_3 = {
    "name":'Павлов П.П.',
    "status": "Третье лицо",
    "inn": "34343434"
}

print(side_1)
print(side_2)
print(side_3)








"""
В процессе выполнения заданий было удобней перепроверять результат через colab :)
Ссылке здесь: https://colab.research.google.com/drive/1sPzDA0XfEkpWaL0fGXJO6J_aYRPqCojm?usp=sharing
"""
