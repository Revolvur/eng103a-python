# i = 1
# keep_looping = True
#
# while keep_looping:
#     print(i)
#     if i == 5:
#         print('FIVE PARTY!')
#         keep_looping = False
#     i += 1
#     print('Start again')
#
# print('End of loop')
#
# for x in ['a', 'b', 'c', 'd', 'e']:
#     i = 100
#     while i < 110:
#         print(x, i)
#         if i == 105 and x == 'b':
#             break
#         i += 1

# age = input("What is your age?\n")
#
# if age.isdigit():
#     int_age = int(age)
# else:
#     print("Please enter age in digits.")
#     age = input("What is your age?\n")

# prompt_user = True
# age = None
# while prompt_user:
#     age = input("What is your age\n")
#     if age.isdigit() and int(age) <= 119:  # check for negative numbers etc
#         prompt_user = False
#     else:
#         print("Please provide a valid age in digits.")
#
# print(f"Double your age is {int(age) * 2}.")

# Max age = 119

prompt_user = True
age = None
while prompt_user:
    age = input("What is your age?\n")
    if age.isdigit():
        if int(age) <= 119:
            prompt_user = False
        else:
            print("You are not that old.")
    else:
        print("Please provide a valid age in digits.")

print(f"Double your age is {int(age) * 2}.")