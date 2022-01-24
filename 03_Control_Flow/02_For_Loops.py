# For Loops

# l = ['a', 'b', 'c']

# for letter in l:  #letter is each variable in turn in L
#     if letter == 'b':
#     # print(letter)
#         print(letter.upper())
#     else:
#         print(letter)

# for i in range(1, 10 + 1):
#     for letter in l:
#         print(i, letter)  # finishes looping l before outside loop is done

me = {'name': 'David', 'age': 375, 'job': 'trainer'}

# for thing in me:
#     print(me[thing])
#
# for thing in me.values():
#     print(thing)
#
# for thing in me.items():
#     print(thing)

# for key, value in me.items():
#     if key == 'age':
#         print(f"My {key} is {value} years old")
#     else:
#         print(f"My {key} is {value}")  # items gives key and value

# letters = ['a', 'b', 'c']
#
# for thing in enumerate(letters):
#     print(thing)
#
# for index, letter in enumerate(letters):
#     print(f"{letter} is in position {index}")

for char in "Hello World!":
    print(char)