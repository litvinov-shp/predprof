from employee import Employee


def read_csv() -> list[Employee]:
    with open('vacancy.csv', 'r') as f:
        lines = f.readlines[1:]
        employees = []
        for line in lines:
            data = line.split(';')
            data[0] = int(data[0])
            data[2] = int(data[2])
            employees.append(Employee(*data))
        return employees
