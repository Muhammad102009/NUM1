# """Задание 1: Set (Множества)
# ТЗ: Напишите функцию unique_elements(lst), которая принимает список и возвращает множество уникальных элементов из этого списка.

# Требования:

# Функция должна принимать список с элементами (могут быть числа, строки или другие хешируемые типы).
# Возвращаемый результат должен быть множеством, содержащим только уникальные элементы."""
# # def unique_elements(lst):
# #     num1 = []
# #     for num in lst:
# #         if num not in num1:
# #             num1.append(num)
# #     return num1
# # num2 = [1.2, 0.7, 2, 3, 4, 4765, 5, 'a', 'b', 'a']
# # num3 = unique_elements(num2)
# # print(num3)
# """Задание 2: Словарь
# ТЗ: Напишите функцию invert_dict(dct), которая принимает словарь и возвращает новый словарь, где ключами становятся значения исходного словаря, а значениями — ключи.

# Требования:

# Если значения в словаре неуникальны, выберите одно из ключей.
# Значения словаря могут быть только хешируемыми типами данных (строки, числа и т.д.)."""
# # def invert_dict(dct):
# #     num = {}
# #     for num1, num2 in dct.items():
# #         num[num2] = num1
# #     return num
# # d = {123: "2495", "abc":123, "xyz": "dygby"}
# # print(invert_dict(d))
# """Задание 3: Функции
# ТЗ: Напишите функцию is_palindrome(s), которая принимает строку и возвращает True, если строка является палиндромом 
# (читается одинаково в обе стороны), и False в противном случае.

# Требования:

# Игнорируйте регистр букв и пробелы.
# Строка может содержать только буквы."""
# def is_palindrome(s):
#     num = []

""" ООП - Объектно Ориентированое Програмтрование """
full_name = 'Islam'

FullName = 'Islam'

class SuperCar: # Шаблон и Чертеж
    def __init__(self,wheel,motor,color): # __init__ Конструктор
        self.wheel = wheel # Отребут класса
        self.motor = motor # self - ссылка на текущий объект
        self.color = color
        self.bak = 20
        self.is_start = False

    def info(self): # Функция внутри класса превращается в метод
            print(f"Колесо - {self.wheel}, Мотор - {self.motor}, Цвет {self.color}")
    def start(self):
         if self.bak > 0 :
              self.is_start = True
              print("Машина заведена")
         else:
              print("У машины нету топлива")
    def stop(self):
         self.is_start = False
         print("Машина заглужена")
    def drive(self, city):
         if self.is_start == True:
              print(f'Машина едет в {city}')
         else:
              print("Машина не заведена")
car = SuperCar("R20",'V8','Black') # Экземпляр класса
car.info() # вызов метода, обращаясь к экземпляру
car.start()
# car.stop()
car.drive("Дубай")