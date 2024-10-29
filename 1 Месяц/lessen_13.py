"""Описание задачи:
Вам нужно создать классы для системы пользователей, где каждый пользователь имеет имя и пароль, 
а администратор — дополнительные привилегии. Используйте наследование для создания разных типов пользователей и инкапсуляцию для защиты пароля.

Требования:
Базовый класс User:

Атрибуты:
username (имя пользователя, строка)
password (пароль, строка, должен быть приватным)
Методы:
get_username(): возвращает имя пользователя.
change_password(new_password): изменяет пароль пользователя (метод должен защищать приватный атрибут).
Класс-наследник AdminUser:

Наследует от класса User.
Дополнительный атрибут:
privileges (строка, описывающая привилегии администратора, например, "может удалять пользователей").
Метод:
get_privileges(): возвращает привилегии администратора.
Инкапсуляция:

Атрибут password должен быть приватным (недоступен напрямую).
Доступ к паролю только через метод change_password()."""
# class User:
#     def __init__(self, username, password): 
#         self.username = username
#         self.__password = password  

#     def get_username(self):
#         return self.username

#     def change_password(self, new_password):
#         self.__password = new_password
#         print("Пароль изменен.")

# class AdminUser(User):
#     def __init__(self, username, password, privileges):  
#         super().__init__(username, password)  
#         self.privileges = privileges

#     def get_privileges(self):
#         return self.privileges

# admin = AdminUser("admin", "adminpass", "может удалять пользователей")
# print(admin.get_username())  
# print(admin.get_privileges())  

# user1 = User("john_doe", "pass123")
# print(user1.get_username())  
# user1.change_password("new_pass456") 

"""Описание задачи:
Создайте систему управления заказами в магазине. В магазине есть разные типы товаров: продукты питания и электроника. 
Каждый тип товара имеет свои уникальные свойства. Используйте наследование для создания классов, которые будут описывать эти товары.

Требования:
Базовый класс Product:

Атрибуты:
name (название товара, строка)
price (цена товара, число с плавающей точкой)
Методы:
get_info(): возвращает информацию о товаре в формате "Товар: <название>, Цена: <цена>".
Класс-наследник FoodProduct (Продукты питания):

Наследует атрибуты и методы класса Product.
Дополнительные атрибуты:
expiration_date (срок годности, строка в формате "ДД.ММ.ГГГГ")
Методы:
get_info(): переопределите этот метод, чтобы он возвращал информацию о продукте питания с учетом срока годности.
Класс-наследник ElectronicProduct (Электроника):

Наследует атрибуты и методы класса Product.
Дополнительные атрибуты:
warranty_years (гарантия в годах, целое число)
Методы:
get_info(): переопределите этот метод, чтобы он возвращал информацию о товаре с учетом гарантии.
Создание товаров:

Создайте объекты для продуктов питания и электроники, используя классы FoodProduct и ElectronicProduct.
Выведите информацию о каждом товаре с помощью метода get_info()."""

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def get_info(self):
#         print(f"Товар {self.name}, Цена {self.price}")

# class FoodProduct(Product):
#     def __init__(self, name, price, expiration_date):
#         super().__init__(name, price)
#         self.expiration_date = expiration_date

#     def get_info(self):
#         print(f"Имя - продукта {self.name}, Цена - продукта {self.price}, Срок годности - продукта {self.expiration_date}")

# class ElectronicProduct(Product):
#     def __init__(self, name, price, warranty_years):
#         super().__init__(name, price)
#         self.warranty_years = warranty_years

#     def get_info(self):
#         print(f"Имя - товара {self.name}, Цена - товара {self.price}, Гарантия - товара {self.warranty_years}")

# num1 = FoodProduct("Ананас", "600c", "30.10.2024г")
# num2 = ElectronicProduct("Ноутбук", "50.000c", "от - 24.10.2024г до - 24.10.2025г")

# num1.get_info() 
# num2.get_info() 

"""Описание задачи:
Вы работаете над системой управления заказами в магазине, где есть различные типы товаров: продукты питания, электроника и одежда. 
Каждая категория товара имеет уникальные свойства и дополнительную логику, например, проверку сроков годности для продуктов питания, 
расчет гарантии для электроники и определение доступных размеров для одежды. Используйте наследование и добавьте дополнительные методы для управления этими особенностями.

Требования:
Базовый класс Product:

Атрибуты:
name (название товара, строка)
price (цена товара, число с плавающей точкой)
quantity (количество товара в наличии, целое число)
Методы:
get_info(): возвращает информацию о товаре в формате "Товар: <название>, Цена: <цена>, Количество: <количество>".
purchase(quantity): уменьшает количество товара на указанное количество (если товара достаточно в наличии).
Класс-наследник FoodProduct (Продукты питания):

Наследует атрибуты и методы класса Product.
Дополнительные атрибуты:
expiration_date (срок годности, строка в формате "ДД.ММ.ГГГГ")
Методы:
get_info(): возвращает информацию о продукте питания с учетом срока годности.
is_expired(current_date): проверяет, просрочен ли продукт на основе текущей даты (в формате "ДД.ММ.ГГГГ").
Класс-наследник ElectronicProduct (Электроника):

Наследует атрибуты и методы класса Product.
Дополнительные атрибуты:
warranty_years (гарантия в годах, целое число)
Методы:
get_info(): возвращает информацию о товаре с учетом гарантии.
is_under_warranty(purchase_date, current_date): проверяет, находится ли товар под гарантией (в формате "ДД.ММ.ГГГГ").
Класс-наследник ClothingProduct (Одежда):

Наследует атрибуты и методы класса Product.
Дополнительные атрибуты:
available_sizes (список доступных размеров, например, ["S", "M", "L", "XL"])
Методы:
get_info(): возвращает информацию о товаре с учетом доступных размеров.
is_size_available(size): проверяет, доступен ли указанный размер.
Логика покупок:

Реализуйте возможность покупки товаров с уменьшением количества на складе через метод purchase(quantity)."""
    
# class Product:
#     def init(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def get_info(self):
#         return f"Товар: {self.name} Цена: {self.price} руб Количество: {self.quantity}"

#     def purchase(self, quantity):
#         if quantity <= self.quantity:
#             self.quantity -= quantity
#             return f"Вы купили {quantity} {self.name}. Остаток: {self.quantity}"
#         else:
#             return f"Недостаточно {self.name} на складе  Доступно: {self.quantity}"

# class FoodProduct(Product):
#     def init(self, name, price, quantity, expiration_date):
#         super().init(name, price, quantity)
#         self.expiration_date = expiration_date

#     def get_info(self):
#         return f"{super().get_info()},= Срок годности: {self.expiration_date}"

#     def is_expired(self, current_date):
#         exp_date = datetime.strptime(self.expiration_date, "%d.%m.%Y")
#         curr_date = datetime.strptime(current_date, "%d.%m.%Y")
#         return curr_date > exp_date

# class ElectronicProduct(Product):
#     def init(self, name, price, quantity, warranty_years):
#         super().init(name, price, quantity)
#         self.warranty_years = warranty_years

#     def get_info(self):
#         return f"{super().get_info()} Гарантия: {self.warranty_years} лет"

#     def is_under_warranty(self, purchase_date, current_date):
#         purchase_date = datetime.strptime(purchase_date, "%d.%m.%Y")
#         current_date = datetime.strptime(current_date, "%d.%m.%Y")
#         warranty_end_date = purchase_date.replace(year=purchase_date.year + self.warranty_years)
#         return current_date <= warranty_end_date

# class ClothingProduct(Product):
#     def init(self, name, price, quantity, available_sizes):
#         super().init(name, price, quantity)
#         self.available_sizes = available_sizes

#     def get_info(self):
#         return f"{super().get_info()}, Доступные размеры: {'' .join(self.available_sizes)}"

#     def is_size_available(self, size):
#         return size in self.available_sizes

# if name == "main":

#     apple = FoodProduct("Яблоко", 50.0, 100, "01.11.2024")
#     print(apple.get_info())
#     print(apple.is_expired("24.10.2024"))
#     print(apple.purchase(20))

#     laptop = ElectronicProduct("Ноутбук", 50000, 5, 2)
#     print(laptop.get_info())
#     print(laptop.is_under_warranty("01.10.2022", "24.10.2024"))
#     print(laptop.purchase(2))

#     tshirt = ClothingProduct("Футболка", 1500, 30, ["S", "M", "L", "XL"])
#     print(tshirt.get_info())
#     print(tshirt.is_size_available("M"))
#     print(tshirt.purchase(5))

# from datetime import datetime

# # Базовый класс Product
# class Product:
#     def init(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def get_info(self):
#         return f"Товар: {self.name}, Цена: {self.price}, Количество: {self.quantity}"

#     def purchase(self, quantity):
#         self.quantity -= quantity
#         return f"Покупка {quantity} единиц товара '{self.name}' успешна. Остаток на складе: {self.quantity}"

# # Класс для продуктов питания
# class FoodProduct(Product):
#     def init(self, name, price, quantity, expiration_date):
#         super().init(name, price, quantity)
#         self.expiration_date = expiration_date

#     def get_info(self):
#         return f"Продукт: {self.name}, Цена: {self.price}, Количество: {self.quantity}, Срок годности: {self.expiration_date}"

#     def is_expired(self, current_date):
#         expiration = datetime.strptime(self.expiration_date, "%d.%m.%Y")
#         current = datetime.strptime(current_date, "%d.%m.%Y")
#         return current > expiration

# # Класс для электроники
# class ElectronicProduct(Product):
#     def init(self, name, price, quantity, warranty_years):
#         super().init(name, price, quantity)
#         self.warranty_years = warranty_years

#     def get_info(self):
#         return f"Электроника: {self.name}, Цена: {self.price}, Количество: {self.quantity}, Гарантия: {self.warranty_years} лет"

#     def is_under_warranty(self, purchase_date, current_date):
#         purchase = datetime.strptime(purchase_date, "%d.%m.%Y")
#         current = datetime.strptime(current_date, "%d.%m.%Y")
#         warranty_end = purchase.replace(year=purchase.year + self.warranty_years)
#         return current <= warranty_end

# # Класс для одежды
# class ClothingProduct(Product):
#     def init(self, name, price, quantity, available_sizes):
#         super().init(name, price, quantity)
#         self.available_sizes = available_sizes

#     def get_info(self):
#         sizes = ", ".join(self.available_sizes)
#         return f"Одежда: {self.name}, Цена: {self.price}, Количество: {self.quantity}, Доступные размеры: {sizes}"

#     def is_size_available(self, size):
#         return size in self.available_sizes

# # Пример использования
# if name == "main":
#     # Продукты питания
#     apple = FoodProduct("Яблоко", 10.5, 100, "25.10.2024")
#     print(apple.get_info())
#     print(apple.purchase(10))
#     print(apple.is_expired("24.10.2024"))  # False

#     # Электроника
#     laptop = ElectronicProduct("Ноутбук", 1500, 5, 2)
#     print(laptop.get_info())
#     print(laptop.purchase(1))
#     print(laptop.is_under_warranty("20.10.2022", "24.10.2024"))  # True

#     # Одежда
#     shirt = ClothingProduct("Рубашка", 30, 50, ["S", "M", "L", "XL"])
#     print(shirt.get_info())
#     print(shirt.purchase(5))
#     print(shirt.is_size_available("M"))  # True