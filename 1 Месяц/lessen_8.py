"""лямбда функции"""""
# def helloworld(x):
#     return x * x
# print(helloworld(10))
###############################################################################################

# hello = lambda x: x * x
# print(hello(10))
###############################################################################################

# def mult(num1 : int = 2, nmu2 : int = 2)-> int:
#     return num1 * nmu2
# print(mult(10,5))
# print(mult())
###############################################################################################

# lambda_mult = lambda num1,num2: num1*num2
# print(lambda_mult(10,5))
###############################################################################################

# print((lambda num1,num2: num1*num2)(10,5))
###############################################################################################

# numbers = [10,3,4,234,2,3,2,5]
# chet = []
# def chet_func(num : list)->list:
#     for n in num:
#         if n % 2 == 0:
#             chet.append(n)
#             return chet
#         print(chet_func(numbers))
###############################################################################################

# numbers = [10,3,4,234,2,3,2,5]
# chet = (list(filter(lambda num : num % 2 == 0, numbers)))
###############################################################################################
# print(list(filter(lambda num: num % 2 == 0,[10,3,4,234,2,3,2,5])))
###############################################################################################
# num = [10,20,30,40,50]
# lst = []
# def mult_two(num_list : list)->list:
#     for n in num:
#         lst.append(n * 2)
#         return lst
#     print(mult_two(num))
###############################################################################################
# numbers = [10,20,30,40,50]
# lst = list(map(lambda num_list : num_list * 2, numbers))
# print(lst)
###############################################################################################
# print(list(map(lambda list_num : list_num * 2,numbers = [10,20,30,40,50])))
###############################################################################################
"""Модули"""
# import time
# def get_time():
#     return time.ctime()
# # print(get_time())
# def hello():
#     return "Hello "




# prices = [10, 50, 30, 75, 100, 20]
# num1 = list(filter(lambda num_list: num_list > 0, prices))
# num2 = list(map(lambda num : num * 1.1, num1))
# print("Цены в долларах:", num2)


# import time
# def get_time():
#     return time.ctime()
# # print(get_time())

def hello():
    return "Hello "
print(hello())

num1 = lambda i: 10,20,40
num2 = list(map(lambda num : num1 / 3))
print(num2)



# hello = lambda x: x * x
# print(hello(10))