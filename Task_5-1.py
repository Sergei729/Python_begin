#  Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

with open('user_file.txt', 'w', encoding='utf-8') as f:

    while True:
        line = input('Введите данные ')
        if not line:
            break
        f.write(f'{line}\n')
