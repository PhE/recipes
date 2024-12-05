from utils import array
from serialize import save_board, load_board
from numpy.testing import assert_array_equal
from test_utils import M1, M5


def test_save_board():
    """sauvegarde matrice"""
    save_board(M1, "myboard1.brd")
    save_board(M5, "myboard2.brd")

    assert open("myboard1.brd").read() == open("M1.brd").read()
    assert open("myboard2.brd").read() == open("M5.brd").read()


def test_load_board_M1():
    save_board(M1, "temp.brd")
    M1b = load_board("temp.brd")

    assert_array_equal(M1, M1b)


def test_load_board_M5():
    save_board(M5, "temp.brd")
    M5b = load_board("temp.brd")

    assert_array_equal(M5, M5b)
