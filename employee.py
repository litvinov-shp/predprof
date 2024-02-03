class Employee:
    """ Описание класса Employee.
    Employee - сотрудник компании. Содержит следующие переменные:
    salary - заработная плата
    work_type - тип контракта
    company_size - количество сотрудников в компании
    role - профессия
    company - название компании
    """
    def __init__(self, salary, work_type, company_size, role, company):
        self.salary = salary
        self.work_type = work_type
        self.company_size = company_size
        self.role = role
        self.company = company
