from read_csv import read_csv


def main():
    """ Описание функции main.

    Записывает в файл vacancy_new.csv 3 самые оплачиваемые професии и выводит их на экран
    в формате <компания> - <вакансия> - <зарплата>

    :return: None
    """
    employees = read_csv()
    employees.sort(key=lambda employee: employee.salary, reverse=True)
    parameters = [[employee.company, employee.role, employee.salary] for employee in employees]

    with open('vacancy_new.csv', 'w', encoding='utf-8') as f:
        for params in parameters:
            line = ';'.join(map(str, params))
            f.write(f'{line}\n')

    for params in parameters[:3]:
        line = ' - '.join(map(str, params))
        print(line)


if __name__ == '__main__':
    main()
