from employee import Employee


def read_csv() -> list[Employee]:
    """ Описание функции read_csv.

    Читает список Employee из файла vacancy.csv

    :return: list[Employee]
    """
    with open('vacancy.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]
        employees = []
        for line in lines:
            data: list = line.split(';')
            data = list(map(str.strip, data))
            data[0] = int(data[0])
            data[2] = int(data[2])
            employees.append(Employee(*data))
        return employees
