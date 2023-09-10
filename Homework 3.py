# try:
#     user_select = int(input("Enter menu number: "))
#
#     if user_select == 1:
#         print("Monday")
#     elif user_select == 2:
#         print("Tuesday")
#     elif user_select == 3:
#         print("Wensday")
#     elif user_select == 4:
#         print("Thursday")
#     elif user_select == 5:
#         print("Friday")
#     elif user_select == 6:
#         print ("Saturday")
#     elif user_select == 7:
#         print ("Sunday")
#     else:
#         print("Incorrect!")
#
#
# except Exception as e:
#     print(f"Error: {e}")

# Завдання 1
# number1 = 8
# number2 = 3
# number3 = 4
# sum_result = number1 + number2 + number3
# print("result:", sum_result)

#Завдання 3

# number = 3553
# number_str = str(number)
# product_result = 1
# for digit in number_str:
#     product_result *= int(digit)
# print("result:", product_result)
######################################

#Завдання 2
# Side = int(input("Enter the length: "))
# Height = int(input("Enter the height: "))
# area = Side * Height
# print("Result:", area)
#
#git
# print("hello world")
# print ("2")
# n1 = 10 + 20 * 2
# n2 = 20

# n1, n2 = 10, 20 + 10
# print(n1 > n2)
# print (n1 >= n2)
# print(n1 < n2)
# print (n1 <= n2)
# print (n1 == n2)
# print(n1 != n2)

# print(1 == 1 and 3 == 3)
# print(1 == 1 or 2 == 3)
# is_valid = False
# print(is_valid)
# print(not is_valid)

# print("hello" in "hello world")

# hours = int(input("Enter hours: "))

# if hours >= 12:
#     print("PM")
# else:
#     print("AM")
# hours = int(input("Enter hours: "))
# if hours >= 12 and hours < 24:
#     print("PM")
# elif hours >= 0 and hours < 12:
#     print("AM")
# else:
#     print("Incorrect hours!")

##########################

# film_rating = int(input("Enter film rating:  "))
# if film_rating == 4 or film_rating == 5:
#     print("OK")
# else:
#     print("Not OK")

###########################

# num = float(input("Enter the number: "))
# print(num)
# print(int(num))

# try:
#     name = input("Enter your name: ")
#     if 1 < len(name) <= 20:
#         print(f"Hello, {name}")
#     else:
#         raise Exception("Please enter valid name!")
# except Exception as e:
#     print(f"Error: {e}")

##########

# for i in range(5):
#     # print("Hello")
#     print(i, end=" ")
#
#
# print()
#
# for i in range(2, 5):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# for i in range(1, 5, 2):
#     # print("Hello")
#     print(i, end=" ")
#
# print()
#
# start, end = 1, 10
# # print("Hello")
# for i in range(start, end + 1):
#     print(i, end=" ")
#
# start, end = 1, 10
# for i in range(end, start -1, -2):
#     print(i, end=" ")

#
# for number in range(start, end + 1):
#     is_simple = True
#
#     if number < 2:
#         continue
# if start > end:
#     start, end = end, start
#
# for number in range (start, end +1):
#     is_simple = True
#     if number < 2:
#         continue
#         for i in range(2, number):
#             if number % i == 0:
#                 break
#     if is_simple:
#         print(number, end="")
##############################
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print()
#############################

# text = '''
# urehwefhw
#     eofjweiov
#         hfowehg
# '''

# dogs, cats = 12, 15
# redult = f"Dogs {dogs} and cats {cats})"
# print(result)
#
# result = "Dpgs {1} and cats {}".format(*args: dogs, cats)
# print(result)
#
# result = "Dpgs {1} and cats {0}".format(*args: dogs, cats)
# print(result)
#
# result = "Dpgs {1} and cats {1}".format(*args: dogs, cats)
# print(result)

# message = "hello world"
# print(message[0])
# print(len(message))
# print(message[len(message) -1])
# print(message[-1])

# sentence = "Hello, wolrd"
# for letter in sentence:
#     print(letter, end=" ")
# print()
#
# for i in range(len(sentence)):
#     print(sentence[i], end= " ")

# sentence = "Hello, world"
# print(sentence[:])
# print(sentence[0:])
# print(sentence[2:])
# print(sentence[2:8])
# print(sentence[1:10:2])
# print(sentence[::-1])

# name = "Vasya"
# surname = "Petrov"
# age = 33
# fullname = name + " " + surname + " " + str(age)
# print(fullname)

# text = "hello world"
# print(text.find("l"))
# print(text.rfind("hello"))

# text = "hello world"
# for i in range(len(text)):
#     print(i)