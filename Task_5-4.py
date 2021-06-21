# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

number_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('numbers_new.txt', 'w', encoding='utf-8') as rus:
    with open('numbers.txt', 'r', encoding='utf-8') as eng:
        rus.write(str([line.replace(line.split()[0], number_dict.get(line.split()[0])) for line in eng]))
