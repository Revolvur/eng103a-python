import os
# from ..my_classes.game_class import Game  # back to parent directory to access package
from packages.my_classes.game_class import Game

work_dir = os.getcwd()


def return_user_id():
    return os.getuid()


def return_os_info():
    return os.uname()


def return_new_vegas():
    return Game("Fallout New Vegas", "PC", 100)
