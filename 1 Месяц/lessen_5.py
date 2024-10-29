# # """ Множества set, frozenset """
# # # tup = ("ISlam",)
# # # print(type(tup))
# # students = {"students" : "alikhan", "age" : "14"}
# # # print(students)
# # # print(students["students"])
# # # print(students["age"])
# # students.setdefault('language', 'python')
# # # print(students)
# # # students.pop('age')
# # # print(students)
# # # print(len(students))
# # # students['language'] = 'JavaScript'
# # # students['place'] = 'ItPark'
# # # print(students)
# # # students.keys
# # # print(students.keys())
# # print(students.values())
# contact = {'Islam':'0555555555'}
# while True:
#     command = input("1 - получить все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
#     if command == '1':
#         print(contact)
#     elif command == '2':
#         add_name = input("Введите имя: ").title()
#         add_nnumber= input("Введите номер: ")
#         if add_name not in contact:
#             contact.setdefault(add_name,add_nnumber)
#             print("Контакт успешено добавлен!")
#         else:
#             print("контакт уже добавлен")
#     elif command == "3":
#          delete_contact = input("Введите имя контакта которого хотите удалить: ").title()
#          if delete_contact in contact:
#              contact.pop(delete_contact)
#              print("Контакт успешно удален!")
#          else:
#              print("Контакт не найден: ")
#     elif command == "4":
#               update_cintact = input("Введите имя контакта который хотите обновить: ")
#               number_update = input("Введите номер телефона: ")
#               contact[update_cintact] = number_update
#               print("Контакт успешно обновлен: ")
#     else:
#         print("error")

             
# names = ["Islam","Alihan", "Asko","Semaa"]
# for i in names:
#     if i == "Asko":
#         print("Asko Есть")
#     else:
#         print("Asko Нет")
# for i in range(2,101,2):
#     print(i)
           
# numbers = [1,10,123,12,32123,1231]   
# for i in numbers:
#     if i % 2 == 0:
#         print(i ,"чет") 
#     else:
#         print(i,"нечет") 
# name = "kurmanbek"
# for d in name:
#     if d == "a"
#     print("Буква а есть")
# numbers = []
# for i in range(1.1001):
#     numbers.append(i)
#     print(numbers)
# number = [10,20,30,40,50]
# for i,n in enumerate(number):
#     print(i,n)
# import random

# n = 0
# rabdom_number = random.randint(1,10000)
# print(rabdom_number)
# while True:
#     n +=1
#     print(n)
#     if n == rabdom_number:
#         break
import time
process = 0
while True:
    print(str(process)+ "% HACK")
    process +=1
    time.sleep(0.1)
    if process == 101:
        print("SUCCESSFULY HACKED")
        break