# """Задание на тему "Наследование, Логика Управления и Отчеты" (Python)
# Описание задачи:
# Вам необходимо создать систему управления инвентарем для магазина, где хранится информация о различных типах товаров: продукты питания, электроника и книги. 
# Каждая категория товара имеет уникальные характеристики и логику, включая проверку сроков годности, расчёт оставшейся гарантии и управление количеством в наличии. 
# Дополнительно, система должна уметь формировать отчёты по товарам: например, показывать список просроченных продуктов или товаров без гарантии.

# Требования:
# Базовый класс Product:

# Атрибуты:
# name (название товара, строка)
# price (цена товара, число с плавающей точкой)
# quantity (количество товара в наличии, целое число)
# Методы:
# get_info(): возвращает информацию о товаре в формате "Товар: <название>, Цена: <цена>, Количество: <количество>".
# purchase(quantity): уменьшает количество товара на указанное количество (если товара достаточно на складе).
# restock(quantity): увеличивает количество товара на указанное количество.
# Класс-наследник FoodProduct (Продукты питания):

# Наследует атрибуты и методы класса Product.
# Дополнительные атрибуты:
# expiration_date (срок годности, строка в формате "ДД.ММ.ГГГГ")
# Методы:
# get_info(): возвращает информацию о продукте питания с учётом срока годности.
# is_expired(current_date): проверяет, просрочен ли продукт на основе текущей даты.
# Класс-наследник ElectronicProduct (Электроника):

# Наследует атрибуты и методы класса Product.
# Дополнительные атрибуты:
# warranty_years (гарантия в годах, целое число)
# Методы:
# get_info(): возвращает информацию о товаре с учётом гарантии.
# remaining_warranty(purchase_date, current_date): возвращает количество оставшихся лет гарантии, либо сообщает, что гарантия истекла.
# `Класс-наследник BookProduct (Книги):

# Наследует атрибуты и методы класса Product.
# Дополнительные атрибуты:
# author (автор книги, строка)
# genre (жанр книги, строка)
# Методы:
# get_info(): возвращает информацию о книге с указанием автора и жанра.`
# Класс InventoryReport (Отчеты по Инвентарю):

# Методы:
# expired_products(products, current_date): принимает список товаров и возвращает список продуктов питания с истекшим сроком годности на текущую дату.
# no_warranty_products(products, purchase_date, current_date): принимает список товаров и возвращает список электронных товаров, гарантия на которые истекла.
# low_stock_products(products, threshold): возвращает список товаров, количество которых меньше указанного порога.
# list_books_by_genre(products, genre): принимает список товаров и возвращает список книг заданного жанра."""
# from datetime import datetime
# class Product:
#     def __init__(self,name,price,quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def get_info(self):
#         print(f"Товар - {self.name}, Цена: - {self.price}, Количество - {self.quantity}")

#     def purchase(self,quantity):
#          if quantity <= self.quantity:
#             self.quantity -= quantity
#             return f"Вы купили {quantity} {self.name}. Остаток: {self.quantity}"
#          else:
#             return f"Недостаточно {self.name} на складе  Доступно: {self.quantity}"
         
#     def restock(self,quantity):
#          if quantity >= self.quantity:
#              self.quantity += quantity
#              return f"В складе {self.quantity} товаров"
#          else:
#              return f"В складе достаточно товаров"
         
# class FoodProduct(Product):
#     def __init__(self, name, price, quantity,expiration_date):
#         super().__init__(name, price, quantity)
#         self.expiration_date = expiration_date

#     def get_info(self):
#         return f"{super().get_info()},= Срок годности: {self.expiration_date}"
    
#     def is_expired(self, current_date):
#         exp_date = datetime.strptime(self.expiration_date, "%d.%m.%Y")
#         curr_date = datetime.strptime(current_date, "%d.%m.%Y")
#         return curr_date > exp_date
    
# class ElectronicProduct(Product):
#     def __init__(self, name, price, quantity, warranty_years):
#         super().__init__(name, price, quantity)
#         self.warranty_years = warranty_years

#     def get_info(self):
#         return f"{super().get_info()} Гарантия: {self.warranty_years} лет"

#     def remaining_warranty(self, purchase_date, current_date):
#         purchase_date = datetime.strptime(purchase_date, "%d.%m.%Y")
#         current_date = datetime.strptime(current_date, "%d.%m.%Y")
#         warranty_end_date = purchase_date.replace(year=purchase_date.year + self.warranty_years)
#         return current_date <= warranty_end_date
    
# class BookProduct(Product):
#     def __init__(self, name, price, quantity, author, genre):
#         super().__init__(name, price, quantity)
#         self.author = author
#         self.genre = genre

#     def get_info(self):
#         return f"{super().get_info()} Автор: {self.author}, Жанр: {self.genre}"

# class InventoryReport:
#     def __init__(self,products,current_date):
#         self.products = products
#         self.current_date = datetime.strptime(current_date, "%d.%m.%Y")

#     def expired_products(self):
#         expired = [
#             product for product in self.products
#             if isinstance(product, FoodProduct) and product.is_expired(self.current_date.strftime("%d.%m.%Y"))
#         ]
#         return expired
    
#     def expired_products(self):
#         expired = [
#             product for product in self.products
#             if isinstance(product, FoodProduct) and product.is_expired(self.current_date.strftime("%d.%m.%Y"))
#         ]
#         return expired
    
#     def no_warranty_products(self, purchase_date):
#         purchase_date = datetime.strptime(purchase_date, "%d.%m.%Y")
#         no_warranty = [
#             product for product in self.products 
#             if isinstance(product, ElectronicProduct) and product.remaining_warranty(purchase_date.strftime("%d.%m.%Y"), self.current_date.strftime("%d.%m.%Y")) == "Гарантия истекла"
#         ]
#         return no_warranty
    
#     def low_stock_products(self, threshold):
#         low_stock = [product for product in self.products if product.quantity < threshold]
#         return low_stock

#     def list_books_by_genre(self, genre):
#         books_by_genre = [
#             product for product in self.products 
#             if isinstance(product, BookProduct) and product.genre.lower() == genre.lower()
#         ]
#         return books_by_genre

# product1 = FoodProduct("Молоко", 100.0, 20, "01.10.2024")
# product2 = ElectronicProduct("Смартфон", 50000.0, 5, 2)
# product3 = BookProduct("Война и мир", 1500.0, 10, "Лев Толстой", "Роман")
# product4 = FoodProduct("Яблоки", 50.0, 100, "10.10.2024")
# product5 = ElectronicProduct("Ноутбук", 80000.0, 3, 1)

# products = [product1, product2, product3, product4, product5]
# inventory = InventoryReport(products, "15.10.2024")

# for product in products:
#     print(product.get_info())

# print("Просроченные продукты:")
# expired = inventory.expired_products()
# for product in expired:
#     print(product.get_info())

# print("Товары с истекшей гарантией:")
# no_warranty = inventory.no_warranty_products("15.10.2022")
# for product in no_warranty:
#     print(product.get_info())

# print("Товары с низким запасом меньше 10:")
# low_stock = inventory.low_stock_products(10)
# for product in low_stock:
#     print(product.get_info())

# print("Книги жанра 'Роман':")
# books_by_genre = inventory.list_books_by_genre("Роман")
# for book in books_by_genre:
#     print(book.get_info())

# """Задание на тему "Управление Финансовыми Транзакциями" (Python)
# Описание задачи:
# Вам нужно создать систему для управления финансовыми транзакциями в банковском приложении. 
# В системе будут три типа транзакций: платеж, перевод средств и снятие наличных. 
# Каждая транзакция имеет свои уникальные свойства и правила обработки, такие как проверка доступного баланса, 
# расчет комиссии и запись времени транзакции. Также система должна уметь генерировать отчеты по транзакциям, 
# например, показывать транзакции, которые превышают заданную сумму, и подсчитывать общую сумму всех транзакций за указанный период.

# Требования:
# Базовый класс Transaction:

# Атрибуты:
# transaction_id (ID транзакции, строка)
# amount (сумма транзакции, число с плавающей точкой)
# timestamp (время транзакции, строка в формате "ДД.ММ.ГГГГ ЧЧ:ММ")
# Методы:
# get_info(): возвращает информацию о транзакции в формате "ID транзакции: <ID>, Сумма: <сумма>, Время: <время>".
# Класс-наследник PaymentTransaction (Платеж):

# Наследует атрибуты и методы класса Transaction.
# Дополнительные атрибуты:
# payee (получатель платежа, строка)
# Методы:
# get_info(): возвращает информацию о платеже с указанием получателя.
# process_transaction(): проверяет, что сумма больше нуля и выводит сообщение о завершении платежа, например, 
# "Платеж на сумму <сумма> завершен для <получатель>".
# Класс-наследник TransferTransaction (Перевод средств):

# Наследует атрибуты и методы класса Transaction.
# Дополнительные атрибуты:
# sender_account (номер счета отправителя, строка)
# receiver_account (номер счета получателя, строка)
# Методы:
# get_info(): возвращает информацию о переводе с указанием счетов отправителя и получателя.
# process_transaction(): проверяет, что сумма перевода больше нуля, выводит сообщение о переводе средств между счетами, например, 
# "Перевод на сумму <сумма> от <счет отправителя> к <счет получателя> завершен".
# Класс-наследник WithdrawalTransaction (Снятие наличных):

# Наследует атрибуты и методы класса Transaction.
# Дополнительные атрибуты:
# atm_location (место расположения банкомата, строка)
# Методы:
# get_info(): возвращает информацию о снятии наличных с указанием банкомата.
# c проверяет, что сумма больше нуля, и выводит сообщение о снятии, например, 
# "Снятие на сумму <сумма> завершено в банкомате <место расположения>".
# Класс TransactionReport (Отчеты по Транзакциям):

# Методы:
# transactions_above_amount(transactions, amount): принимает список транзакций и возвращает транзакции, превышающие заданную сумму.
# total_amount(transactions): возвращает общую сумму всех транзакций.
# transactions_in_period(transactions, start_date, end_date): возвращает список транзакций, которые были совершены в указанный период."""
# from datetime import datetime

# class Transaction:
#     def __init__(self, transaction_id, amount, timestamp):
#         self.transaction_id = transaction_id
#         self.amount = amount
#         self.timestamp = timestamp

#     def get_info(self):
#         return f"ID транзакции - {self.transaction_id}, Сумма: - {self.amount}, Время: - {self.timestamp}"

# class PaymentTransaction(Transaction):
#     def __init__(self, transaction_id, amount, payee, timestamp=None):
#         super().__init__(transaction_id, amount, timestamp)
#         self.payee = payee

#     def get_info(self):
#         return f"ID транзакции: {self.transaction_id}, Сумма: {self.amount}, Время: {self.timestamp}, Получатель: {self.payee}"

#     def process_transaction(self):
#         if self.amount > 0:
#             print(f"Платеж на сумму {self.amount} завершен для {self.payee}")
#         else:
#             print("Ошибка: сумма платежа должна быть больше нуля.")

# class TransferTransaction(Transaction):
#     def __init__(self, transaction_id, amount, timestamp, sender_account, receiver_account):
#         super().__init__(transaction_id, amount, timestamp)
#         self.sender_account = sender_account
#         self.receiver_account = receiver_account

#     def get_info(self):
#         return (f"ID транзакции: {self.transaction_id}, Сумма: {self.amount}, Время: {self.timestamp}, "
#                 f"Счет отправителя: {self.sender_account}, Счет получателя: {self.receiver_account}")
    
#     def process_transaction(self):
#         if self.amount > 0:  
#             print(f"Перевод на сумму {self.amount} от {self.sender_account} к {self.receiver_account} завершен.")
#         else:
#             print("Ошибка: сумма перевода должна быть больше нуля.")

# class WithdrawalTransaction(Transaction):
#     def __init__(self, transaction_id, amount, timestamp, atm_location):
#         super().__init__(transaction_id, amount, timestamp)
#         self.atm_location = atm_location

#     def get_info(self):
#         return (f"ID транзакции: {self.transaction_id}, Сумма: {self.amount}, Время: {self.timestamp}, "
#                 f"Банкомат: {self.atm_location}")

#     def process_transaction(self):
#         if self.amount > 0:
#             print(f"Снятие на сумму {self.amount} завершено в банкомате {self.atm_location}.")
#         else:
#             print("Ошибка: сумма снятия должна быть больше нуля.")

# class TransactionReport:
#     def __init__(self):
#         self.transactions = []

#     def add_transaction(self, transaction):
#         self.transactions.append(transaction)

#     def generate_report(self):
#         report = "Отчет по транзакциям:\n"
#         for transaction in self.transactions:
#             report += transaction.get_info() + "\n"
#         return report

#     def transactions_above_amount(self, amount):
#         return [trans for trans in self.transactions if trans.amount > amount]

#     def total_amount(self):
#         return sum(trans.amount for trans in self.transactions)

#     def transactions_in_period(self, start_date, end_date):
#         start_date = datetime.strptime(start_date, "%d.%m.%Y")
#         end_date = datetime.strptime(end_date, "%d.%m.%Y")
#         return [trans for trans in self.transactions if start_date <= datetime.strptime(trans.timestamp, "%d.%m.%Y %H:%M") <= end_date]


# transfer = TransferTransaction("TX1002", 2000.0, "25.10.2024 14:30", "1234567890", "0987654321")
# withdrawal = WithdrawalTransaction("TX1003", 500.0, "25.10.2024 15:00", "Центральный банк")
# withdrawal2 = WithdrawalTransaction("TX1004", 3000.0, "26.10.2024 09:00", "Народный банк")

# report = TransactionReport()
# report.add_transaction(transfer)
# report.add_transaction(withdrawal)
# report.add_transaction(withdrawal2)

# print(report.generate_report())  
# print("Транзакции выше 1000:", [trans.get_info() for trans in report.transactions_above_amount(1000)]) 
# print("Общая сумма транзакций:", report.total_amount())  
# print("Транзакции в период с 25.10.2024 по 26.10.2024:", [trans.get_info() for trans in report.transactions_in_period("25.10.2024", "26.10.2024")]) 
