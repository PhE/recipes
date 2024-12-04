from utils import neighborhood, array


def test_1():
    assert True


def test_2():
    """
    exeemples p9
    """
    M = array([[1, 0, 1], [0, 0, 0], [1, 0, 1]], dtype="bool")
    assert neighborhood(M, 0, 0) == [False, False, False]