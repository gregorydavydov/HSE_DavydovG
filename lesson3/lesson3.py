"""
with open('traders.txt') as ... - открыть файл
f.readline() - открыть очередную строку
next(f) - также открыть очередную строку
content = f.readlines() - прочитать файл целиком в назначенную переменную 'content'
enumerate() - перечисление выведенных значений
line.append - добавить
line.strip('\n').split(',') = убираем лишние символы + преобразуем значения в список
"""

#Task 1

import json

inn_list = []
org_list = []

with open('traders.txt') as f1: # Получаем из файла список ИНН
    for line in f1:
        inn_list.append(line.strip()) # Добавляем значение line в список inn_list

with open('traders.json', 'r') as f2: # Находим в json файле информацию об организации по ИНН из первого файла
    org_data = json.load(f2)
    for org in org_data:
        if org['inn'] in inn_list:
            org_list.append(org) # Добавляем значения в org_list при условии, если org есть в inn_list

with open('traders.csv', 'w', encoding='utf-8') as f3: # Сохраняем информацию в новом файле
    f3.write('Информация об организациях:\n')
    for org in org_list: # Приравнием к org значение 'inn', 'ogrn', 'address'
        inn = org['inn']
        ogrn = org['ogrn']
        address = org['address']
        f3.write(f'ИНН:{inn}, ОГРН: {ogrn}, Адрес: {address}\n')


#Task 2

import json
import re

def find_emails(file_json): # Функция, которая принимает в себя файл '1000_efrsb_messages.json'
    emails_data = {} # Пустой словарь
    with open(file_json, 'r') as f:
        messages = json.load(f)
        for message in messages:
            publisher_inn = message['publisher_inn']
            msg_text = message['msg_text']
            emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', msg_text)
            # Поиск всех адресов электронной почте в msg_text на основе регулярного выражения
            if emails:
                if publisher_inn not in emails_data:
                    emails_data[publisher_inn] = set()
                emails_set = set(emails) # Множество адресов электронной почты
                emails_data[publisher_inn].update(emails_set) # Обновляет множество электронных адресов для каждого ИНН
    return emails_data # Возвращаем словарь

emails_data = find_emails('1000_efrsb_messages.json') # Обращаемся к файлу json

with open('emails.json','w', encoding='utf-8') as email2write:
    # Создаем новый файл json, в котором сохраним все данные emails_data
    email2write.write('Список адресов электронной почты:''\n')
    for message in emails_data:
        email2write.write(f'{emails_data}')



























































































































