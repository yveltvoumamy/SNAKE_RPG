
from src.scene.RPG_SCENE import Rpg
from src.scene.MENU import *
from src.scene.RATING_BOARD import *

RPG = Rpg()


def start_menu():
    menu = Menu()
    menu.append_option('Start the game', lambda: RPG.start())
    menu.append_option('Rating board', lambda: open_rating_board())
    menu.append_option('Clean rating board', lambda: clean_rating_board())
    shop_alive(menu)


if __name__ == "__main__":
    start_menu()
