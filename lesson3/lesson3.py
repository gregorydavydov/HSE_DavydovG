"""
f = open('traders.txt') - открыть файл
f.readline() - открыть очередную строку
next(f) - также открыть очередную строку
content = f.readlines() - прочитать файл целиком в назначенную переменную 'content'
enumerate() - перечисление выведенных значений
line.strip('\n').split(',') = убираем лишние символы + преобразуем значения в список

f = open('traders.txt')
b = open('traders.json')
for line in f
line = line.strip('\n').split(',')
content = line
print(line or content)

break

with open ('traders.txt') as file:
    for line in file:
        line = line.strip('\n').split(',')
        content = line
        print(content)


with open ('traders.txt') as f:
    with open ('traders.json') as f2read:
        with open ('traders.csv') as f2write:

Перевод json файл в cловарь
import json

with open ('traders.json') as f:
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        print(dict_, type(dict_))

1)with open('traders.json','r') as f:
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        content = dict_

2)with open('data) as f2write:
    json.dump(content, f2write)
    f2write.write('\n')

3)with open('data'') as f:
    for line in f:
        line = line.strip()
        dict2_ = json.loads(line)
        content = dict2_

import json

with open('traders.json','r') as f:
    for line in f:
        line = line.strip()
        dict_ = json.loads(line)
        content = f1.read()
        dict_ = json.loads(content)
        contents = dict_
        print(contents)

import json
from traders.json
from traders.txt

result = ['7702758341', '7802654025', '5027217264','6324042940','5834031870','1657061756','3665044042','6453102410']

import json

with open('traders.json','r') as f1:
        content = f1.read()
        data = json.loads(content)
        print(data)

with open('traders.txt') as f2:
    for line in enumerate(f2):
        inn_list = [line.strip() for line in f2]
        inn = ['7802654025', '5027217264', '6324042940', '5834031870', '1657061756', '3665044042', '6453102410']
        if inn in data:
            inn = data[inn]
            inn = data[ogrn]
            inn = data[address]

with open('traders.json', 'r') as f2:
    content = f2.read()
    data = json.loads(content)



"""
import json

with open('traders.txt') as f1:
    for line in enumerate(f1):
        inn_list = [line.strip() for line in f1]
        print(inn_list)

with open('traders.json', 'r') as f2:
    for line in f2:
        line = line.strip()
        dict_ = json.loads(line)
        if inn_list in dict_:
            inn_list = dict_[inn]
            inn_list = dict_[address]
            inn_list = dict_[address]





























































