def option_b():
    for i in range(1, 101):  # executes code for fizzbuzz activity
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


def option_c():
    exit()


def option_a():
    fizz_alt = None
    buzz_alt = None
    range_start = None
    range_end = None
    while True:
        if range_start is None:  # if nothing in range_start
            range_start = input("Enter starting range in whole numbers:\n")
            if not range_start.isdigit():  # if not a whole number
                print("Please enter a whole number.\n")
                range_start = None  # resets to None
            continue
        elif range_end is None:  # if nothing in range_end
            range_end = input("Enter end range in whole numbers:\n")
            if not range_end.isdigit():  # if not a whole number
                print("Please enter a whole number.\n")
                range_end = None  # resets to None
            continue
        # code exits IF statement if variables are not None
        fizz_alt = input("Enter the alternative word for fizz:\n")
        buzz_alt = input("Enter the alternative word for buzz:\n")
        break  # breaks while loop and continues onto next line

    for i in range(int(range_start), int(range_end) + 1):  # executes code for fizzbuzz activity
        if i % 3 == 0 and i % 5 == 0:
            print(fizz_alt + buzz_alt)
        elif i % 3 == 0:
            print(fizz_alt)
        elif i % 5 == 0:
            print(buzz_alt)
        else:
            print(i)


# initialise variables, get user input, set up counter, give counter to user, user enters input
# validation checks to see if user enters A-C (upper), 5 turns otherwise program exits
# user enters A, runs A function, user enters B, runs B function, user enters C, runs C function

turns = 0  # sets values for all variables
counter = 6
user_input = None

while turns < 5 and user_input is None:
    counter -= 1
    turns += 0
    print(f"You have {counter} turns to follow the instructions correctly!\n")
    user_input = input("Enter 'A' for the version of fizzbuzz with editable ranges and alternate words,"
                       "enter 'B' for the default game and enter 'C' to exit the program.\n")
    if user_input.upper() not in ('A', 'B', 'C'):
        user_input = None

    # if turns == 5:
    #     exit()

if user_input is None:
    exit()

if user_input.upper() == 'A':
    option_a()
elif user_input.upper() == 'B':
    option_b()
else:
    option_c()
