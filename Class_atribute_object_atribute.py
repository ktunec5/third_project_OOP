class Employee:
    vacation_days = 28

    # Вместо инструкции pass напишите свой код.
    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender

    def scream(self):
        return 'ААааа!'

    def consume_vacation(self, days: int):
        self.vacation_days = self.vacation_days - days

    def remaining_vacation_days(self):
        return self.vacation_days


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee('Миша', 'Тун', 'М')
employee2 = Employee('Вера', 'Тун', 'Ж')

# Допишите код для вывода информации о сотрудниках.
# print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, '
#       f'Пол: {employee1.gender}, '
#       f'Отпускных дней в году: {Employee.vacation_days}.')
# print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, '
#       f'Пол: {employee2.gender}, '
#       f'Отпускных дней в году: {Employee.vacation_days}.')
print(employee1.remaining_vacation_days())
employee1.consume_vacation(2)
print(employee1.remaining_vacation_days())
print(employee2.remaining_vacation_days())
