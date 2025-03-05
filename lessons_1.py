# 1. Создать класс Person с атрибутами fullname, age, is_married

# 2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке

# 3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем, где ключ это название урока, а значение - оценка.
#
# 4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
#
# 5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
#
# 6. Добавить в класс Teacher атрибут уровня класса base_salary.
#
# 7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к базовой зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.
#
# 8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
#
# 9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и список возвращается функцией как результат.
#
# 10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.



class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'My name is {self.fullname}, I am {self.age} years old, and I am {"married" if self.is_married == True else "not married"}.'

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def counter_mark(self):
        counter = sum(self.marks.values()) / len(self.marks)
        return round(counter, 1)

class Teacher(Person):
    base_salary = 5000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def salary(self):
        if self.experience > 3:
            salary = self.base_salary + (self.base_salary * 0.05) * (self.experience - 3)
        else:
            salary = self.base_salary
        return f'Salary: {int(salary)} som.'

Teacher = Teacher('Aleksei', 30, True, 8)
print(Teacher.salary())
print(Teacher.base_salary)

def create_students():
    Ruslan = Student('Han_Ruslan', 20, False, {'Math': 10, 'Physics': 8, 'English': 7, 'Geograf': 5})
    Diana = Student('Rustamova_Diana', 19, False, {'Math': 6, 'Physics': 4, 'English': 7, 'Geometry': 9, 'Literatura': 4})
    Matvei = Student('Novikow_Matvei', 22, False, {'Math': 3, 'Physics': 4, 'Sport': 10, 'Chimia':5 })
    Students = [Ruslan, Diana, Matvei]
    return Students

univer = create_students()
for student in univer:
    print(student.introduce_myself(),  f'{student.counter_mark()} Средняя оценка  ')
