import json


# Экспортировать данные в формате json
def export_to_json():
    with open('workers.txt', 'r') as f:
        data = f.readlines()
    with open('workers.json', 'w') as file:
        json.dump(data, file)


# Экспортировать данные в формате csv
def export_to_csv():
    with open('workers.txt', 'r') as f:
        data = f.readlines()
    with open('workers.csv', 'w') as file:
        for line in data:
            file.write(f'{line}')


# Нумерация списка сотрудников
def numerate_list():
    with open('workers.txt', 'r') as f:
        lines = f.readlines()
    with open('workers.txt', 'w') as file:
        for i, line in enumerate(lines, start=1):
            if '.' in line:
                line = line.split('.')
                data = f'{i}. {line[1][1:]}'
                file.write(data)
                continue
            data = f'{i}. {line}'
            file.write(data)


# Добавить сотрудника
def add_worker():
    with open('workers.txt', 'a') as f:
        first_name = input('First name: ')
        second_name = input('Second name: ')
        print('1 - Разнорабочий\n'
              '2 - Менеджер/Инженер\n'
              '3 - Заместитель главы отдела\n'
              '4 - Глава отдела\n'
              '5 - Заместитель генерального директора\n'
              '6 - Генеральный директор\n')
        post_dict = {1: 'Разнорабочий',
                     2: 'Менеджер/Инженер',
                     3: 'Заместитель главы отдела',
                     4: 'Глава отдела',
                     5: 'Заместитель генерального директора',
                     6: 'Генеральный директор'}
        post = int(input('Post: '))
        salary = input('Salary: ')
        f.write(f'{first_name}|{second_name}|{post_dict[post]}|{salary}\n')


# Удалить сотрудника

def delete_worker(deleted=''):
    with open('workers.txt', 'r') as f:
        lines = f.readlines()
    with open('workers.txt', 'w') as file:
        for line in lines:
            data = line.split('.')
            if data[0] != deleted:
                file.write(line)


# Обновить данные сотрудника
def update_data_worker(updated):
    with open('workers.txt', 'r') as f:
        lines = f.readlines()
    with open('workers.txt', 'w') as file:
        for line in lines:
            data = line.split('.')
            if data[0] != updated:
                file.write(line)
            else:
                first_name = input('First name: ')
                second_name = input('Second name: ')
                print('1 - Разнорабочий\n'
                      '2 - Менеджер/Инженер\n'
                      '3 - Заместитель главы отдела\n'
                      '4 - Глава отдела\n'
                      '5 - Заместитель генерального директора\n'
                      '6 - Генеральный директор\n')
                post_dict = {1: 'Разнорабочий',
                             2: 'Менеджер/Инженер',
                             3: 'Заместитель главы отдела',
                             4: 'Глава отдела',
                             5: 'Заместитель генерального директора',
                             6: 'Генеральный директор'}
                post = int(input('Post: '))
                salary = input('Salary: ')
                file.write(f'{updated}. {first_name}|{second_name}|{post_dict[post]}|{salary}\n')
