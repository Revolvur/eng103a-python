# Basic Version

# For numbers 1 to 100
# Play fizzbuzz
# Print the number
# If divisible by 3, fizz
# If by 5, buzz
# If both, fizzbuzz

turns = 0  # sets values for all variables
counter = 6
range_start = None
range_end = None
user_input = None
fizz_alt = 'fizz'  # fizz and buzz set unless prompted by user otherwise
buzz_alt = 'buzz'

while turns < 5:

    if user_input is None:  # if nothing in user_input
        counter -= 1  # for visual countdown timer
        turns += 1  # for while loop to exit
        print(
            "You have " + str(counter) + " turns to follow the instructions correctly! \n")  # line 24+25 visual counter
        print("Turns remaining: " + str(counter) + "\n")
        user_input = input("Enter 'A' if you want to fill in the number ranges "  # gives user choices
                           "and choose your own 'fizzbuzz words"
                           ", enter 'B' if you want the default settings,"
                           "or enter 'C' if you want to exit the program.\n")
        print("You have chosen '" + str(user_input.upper()) + "'.\n")
        if user_input not in ('A', 'a', 'B', 'b', 'C', 'c'):  # if input is not what's asked, user_input reset
            user_input = None  # resets user_input to None

    else:
        break  # exits while loops after user_input != None

if turns > 5:  # exits program after 5 attempts
    exit()

print("You're giving me the correct input.")

if user_input.upper() == 'C':  # exits program
    exit()
elif user_input.upper() == 'B':  # runs as default settings
    range_start = '1'
    range_end = '100'
elif user_input.upper() == 'A':  # runs option A
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
# end


# # What can you add
# # Can we customise the end number?
# # Or the start number?
# # Can we get those from player input?
# # Can we input alternate words for fizz and buzz?
#
# # Try to stick to PEP8
# Comment your code
