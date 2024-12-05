from utils import neighborhood, array


M1 = array(
    [
        [1, 1, 1],
        [0, 0, 0],
        [0, 0, 1],
    ],
    dtype="bool",
)

M4 = array(
    [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ],
    dtype="bool",
)

M5 = array(
    [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ],
    dtype="bool",
)


def test_bidon():
    assert True
    assert 2 == 1 + 1


def test_vide():
    """
    matrice vide
    """
    M = array([[]], dtype="bool")
    assert neighborhood(M, 0, 0) == []

    M = array([], dtype="bool")
    assert neighborhood(M, 0, 0) == []


def test_2():
    """
    exemples p9
    """
    M = array([[1, 0, 1], [0, 0, 0], [1, 0, 1]], dtype="bool")

    # comme indiqué l'odre n'est pas important
    assert neighborhood(M, 0, 0) == [False, False, False]
    assert neighborhood(M, 1, 2) == [False, True, False, False, True]
    assert neighborhood(M, 1, 1) == [True, False, True, False, False, True, False, True]


def test_2b():
    assert True
