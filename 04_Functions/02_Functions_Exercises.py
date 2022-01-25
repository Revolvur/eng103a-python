# fizzbuzz code as functions

print("\nQ1a\n")


# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

# def divisor(num):
#     divisible_num = 0
#     for i in range(1, num):


# n = "1, 2, 3, 4"
# f = 12
# a = f/2
# b = a/2
# c = b/2
# d = str(f"{a}, {b}, {c}")
# print(c)
# split = d.split(",")
# print(split)

#
# split = n.split(",")
# print(split)

def a1a():
    divisor = int(input("Enter a number:\n"))
    final = []
    for x in range(1, divisor + 1):
        if divisor % x == 0:
            final.append(x)
    print(final)


a1a()
#
#
print("\nQ1b\n")


#
# # Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# # is a factor of the other, false otherwise
# # (bonus points if you call your previous function within this function
#
# # A1b:
#
#
def factor(num1, num2):
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}")
    elif num2 % num1 == 0:
        print(f"{num2} is divisible by {num1}")
    else:
        print("neither number is divisible by the other")


factor(10, 5)
#
# print("\nQ2a\n")
# # # Q2a: write a function which takes a letter (as a string) as an input and outputs its position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


#
# # A2a:

def find_alphabetical_pos(letter):
    # letter = input("Enter a character of the alphabet, please.\n")
    return alphabet.index(letter)
    # print(f"The position of your letter in the alphabet is {place}.")


print(find_alphabetical_pos("z"))

print("\nQ2b\n")


# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def id_number(word):
    result = ""
    for item in word:
        number = find_alphabetical_pos(item)
        result += str(number)
    return result


print(id_number("pele"))

print("\nQ2c\n")


# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

def password(word):
    total = 0
    num = id_number(word)
    for i in num:
        #    print(i)
        total += int(i)
    # print(total)
    true_total = int(num) - total
    return true_total


print(password("pele"))

print("\nQ3a\n")


# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def check(number):
    num_str = str(number)
    if num_str.isdecimal():
        print("You have passed validation checks")
    else:
        print("Your number is not a digit!")
        exit()



def prime(number):
    check(number)
    isPrime = True
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                isPrime = False
                break
    if isPrime:
        print("Prime number.")
    else:
        print("Not a prime number.")


prime(1000003)

print("\nQ3b\n")

# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:


# check(12)
