# ''' OOП - Обкутно ориентированное програмирование '''
# ''' Инкапсуляция '''

# # Публичный

# class PublickExemple:
#     def init(self, value):
#         self.value = value

#     def info(self):
#         return self.value #Публичный атрибут

# public = PublickExemple(23)
# print(public.info()) # Вызов публичного метода
# print(public.value) # Вызов атребута

# # Защищенный
# class ProtectedExample:
#     def __init__(self,value):
#         self._value = value# Защищенный атрибут

#     def _info(self):
#         return self._value #Защищенный метод
    
# protected = ProtectedExample(43)
# print(protected._info()) # Это работает, но это противоречит принципам инкапсуляции
# print(protected._value) # Можно получить значение напрямую, но это не рекомендуется


# # Приватный 
# class PrivateExample:
#     def __init__(self,value):
#         self.__value = value

#     def  __info(self):
#         return self.__value
    
# private = PrivateExample(65)
# print(private.__info())
# print(private.__value)
# print(private.__value)
# print(private.access_private)
# print(private._PrivateExample__value)
# class MobiLegends:
#     def __init__(self, person, rang, item, history):
#         self.__history = history

#     def _item_player(self):
#         self.person = input("Выберите персонажа: ")
#         self.rang = input("Введите ранг: ")
#         self.item = input("Введите сборку: ")
#     def __history_player(self):
#         print(f'Персонаж - {self.person}, Ранг - {self.rang}, Сумка - {self.item}, История - {self.__history}')

#     def access_history(self):
#         return (self.__history_player())

# mobile = MobiLegends("Альфа", "Легенда", "меч", "2 победы")
# mobile._item_player()
# mobile.access_history()


"""Задание: Создать класс для управления состоянием телефона с использованием инкапсуляции.

Описание задачи:

Создайте класс Phone с инкапсуляцией данных, который будет представлять телефон. В классе должны быть следующие поля и методы:

Поля:

Закрытое поле _battery_level — уровень заряда батареи (значение от 0 до 100).
Закрытое поле _is_on — статус телефона (включен или выключен).
Методы:

turn_on() — включает телефон (если заряд батареи больше 0).
turn_off() — выключает телефон.
charge(amount) — заряжает телефон на указанное количество процентов (максимум до 100).
use_phone(time) — использует телефон в течение указанного времени (каждые 10 минут использования уменьшают заряд батареи на 10%).
Задание:

Реализуйте класс Phone с инкапсуляцией данных.
Напишите код, который создает объект телефона, включает его, использует, затем заряжает, и выводит на экран состояние телефона после каждой операции."""

class Phone:
    def __init__(self,battery,on_of):
        self._battery_level = battery
        self._is_on = on_of
    def 