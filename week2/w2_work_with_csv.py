# задача 3
# 1. Создать список словарей
# 2. Экспорт в csv

# импортируем моудль для работы с csv
from csv import DictWriter as dw
# создаем список словарей
age_and_role =         [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

# производим запись в файл
with open('age_and_role.csv', 'w', encoding = 'utf-8') as file:
    fields = ['name', 'age', 'job']
    writer = dw(file, fields, delimiter = '-')
    writer.writeheader()
    for row in age_and_role:
        writer.writerow(row)
