# class Game:
#     def __init__(self, game_name, relize, type, memory):
#         self.game_name = game_name
#         self.relize = relize
#         self.type = type
#         self.memory = memory

#     def info(self):
#         print(f"Название игры - {self.game_name}\nДата выпуска - {self.relize}\nТип игры - {self.type}\nВес игры - {self.memory}")

# # Наследование класса Game
# class Roblox(Game):
#     def __init__(self, game_name, relize, type, memory, multiplayer):
#         # Вызов конструктора родительского класса
#         super().__init__(game_name, relize, type, memory)
#         self.multiplayer = multiplayer
#         self.name = 'biloolool'
#         self.gender = 'man'
#         self.skin = 'naruto'
#         self.hp = 100

#     # Переопределение метода info для класса Roblox
#     def info(self):
#         super().info()  # Вызов метода info родительского класса
#         print(f"Мультиплейер - {self.multiplayer}")

#     # Метод для отображения информации об игроке
#     def info_player(self):
#         print(f"Игрок - {self.name} - {self.gender} - {self.skin} - {self.hp}")

#     # Метод для изменения характеристик игрока
#     def edit_player(self):
#         name = input("Введите имя игрока: ")
#         gender = input("Введите пол игрока: ")
#         skin = input("Введите облик для игрока: ")
#         self.name = name
#         self.gender = gender
#         self.skin = skin

# # Пример использования
# roblox = Roblox('Roblox', 2008, 'multi platforms', "30GB", "yes")
# roblox.info()  # Вывод информации о игре
# roblox.edit_player()  # Изменение характеристик игрока 
# roblox.info_player()  # Вывод информации об игроке

# class Strike(Roblox):
#     def __init__(self, game_name, relize, type, memory, multiplayer):
#         super().__init__(game_name, relize, type, memory, multiplayer)

#         def info_player(self):
#             return super().info_player()
        

"""''''Задание: Симуляция Зоопарка с Конструкторами
Создайте классы, которые будут моделировать разных животных в зоопарке, используя множественное наследование и конструкторы для инициализации объектов.

Базовые классы:

Создайте класс Animal, который будет представлять общее животное. У этого класса должен быть конструктор init(), который принимает параметр name для имени животного. Также добавьте методы eat() и sleep(), которые выводят сообщения, например, "{name} ест" и "{name} спит".

Создайте класс Walker, который будет представлять животных, которые могут ходить. У этого класса должен быть метод walk(), который выводит сообщение "{name} ходит".

Создайте класс Swimmer, который будет представлять животных, которые могут плавать. У этого класса должен быть метод swim(), который выводит сообщение "{name} плавает".

Создайте класс Flyer, который будет представлять животных, которые могут летать. У этого класса должен быть метод fly(), который выводит сообщение "{name} летает".

Комбинированные классы:
                                            
Создайте класс Penguin, который наследуется от Animal, Walker, и Swimmer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что пингвин может ходить и плавать.

Создайте класс Duck, который наследуется от Animal, Walker, Swimmer, и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что утка может ходить, плавать и летать.

Создайте класс Bat, который наследуется от Animal и Flyer. Реализуйте конструктор, который принимает параметр name и вызывает конструктор класса Animal. Добавьте метод describe(), который выводит сообщение о том, что летучая мышь может летать.

Тестирование:

Создайте экземпляры каждого из созданных вами классов, передавая им имена, и вызовите для них методы describe(), а также методы, относящиеся к их поведению (напsefример, walk(), swim(), fly()).'''"""

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")

    def sleep(self):
        print(f"{self.name} спит")


class Walker:
    def walk(self):
        print(f"{self.name} ходит")


class Swimmer:
    def swim(self):
        print(f"{self.name} плавает")


class Flyer:
    def fly(self):
        print(f"{self.name} летит")


class Penguin(Animal, Walker, Swimmer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может ходить и плавать но не летать")


class Duck(Animal, Walker, Swimmer, Flyer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может ходить плавать и летать")


class Bat(Animal, Flyer):
    def __init__(self, name):
        super().__init__(name)

    def describe(self):
        print(f"{self.name} может летать но не плавать и не ходить")


penguin = Penguin("Пингвин")
duck = Duck("Утка")
bat = Bat("Летучая мышь")

penguin.describe()
penguin.walk()
penguin.swim()
penguin.eat()
penguin.sleep()
print("\n")
duck.describe()
duck.walk()
duck.swim()
duck.fly()
duck.eat()
duck.sleep()
print("\n")
bat.describe()
bat.fly()
bat.eat()
bat.sleep()
