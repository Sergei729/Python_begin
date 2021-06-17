# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def data(**kwargs):
    return ''.join(kwargs.values())


name = input('Введите имя_ ')
surname = input('Введите фамилию_ ')
birth_of_year = input('Введите год рождения_ ')
city = input('Введите город проживания_ ')
e_mail = input('Введите эл. адрес почты_ ')
phone = input('Введите номер телефона_ ')

print(data(name=name, surname=surname,  birth_of_year=birth_of_year, city=city, e_mail=e_mail,  phone=phone))

