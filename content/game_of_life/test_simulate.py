from simulate import next_turn, simulate
from utils import print_board, array
from numpy.testing import assert_array_equal
from test_utils import M1, M4, M5


def test_1():
    m0 = array(
        [
            [1, 1, 0],
            [1, 0, 0],
            [0, 0, 0],
        ],
        dtype="bool",
    )
    m1 = next_turn(m0)
    m2 = next_turn(m1)
    m3 = next_turn(m2)

    assert print_board(m0) == "110\n100\n000\n"
    assert print_board(m1) == "110\n110\n000\n"
    assert print_board(m2) == "110\n110\n000\n"
    assert print_board(m3) == "110\n110\n000\n"


def test_simulate_M5():
    assert_array_equal(
        simulate(M5, 2),
        array(
            [
                [False, False, True, False, False],
                [False, True, False, True, False],
                [True, False, False, False, True],
                [False, True, False, True, False],
                [False, False, True, False, False],
            ],
            dtype=bool,
        ),
    )


def test_simulate_M4():
    assert_array_equal(
        simulate(M4, 2),
        array(
            [
                [False, False, False, False],
                [False, True, True, False],
                [False, True, True, False],
                [False, False, False, False],
            ],
            dtype=bool,
        ),
    )
