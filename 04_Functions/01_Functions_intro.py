# def woof(number_of_woofs):
#     # number_of_woofs = 17
#     for i in range(number_of_woofs):
#         print("WOOF!")
#
#
# woof(1)
# woof(17)

# def woof(number_of_woofs):
#     print("Woof!\n" * number_of_woofs)
#
# def greeting(name):
#     print(f"Hello to you, {name}!")
#
#
# greeting("David")
# woof(5)

# def double_plus_num(num1, num2=1):  # can add number to num 2, so it defaults in case there is no number
#     ans = (num1 * 2) + num2
#     # print(str(ans))  # things in a function are only available from within that function and not globally
#     return ans  # returns to global scope
#
#
# # cannot do num1 = 1, num2 because 2nd argument needs to go first over default argument
# print(double_plus_num(1))
#
#
# # def shopping(*items):  # *items multiple arguments (multi args)
# #     # print(items, type(items))
# #     for item in items:
# #         print(f"Don't forget to buy a {item}.")
# #
# #
# # shopping("banana", "apple", "orange")
#
# def shopping(name, *items, shout=False):  # *items multiple arguments (multi args)
#     # print(items, type(items))
#     if shout:
#         name = name.upper()
#     for item in items:
#         print(f"{name}! Don't forget to buy a {item}!")
#
#
# shopping("David", "banana", "apple", "orange", shout=True)  # default arguments need to be specified


# def greeting(name):
#     print(f"Hello to you, {name}")
#
# greeting(24601)

# Type hints

def greeting(name: str = "David"):
    print("Hello to you, " + name + ".")


greeting()


def double_plus_num(num1: int, num2: int):
    ans = str((num1 * 2) + num2)
    return ans


x = double_plus_num(5, 6)
print(x)