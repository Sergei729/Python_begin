# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('list_workers.txt', encoding='utf-8') as f:
    workers_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя зарплата = {round(sum(workers_dict.values()) / len(workers_dict), 0)}\n'
          f'Сотрудники с окладом менее 20 тыс.: {[i[0] for i in workers_dict.items() if i[1] < 20000]}')
