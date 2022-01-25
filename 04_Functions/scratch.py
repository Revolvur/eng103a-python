# def getfive():
#     print(5)
#
# my_number = getfive()
# print(my_number)
#
# def addfive(input_number):
#     result = input_number + 5
#     return result
#
# new_numb = addfive(69)
# print(new_numb)
#
# def add(num1, num2):
#     ans = num1 + num2
#     return ans
#
# print(add(2349, -300))

# prime numbers
# num = 13
# if num > 1:
#     for i in range(2, num // 2):
#         if (num % i) == 0:
#             print("Primee")

# isPrime = False
#
# num = 13
#
# if num > 1:
#     for i in range(2, num+1):
#         if (num % i) == 0:
#             isPrime = True
#             break
# if isPrime:
#     print("Prime")
# else:
#     print("Not prime")

# def prime(number):
#     try:
#         isPrime = True
#         if number > 1:
#             for i in range(2, number):
#                 if (number % i) == 0:
#                     isPrime = False
#                     break
#         if isPrime:
#             print("Prime number.")
#         else:
#             print("Not a prime number.")
#     except TypeError:
#         print("TypeError")
#         prime()
#
# prime("13")

def check(number):
    num_str = str(number)
    if not num_str.isdecimal():
        print("Your number is not a digit!")
        exit()
    else:
        print("You have passed validation checks")


check()
