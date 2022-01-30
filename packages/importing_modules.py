# # import random
# #
# # print(random.random())  # random number between 0 and 1
#
# from random import random, randint  # from package random import function random, so dont need package name every time
# from math import ceil, floor, pi
# import os
#
# print(random())
#
# print(pi)
# print(ceil(pi))  # rounds up
# print(floor(pi))  # rounds down
#
# print(randint(1, 100))
#
# work_dir = os.getcwd()
# print(work_dir)
# print(os.getpid())
# print(os.name())

# import packages.my_functions.os_functions as f
# from my_classes.game_class import Game
#
# print(f.work_dir)
# new_vegas = Game("Fallout New Vegas", "PC", 100)
# print(new_vegas.name)
#
# print(f.return_new_vegas())

# PIP -> PIP Installs Packages (Auto-acronym)

import requests, emoji

r = requests.get("https://www.bbc.co.uk")
print(r, type(r))

print(r.status_code)
print(r.content)

print(emoji.emojize('Python is: thumbs_up:'))
