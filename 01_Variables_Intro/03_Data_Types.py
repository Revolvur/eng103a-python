# Numeric!

# control + / to comment all or uncomment
#
# i = 375  # int
# f = 3.75  # float
# c = 3j + 2  # complex
#
# print(c, type(c))
#
# add = 3 + 5
# subtract = 3 - 5
# multiply = 3 * 5
# divide = 3 / 5
# power = 3 ** 5  # three to the power of 5
# modulo = 3 % 5  # gives remainder after division
#
# print(13 % 3)  # 4 * 3 = 12, 13 - 12 = 1
# print(12 % 3)  # = 0
#
# print(13 / 3)  # 4.33333333333333
# print(13 // 3, 13 % 3)  # Division to a whole number = 4 to the lowest number with remainder 1
#
# third = 1 / 3
# print(third)
# print(third * 3)  # float
#
# print(25 ** 0.5)  # square root

# Strings!

# single = 'hi'
# double = "yo"
# # mix = 'String in both"  will not work as you can't mix and match
#
# # failure = 'This is David's string'
#
# single_in_double = "This is David's string"
# double_in_single = 'This is a "string"'
# both = "This is David's \"string\""
# print(both)

# Indexing and slicing

# hi = "Hello World!"
# print(hi[0])  # Python starts counting at zero!
# print(hi[6])
# print(hi[-1])
# print(hi[0:7])  # Hello, everything up to but not including 7
# print(hi[3:8])  # lo Wo
#
# print(len(hi))  # length of string

# Methods

# white_space = "     lots of white space      "
# print(len(white_space))
# print(white_space.strip())  # .methods
# print(white_space.lstrip())  # .methods l is from left and r from right
# white_space2 = "......lots of white space......"
# print(white_space2.strip("."))
# print(white_space.upper())
# print(white_space
#       .strip()
#       .capitalize())
#
# print(white_space.count(" "))  # how many times it occurs
# print(white_space.strip().count(" "))  # how many times it occurs
# print(white_space.replace("o", "ooooo").replace("i", "oooo").replace("a", "ooooo"))  # replaced 'o' with 'ooooo'
#
# print(white_space)  # these either change the thing or return
#
# # F-Strings
#
# pi = 3.14159265359
# print(pi)
# print(f"Pi to 3dp: {pi:.3f}")  # 3 d.p and f means float
# print(f"Pi to 3dp: {pi:.5f}")
# print(f"Pi to 3dp: {pi:.0f}")
#
# score = 16
# max_score = 26
#
# print(f"You scored {score / max_score}")
# print(f"You scored {score / max_score:.2f}")
# print(f"You scored {score / max_score:%}")
# print(f"You scored {score / max_score:.2%}")
# print(f"You scored {score / max_score:.0%}")


# Boolean

t = True
f = False

# print(t, type(t))
#
# print(3 + 2 == 5)
# print(12 % 3 == 0)
# print(5 != 5)
# print(1 < 100)
# print(100 < 1)
# print(5 < 5)
# print(5 <= 5)
# print(5 >= 5)

# age = 19
# drink = 'alcohol'
#
# print(age > 18 and drink == 'alcohol')
#
# age = 14
# drink = 'alcohol'
#
# print(age > 18 and drink == 'alcohol')
# print(age > 18 or drink == 'alcohol')

# hi = "Hello World"
# print(hi.replace(" ", "").isalpha())
# print(hi.strip(" World").isalpha())
# print(hi.lower().islower())  # only cares about letters e.g. SJDJ 2323!! is still true
# print(hi.upper().isupper())  # only cares about letters
# print(hi.endswith("rld"))
# print(hi.startswith("He"))
# print(hi.isalnum())  # checks for letters and numbers

# print(bool(1))
# print(bool(0))
# print(bool(32423523523523523523523))
# print(bool(-4.5))  # bool always return true unless 0
#
# print(int(False))
# print(int(True))
# print(bool("")) #  string of length zero equals FALSE
#
# empty = ""
# print(empty, type(empty), bool(empty))

# none

n = None

print(n, type(n))  # normally used as place holder

print(n is None)

print(type(15) is int)  #  'is' to check class etc





