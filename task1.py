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

    def sound(self):
        print('Работаю!')


employee = Employee('Роберт', 'Крузо', 'м')
employee_2 = Employee('Vira', 'Tun', 'f')
employee_2.consume_vacation(1)


class TeamLead(Employee):
    team = 40
    vacation_days = 300

    def __init__(self, first_name, second_name, gender, weight):
        super().__init__(first_name, second_name, gender)
        self.weight = weight

    def sound(self):
        print('Работать!')


teamlead = TeamLead('Mike', 'Tun', 'm', 92)
mlead = TeamLead('Vira', 'Tun', 'f', 80)

teamlead.first_name = 'Mihhail'
print(mlead.weight, mlead.first_name, mlead.second_name)

