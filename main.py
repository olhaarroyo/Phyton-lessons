# Завдання 1: Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр.
# # Отриманий результат повертається із функції.
# from random import *
#
# numbers = [randint(1, 20) for _ in range(5)]
# print("List: ", numbers)
#
# def calculate_product_of_list(input_list):
#     product = 1
#     for num in input_list:
#         product *= num
#     return product
# result = calculate_product_of_list(numbers)
# print("Result: ", result)



# Завдання 2

# numbers = [11, 23, 56, 90, 87]
# print(numbers)

# def find_min_value(numbers):
#     if not numbers:
#         return None
#     min_value = numbers[0]
#     for num in numbers:
#         if num < min_value:
#             min_value = num
#     return min_value
# min_value = find_min_value
# # print("min", min_value)
# result = find_min_value(numbers)
# print("Result: ", result)

# Завдання 3
# Напишіть функцію, яка визначає кількість простих чисел у списку цілих. Список передається як параметр.
# Отриманий результат повертається із функції.

# from random import *
#
# numbers = [randint(1, 30) for _ in range(10)]
#
# print(numbers)
#
# def is_simple(number: int) -> bool:
#     if number < 2:
#         return False
#
#     for num in range(2, number):
#         if number % num == 0:
#             return False
#     return True
#
# def get_simple_numbers(nums: list) -> int:
#     counter = 0
#     for number in nums:
#         if is_simple(number):
#             counter += 1
#             print(number)
#
#     return counter
#
# try:
#     result = get_simple_numbers(numbers)
#     print(f"Simple numbers count: {result}")
# except Exception as error:
#     print(Error)

# Завдання 4

# list = [22, 11, 56, 1, 4, 4, 6, 7]
# print("List: ", list)
#
# def remove_numbers(list, number_to_remove):
#     digit_to_remove = list.count(number_to_remove)
#     while number_to_remove in list:
#         list.remove(number_to_remove)
#
#     return digit_to_remove
# number_to_remove = 4
# digit_to_remove = remove_numbers(list, number_to_remove)
# print("new list: ", list)

# Завдання 5

# my_list1 = [2, 6, 98, 45, -9]
# my_list2 = [11, 6, 89, 45, 9]
# print("a: ", my_list1)
# print("b: ", my_list2)
#
#
# def merge_list(my_list1, my_list2):
#     merged_list = my_list1 + my_list2
#     return merged_list
#
# result = merge_list(my_list1, my_list2)
# print("Merged list: ", result)

# Завдання 6

# def list_pow(numbers, degree):
#     for i in range(len(numbers)):
#         numbers[i] **= degree
#
#     return numbers
#
# numbers = [10, 2, 5, 111, 55]
# print(numbers)
# numbers = list_pow(numbers, 2)
# print(numbers)
