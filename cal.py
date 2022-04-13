# # Program make a simple calculator

# # This function adds two numbers
# def add(x, y):
#     return x + y

# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# # This function divides two numbers
# def divide(x, y):
#     return x / y


# print("Select an operation.")
# print("1)","+.Add")
# print("2)","-.Subtract")
# print("3)","*.Multiply")
# print("4)","/.Divide")

# while True:
#     # take input from the user
#     choice = input("Enter choice(+/-/*//): ")

#     # check if choice is one of the four options
#     if choice in ('+', '-', '*', '/'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '+':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '-':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '*':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '/':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
#         # check if user wants another calculation
#         # break the while loop if answer is no
#         next_calculation = input("Let's do next calculation? (y/n): ")
#         if next_calculation == "n":
#           break
    
#     else:
#         print("Invalid Input")

# print()



import pytz
from datetime import datetime
tz = pytz.timezone('UTC')
naive_time = datetime.strptime('2016-04-05 15:00', '%Y-%m-%d %H:%M')
tz_time = tz.localize(naive_time)
london_tz = pytz.timezone('Europe/London')
london_time = tz_time.astimezone(london_tz)
print(london_time)