"""Исключение try"""
# def div(num1 : int = 2,num2 : int = 2)->float:
#     try:
#      return num1 / num2
#     except ZeroDivisionError:
#         return "Я не умею делить на ноль"
# print(div(10,0))

# def calculator():
#     while True:
#         try:
#             num1 = int(input("Введите первое число "))
#             operator = (input("+ , - , * , /: "))
#             num2 = int(input("Введите второе число "))
#             if operator == "+":
#                 print(num1 + num2)
#             elif operator == "-":
#                  print(num1 - num2)
#             elif operator == "*":
#                 print(num1 * num2)
#             elif operator == "/":
#                  try:
#                     print (num1 / num2)
#                  except ZeroDivisionError:
#                         print("Я не умею делить на ноль")
#                  else:
#                     print("Оператор не найден")
#         except ValueError:
#                         print("Введите целые числа")
# calculator()

# try:
#     print(10 / 0)
# except:
#     print("Ошибка")
#     # raise ValueError("Делать нам нечего спецально выводим ошибку: ")
# finally:
#     print("Я буду работать: ")

# f = open("ITpark.txt",'w')
# f.write("Hello itpark")
# f.close()

# r = open('ITpark.txt','r')
# print(r.read())
# r.close()

# import time
# def safe_login_passord(login : str, password : str)->str:
#     password_file = open("login_password.txt", 'a+')
#     if login and len(password)>= 8 and ' ' not in password:
#         password_file.write(f'{login}, {password}, {time.ctime()}\n')
#     else:
#         return "Неправильный логин или пароль"
#     password_file.close()
#     return "Логин и пароль сохранен"
# print(safe_login_passord("bilol","sodiq.009"))
# print(safe_login_passord("abdurasuljanowmuhammadsodiq008@gmail.com","sodiq.009"))
"""Задание: Найти пары чисел
У вас есть список целых чисел. Нужно написать функцию find_pairs, которая находит все пары чисел, чья сумма равна заданному числу target_sum.

Условия:
Входные данные: список целых чисел и целое число target_sum.
Нужно найти все уникальные пары чисел, сумма которых равна target_sum.
Каждую пару можно использовать только один раз (например, если числа 3 и 7 образуют пару, то их нельзя повторно использовать в других парах).
Порядок чисел в парах не имеет значения (пара [3, 7] и [7, 3] считается одной парой)."""
# num1 = [1,2,3,4,,1,2,3,4]
# turget_sum = 5
# def find_pairs():
#     for 