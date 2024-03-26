class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days
        # Сюда добавьте новый атрибут remaining_vacation_days

    # Сюда добавьте методы consume_vacation и get_vacation_details.
    def consume_vacation(self, days):
        self.remaining_vacation_days = self.remaining_vacation_days - days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'

    def __str__(self):
        return 'Я объект employee, принадлежащий классу Employee.'


employee = Employee('Роберт', 'Крузо', 'м')

print(employee)