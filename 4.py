from employee import Employee
from read_csv import read_csv


def get_salaries_for_work_type(employees: list[Employee], work_type: str):
    """ Описание функции get_employees_with_work_type.

    Возвращает все зарплаты сотрудников для определённый типом трудоустройства.

    :param employees: сотрудники
    :param work_type: тип трудоустройства
    :return: list[Employee]
    """
    return [employee.salary for employee in employees if employee.work_type == work_type]


def avg(arr: list) -> float:
    """ Описание функции avg.

    Вычисляет среднее значение списка arr

    :param arr: список, для которого вычислится среднее значение
    :return: None
    """
    return sum(arr) / len(arr)


def main():
    """ Описание функции main.

    Вычисляет процентное отношение зарплаты каждого сотрудника к средней зарплате для трудойстройства сотрудника в файле
    `vacancy.csv` и записывает сгенерированные данные в файл `vacancy_procent.csv`

    :return: None
    """
    employees = read_csv()
    work_types = set(employee.work_type for employee in employees)
    average_salaries = {
        work_type: avg(get_salaries_for_work_type(employees, work_type)) for work_type in work_types
    }

    percents = [None] * len(employees)
    for i, employee in enumerate(employees):
        percents[i] = round(employee.salary / average_salaries[employee.work_type] * 100)

    with open('vacancy_procent.csv', 'w', encoding='utf-8') as f:
        for i, employee in enumerate(employees):
            f.write(f'{employee.to_csv()};{percents[i]}%\n')


if __name__ == '__main__':
    main()
