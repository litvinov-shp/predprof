class Employee:
    """ Описание класса Employee.

    Employee - сотрудник компании. Содержит следующие переменные:

    @:param salary - заработная плата

    @:param work_type - тип трудоустройства

    @:param company_size - количество сотрудников в компании

    @:param role - профессия

    @:param company - название компании
    """
    def __init__(self, salary, work_type, company_size, role, company):
        self.salary = salary
        self.work_type = work_type
        self.company_size = company_size
        self.role = role
        self.company = company

    def to_csv(self, delimiter: str = ";") -> str:
        """ Описание функции to_csv
        Превращает Employee в строку csv
        @:param delimiter - разделитель csv
        :return: str
        """
        parameters = [self.salary, self.work_type, self.company_size, self.role, self.company]
        return delimiter.join(map(str, parameters))
