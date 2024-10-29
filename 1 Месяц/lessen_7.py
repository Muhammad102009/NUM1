"""""Задание 1: Конвертация типов и работа с циклами
Напишите функцию convert_and_calculate, которая принимает список строк, каждая из которых представляет число (например, ["5", "12", "9", "3"]).

Функция должна преобразовать элементы списка в целые числа.
Затем функция должна пройтись по преобразованному списку с помощью цикла и найти сумму всех чисел, которые являются чётными.
Функция должна вернуть полученную сумму."""
# def convert_and_calculate(num1):
#     num2 = [int(x) for x in num1]
#     even_sum = 0
#     for num in num2:
#         if num % 2 == 0:
#             even_sum += num
#     return even_sum
# num1 = ["5", "12", "9", "3"]
# result = convert_and_calculate(num1)
# print(result)
""""Задание 2: Работа с типами данных и циклами в функции
Создайте функцию string_lengths, которая принимает список строк, находит длину каждой строки, 
и если длина строки меньше 5 символов, она должна быть преобразована в целое число, представляющее длину этой строки.
Если длина строки больше или равна 5 символов, строка остается неизменной.
Функция должна вернуть новый список, состоящий из чисел и строк."""
# def string_lengths(num):
#     num1 = []
#     for num2 in num:
#         if len(num2) < 5:
#             num1.append(len(num2))
#         else:
#             num1.append(num2)
#     return num1
# num = ["23", "1224", "55555", "11", "22"]
# print(string_lengths(num))
""""Задание 3: Конвертация и циклы для вычисления среднего значения
Напишите функцию calculate_average, которая принимает список значений разного типа (например, целые числа, строки, вещественные числа).

Функция должна пройтись по списку с помощью цикла и конвертировать все строки, представляющие числа, в целые или вещественные числа (если это возможно).
Затем функция должна вычислить и вернуть среднее арифметическое всех числовых значений."""""
# def calculate_average(num):
#     num1 = ["sko","324","2.23","12","ddsfw"]


# analyze_text(text):
#     words = text.split()
#     word_count = len(words)
#     sentence_count = sum(text.count(end) for end in ['.', '!', '?'])
#     longest_word = max(words, key=len) if words else ''
#     lower_text = text.lower()
#     return {
#         'word_count': word_count,
#         'sentence_count': sentence_count,
#         'longest_word': longest_word,
#         'lower_text': lower_text
#     }
# text = "Если устал сидеть то встань. Не болейте раком болейте стоя. P.S Стетхом"
# result = analyze_text(text)
# print("Количество слов:", result['word_count'])
# print("Количество предложений:", result['sentence_count'])
# print("Самое длинное слово:", result['longest_word'])
# print("Преобразованный текст:", result['lower_text'])



