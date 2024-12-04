from numpy import array, zeros


def print_board(M: array):
    for ligne in M:
        for cellule in ligne:
            print(str(int(cellule), end=""))
        print()


def neighborhood(M: array, i: int, j: int) -> list:
    ...
