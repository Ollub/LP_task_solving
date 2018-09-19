# открываем файл и записываем в переменную (топорно)
with open('referat.txt', 'r') as file:
    ref = file.read()

# выведем на печать длину строки
print('Длина текста: ', len(ref))

#теперь то же, только построчно
# как понял из видео, так проще обрабатывать тяжелые файлы
# функцию не вижу смысла тут создавать

sum_symb = 0
with open('referat.txt', 'r') as file:
    ref = file.readlines()
for line in ref:
    sum_symb += len(line)

print('Длина текста: ', sum_symb)

# меняем точки на восклицательные знаки
for i in range(len(ref)):
    ref[i] = ref[i].replace(".", '!')
    
# writing changes into new file
with open('decorated_referat.txt', 'w') as file:
    for i in ref:
        file.write(i)
