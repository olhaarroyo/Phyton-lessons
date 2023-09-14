# Завдання 1
# try:
#     week_day_number = int(input("Enter week day number: "))
#     match week_day_number:
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wensday")
#         case 4:
#             print("Thursday")
#         case 5:
#             print("Friday")
#         case 6:
#             print("Saturday")
#         case 7:
#             print("Sunday")
#         case _:
#             print("Incorrect week day number")
# except ValueError:
#     print("Enter only numbers")
# except Exception as error:
#     print(error)
##################################
# Завдання 2
# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     result = (num1 >num2)
#     print(f"Result: {result}")
# except ValueError as error:
#     print("Enter only numbers!")
#     print(f"ValueError: {error}")
# else:
#     min_num = min(num1, num2)
#     max_num = max(num1, num2)
#
#
# finally:  print(f" {min_num}, {max_num}")
#Завдання 2 V2
# try:
#     first_number = int(input("Enter first number: "))
#     second_number = int(input("Enter second number: "))
#     if first_number > second_number:
#         print(second_number, "and", first_number)
#     elif second_number > first_number:
#         print(first_number,"and", second_number)
#     else:
#         print("Equals")
# except ValueError:
#     print("Enter only number please")
# except Exception as error:
#     print(error)
#############################

# Завдання 3

# try:
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     math_action = input("Enter math action: + - * /")
#
#     match math_action:
#         case "+":
#             print(num1, math_action, num2, "=", num1 + num2)
#         case "-":
#             print(num1, math_action, num2, "=", num1 - num2)
#         case "*":
#             print(num1, math_action, num2, "=", num1 * num2)
#         case "/":
#             print(num1, math_action, num2, "=", num1 / num2)
#         case _:
#             raise Exception("Incorrect math action")
# except ValueError:
#     print("Enter only number please")
# except ZeroDivisionError as error:
#     print("impossible to divide by zero")
# except Exception as error:
#     print(error)
