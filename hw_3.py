# 1. Создать класс Computer (компьютер) с приватными атрибутами cpu и memory.
#
# 2. Добавить сеттеры и геттеры к существующим атрибутам.
#
# 3. Добавить в класс Computer метод make_computations, в котором бы выполнялись арифметические вычисления с атрибутами объекта cpu и memory.
#
# 4. Создать класс Phone (телефон) с приватным полем sim_cards_list (список сим-карт)
#
# 5. Добавить сеттеры и геттеры к существующему атрибуту.
#
# 6. Добавить в класс Phone метод call с входящим параметром sim_card_number и call_to_number, в котором бы распечатывалась симуляция звонка в зависимости от переданного номера сим-карты (например: если при вызове метода передать число 1 и номер телефона, распечатывается текст “Идет звонок на номер +996 777 99 88 11” с сим-карты-1 - Beeline).
#
# 7. Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone.
#
# 8. Добавить метод в класс SmartPhone use_gps с входящим параметром location, который бы распечатывал симуляцию построения маршрута до локации.
#
# 9. В каждом классе переопределить магический метод __str__ которые бы возвращали полную информацию об объекте.
#
# 10. Перезаписать все магические методы сравнения в классе Computer (6 шт.), для того чтоб можно было сравнивать между собой объекты, по атрибуту memory.
#
# 11. Создать 1 объект компьютера, 1 объект телефона и 2 объекта смартфона
#
# 12. Распечатать информацию о созданных объектах.
#
# 13. Опробовать все возможные методы каждого объекта (например: use_gps, make_computations, call, а также магические методы).


class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print (f'выполняются арифметические вычисления с cpu and memory .')

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory



    def __str__(self):
        return f'Назввания процессора {self.cpu}, оперативная память {self.memory}'




class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value



    def call(self, sim_card_number, call_to_number):
        if sim_card_number == 1:
            print(f'Идет звонок на номер: {call_to_number} с сим-карты {sim_card_number} - O!')
        elif sim_card_number == 2:
            print(f'Идет звонок на номер: {call_to_number} с сим-карты {sim_card_number} - Megacom')
        else:
            print('Нет такой сим-карты.')

    def __str__(self):
        return f'Номера телефона {self.sim_cards_list}'

class SmartPhone(Phone, Computer):

    def __init__(self, cpu, memory, sim_cards_list):
        Phone.__init__(self, sim_cards_list)
        Computer.__init__(self, cpu, memory)

    def use_gps(self, location):
        print (f'Едим в {location}')

    def __str__(self):
        return f"'Aple', список контактов: {self.sim_cards_list}, память: {self.memory}, оперативная память: {self.cpu}"







computer = Computer('Ryzen_3050', 256)
phone = Phone(['700458568', '700152574'])
smart_phone = SmartPhone('intel_core_i5', 516, ['700546482', '700353956'])
smart_phone_2 = SmartPhone('intel_core_i7', 1024, ['512842854', '512435567'])



print(computer)
print(phone)
print(smart_phone)
print(smart_phone_2)
computer.make_computations()
phone.call(1, '700486828')
smart_phone.use_gps('Dordoi_Plaza')
smart_phone_2.use_gps('Mall')

print(computer > smart_phone_2)
print(computer < smart_phone)
print(computer <= smart_phone)
print(computer >= smart_phone_2)
print(computer != smart_phone_2)
print(computer == smart_phone)
