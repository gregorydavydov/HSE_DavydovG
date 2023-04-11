"""
f = open('traders.txt') - открыть файл
f.readline() - открыть очередную строку
next(f) - также открыть очередную строку
content = f.readlines() - прочитать файл целиком в назначенную переменную 'content'
enumerate() - перечисление выведенных значений
line.strip('\n').split(',') = убираем лишние символы + преобразуем значения в список
"""

#Task 1

import json

inn_list = []
org_list = []

# 1. Получаем из файла список ИНН
with open('traders.txt') as f1:
    for line in f1:
        inn_list.append(line.strip())

# 2. Находим в json файле информацию об организации по ИНН из первого файла
with open('traders.json', 'r') as f2:
    org_data = json.load(f2)
    for org in org_data:
        if org['inn'] in inn_list:
            org_list.append(org)

# 3. Сохраняем информацию в новом файле
with open('traders.csv', 'w', encoding='utf-8') as f3:
    f3.write('INN, OGRN, ADDRESS\n')
    for org in org_list:
        inn = org['inn']
        ogrn = org['ogrn']
        address = org['address']
        f3.write(f'{inn}, {ogrn}, {address}\n')




































































