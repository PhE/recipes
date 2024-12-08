from simulate import next_turn, simulate
from utils import print_board, array
from numpy.testing import assert_array_equal
from test_utils import M1, M4, M5


def test_0():
    assert_array_equal(M1, M1)

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

    assert_array_equal(
        m1,
        array(
            [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 0],
            ],
            dtype=bool,
        ),
    )

    assert_array_equal(
        m2,
        array(
            [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 0],
            ],
            dtype=bool,
        ),
    )

    assert_array_equal(
        m3,
        array(
            [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 0],
            ],
            dtype=bool,
        ),
    )


def test_simulate_M5():
    assert_array_equal(
        simulate(M5, 2),
        array(
            [
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [1, 0, 0, 0, 1],
                [0, 1, 0, 1, 0],
                [0, 0, 1, 0, 0],
            ],
            dtype=bool,
        ),
    )


def test_simulate_M4():
    assert_array_equal(
        simulate(M4, 2),
        array(
            [
                [0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
            ],
            dtype=bool,
        ),
    )
