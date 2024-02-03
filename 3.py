from read_csv import read_csv


def main():
    employees = read_csv()

    company = input('Введите название компании:\n')
    while company != 'None':
        company_employees = [employee for employee in employees if employee.company == company]

        if not company_employees:
            print('К сожалению, ничего не удалось найти')
        else:
            for employee in company_employees:
                print(f'В {employee.company} найдена вакансия: {employee.role}. З/п составит: {employee.salary}')

        company = input('Введите название компании:\n')


if __name__ == '__main__':
    main()
