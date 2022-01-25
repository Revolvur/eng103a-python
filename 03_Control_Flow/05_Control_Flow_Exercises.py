# # A1a:
#
# print("\nQ1a\n")
# # Q1a: Print only the first 5 numbers in this list
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
#
# Q1a = []
# for index in range(0, 5):
#     Q1a.append(x[index])
#
# print(Q1a)

# print("\nQ1b\n")
# # Q1b: Now print only the even numbers in this list (the elements that are themselves even)
# x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]
#
# for index in x:  # can also use x
#     if index % 2 == 0:
#         print(index)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:

# i = 0
# while i < 5:
#     for index in x:
#         if index % 2 == 0:
#             print(index)
#         i += 1

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:

# first_letters_name = []
# first_letters = 0
# full_name = 0
# for index in names:
#     first_letters_name.append(names[first_letters][full_name])
#     first_letters += 1
#    #  full_name += 1
# print(first_letters_name)

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:


# name_order = 0
# your_string = []
# for i in names:
#     your_string.append(names[name_order].find(' '))
#     name_order += 1
#
# print(your_string)

# print("\nQ2c\n")
# # Q2c: from the list of names, create another list that consists of the first and last initial of each individual
# names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]
#
# # A2c:
#
# first_name = 0
# last_name = 1
# initials = []
# for name in names:
#     x = name.split(" ")
#     initials.append(x[first_name][0] + "." + x[last_name][0] + ".")
# print(initials)
#


# print("\nQ3a\n")
# # Q3a: Here is a list of lists, print only the lists which have no duplicates
# # Hint: This can be easily done by using sets as a set does not contain duplicates
# list_of_lists = [[1,5,7,3,44,4,1],
#                  ["A", "B", "C"],
#                  ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
#                  ["one", "Two", "Three", "Four"]]
#
#
# # A3a:
#
# for sublist in list_of_lists:
#     set_no_dupes = set(sublist)
#     if len(set_no_dupes) == len(sublist):
#         print(sublist)

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
#
# condition = True
# while condition:
#     user_input = int(input("Enter a number greater than 100\n"))
#     if user_input >= 100:
#         print(f"You have entered {user_input}")
#         condition = False
#     else:
#         print("Please enter a number greater than 100.")

print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

condition = True
while condition:
    user_input = int(input("Enter a number greater than 100\n"))
    if user_input >= 100:
        print(f"You have entered {user_input}\n")
        prime = True
        for i in range(2, user_input // 2):
            if (user_input % i) == 0:
                prime = False
                print("Your number is also a prime number!\n")
            break
        if not prime:
            print("Your number is not a prime number.\n")
        condition = False
    else:
        print("That number is not greater than 100.\n")
