# Exercise 1: Reverse a list in Python

print("Q1")

list1 = [100, 200, 300, 400, 500]

list1.reverse()

print(list1, "\n")

# Exercise 2: Concatenate two lists index-wise

print("Q2")

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

# result = zip(list1, list2)
#
# result_zip = list(result)

# zip concatenates them together, i and j go through each string and concatenate
result_zip = [i + j
              for i, j in zip(list1, list2)]

print(result_zip, "\n")

# Exercise 3: Turn every item of a list into its square

print("Q3")

numbers = [1, 2, 3, 4, 5, 6, 7]

# go through the list and * each by itself
square_num = []

for i in numbers:
    square_num.append(i * i)

print(square_num, "\n")

# Exercise 4: Concatenate two lists in the following order
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

print("Q4")

list1_0 = ["Hello ", "take "]
list2_0 = ["Dear", "Sir"]

# new_list_following_order = []

# new_list_following_order = [i + j for i, j in zip(list1_0, list2_0)]

# i goes through list 1 and j goes through list 2, each loop they concatenate into a string through the list

new_list_following_order = [
    i + j for i in list1_0
    for j in list2_0
]

print(new_list_following_order, "\n")

# Exercise 5: Iterate both lists simultaneously
print("Q5")
# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in
# -original order and items from list2 in reverse order.

list1_1 = [10, 20, 30, 40]
list2_1 = [100, 200, 300, 400]

list2_1.reverse()

# for i in list1_1:
#     for j in list2_1:
#         print(i, " ", j)
zipped_list_q5 = zip(list1_1, list2_1)
# print(list(zipped_list_q5)) # [(10, 400), (20, 300), (30, 200), (40, 100)]

for a, b in zipped_list_q5:  # a and b going through each string
    print(a, b)
print("\n")
#  Exercise 6: Remove empty strings from the list of strings
print("Q6")

list1_3 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

filter_list1 = filter(None, list1_3)
print(list(filter_list1), "\n")

