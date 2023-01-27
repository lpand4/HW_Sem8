# Найти сотрудника
def find_worker(first_name=''):
    with open('workers.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            name_line = line.split('|')
            if name_line[0][3:] == first_name:
                print(f'Worker - {line}')


# Сделать выборку сотрудников по должности
# Разнорабочий
# Менеджер/Инженер
# Заместитель главы отдела
# Глава отдела
# Заместитель генерального директора
# Генеральный директор
def show_worker_by_post(finded):
    post_finded = finded.split()

    post_dict = {'Разнорабочий': '1',
                 'Менеджер/Инженер': '2',
                 'Заместитель главы отдела': '3',
                 'Глава отдела': '4',
                 'Заместитель генерального директора': '5',
                 'Генеральный директор': '6'}
    with open('workers.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split('|')
            for i in post_finded:
                if post_dict[data[2]] == i:
                    print(line)


# Сделать выборку сотрудников по зарплате
def show_worker_by_salary(start, finish):
    with open('workers.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data = line.split('|')
            if start < int(data[3][:-1]) < finish:
                print(line)


# Показать всех сотрудников
def show_all_worker():
    with open('workers.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line)
