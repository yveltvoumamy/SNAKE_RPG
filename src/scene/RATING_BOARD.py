from src.scene.SHOP_SCENE import shop_alive
from src.scene.MENU import *


def open_rating_board():
    global sc
    f = open('data/rating_board.txt')
    data = []
    for x in f:
        data.append(str(x))
    board = Menu()
    for i in range(len(data)):
        text = data[i][:-1]
        board.append_option(text, lambda: ...)
    shop_alive(board)


def clean_rating_board():
    f = open('data/rating_board.txt', 'w')
    f.close()
