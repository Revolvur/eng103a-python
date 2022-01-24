# age = 17
# film_showing = False

# if age >= 18 and film_showing is True:
#     print("You are allowed to buy a ticket for this film.")
#     print("Enjoy the film")  # indentation matters
#
# print("This will always print")


# if age >= 18 and film_showing:
#     print("You are allowed to buy a ticket for this film.")
#     print("Enjoy the film")  # indentation matters
#
# elif age < 18:
#     print("You are not old enough")  # once it hits elif, it will not hit any of the others
# elif not film_showing:
#     print("The film is not showing")
#
# print("This will always print")

# age = 17
# film_showing = False
#
# if age >= 18 and film_showing:
#     print("You are allowed to buy a ticket for this film.")
#     print("Enjoy the film")  # indentation matters
#
# elif age == 17:
#     print("Come back next year")
#
# else:
#     print("No dice")
#
# print("This will always print")

certificate = '12' # U, PG, 12, 12A, 15, 18
# Check the certificate
# Print corresponding info about film

if certificate.upper() == 'U':
    print('Suitable for all ages')

elif certificate.upper() == 'PG':
    print('Parental Guidance required')
# elif certificate.upper() == '12' or certificate.upper() == '12A':
#     print("Ages 12 or above, 12A requires an adult at all times")
elif certificate.upper() in ('12', '12A'):
    print("Ages 12 or above, 12A requires an adult at all times")

elif certificate == '15':
    print("Age required is 15 years or older")
elif certificate == '18':
    print("Viewer must be 18 years or older")
else:
    print('Certificate not recognised')

# elif certificate == 12 or 12A won't work as it will always resolve to true
