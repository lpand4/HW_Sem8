import modules as m
import view


def menu():
    while True:
        choise = show_menu()
        print('')
        if choise == 0:
            break
        elif choise == 1:
            view.find_worker(input('Введите имя искомого сотрудника: '))
        elif choise == 2:
            print('1 - Разнорабочий\n'
                  '2 - Менеджер/Инженер\n'
                  '3 - Заместитель главы отдела\n'
                  '4 - Глава отдела\n'
                  '5 - Заместитель генерального директора\n'
                  '6 - Генеральный директор\n')
            view.show_worker_by_post(input('Введите через пробел должности,'
                                               ' которые хотите увидеть: '))
        elif choise == 3:
            view.show_worker_by_salary(int(input('Введите нижнюю границу зарплаты: ')),
                                       int(input("Введите верхнюю границу зарплаты:")))
        elif choise == 4:
            m.add_worker()
            m.numerate_list()
        elif choise == 5:
            view.show_all_worker()
            m.delete_worker(input('Введите номер сотрудника, которого хотите удалить: '))
            m.numerate_list()
        elif choise == 6:
            view.show_all_worker()
            m.update_data_worker(input('Введите номер сотрудника,'
                                       ' информацию которого хотите обновить: '))
        elif choise == 7:
            m.export_to_json()
        elif choise == 8:
            m.export_to_csv()
        elif choise == 9:
            view.show_all_worker()

    if choise == 0:
        print('Goodbye!')


def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате csv")
    print("9. Показать всех сотрудников")
    print("0. Закончить работу")
    return int(input("Введите номер необходимого действия: "))
