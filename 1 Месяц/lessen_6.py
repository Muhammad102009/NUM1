# """"Функции"""
# hollo_world = "Hello world"   # змеиный регистр
# HelloWorld = "Hello world"    # Верблюжий регистер
# def calc():
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(num1 + num2)
# calc()
# def calc(num1,num2):    #num1 И num2 это параметры
#     print(num1 + num2)
# calc(214,273)    # К параметрам num1 И num2 передаются аргументы
# def hello_world():
#     print("Hello world")
# hello_world()
# def func_while():
#     while True:
#         print("ITpark")
# func_while()
# def itpark(name: str)-> str:
#     print("Здраствуйте, " + name)
# itpark("Asyl")
# def add(num1 : int,num2 : int):
#     print(num1 + num2)
# def sub(num1 : int,num2 : int):
#     print(num1 - num2)
# def milt(num1 : int,num2 : int):
#     print(num1 * num2)
# def div(num1 : int,num2 : int):
#     print(num1 / num2)
# def calculator(num1 : int,operator : str,num2 :int):
#     if operator == "+":
#      add(num1,num2)
#     elif operator == "-":
#      sub(num1,num2)
#     elif operator == "*":
#      milt(num1,num2)
#     elif operator == "/":
#      div(num1,num2)
#     else:
#        print("Error")
# calculator(12346,"/",2)

# def chet_nechet(num : int = 2):    # 2 это значение поумолчанию
#     if num % 2 == 0:
#       print(num,"Четное")
#     else:
#       print(num,"Нечетное")
# chet_nechet(222)
# numbers = [10,20,30,1,3,5,11]
# tup_numbers = (2,3,12,412,42,10)

# def list_chet(list_num : list)->str:
#     for num in list_num:
#         if num % 2 == 0:
#             print(f"{num},Четный")
#         else:
#             print(f"{num},Нечотный")
# list_chet(numbers)
# list_chet(tup_numbers)
# def hello(num1 : int,num2 : int):
#     return num1 + num2
# print(hello(20,30))
def calculate_area():
    num1 = int(input("Введите длину: "))
    num2 = int(input("Введите ширину : "))
    if num1 > 0 and num2 > 0:
        print( num1 * num2 )
    else:
        return"число не коректно"
calculate_area()
