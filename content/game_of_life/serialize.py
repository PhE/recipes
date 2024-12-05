from utils import ndarray, array
from numpy import zeros


def save_board(M: ndarray, fname: str):
    """
    format de sauvegarde suivant :
    La première ligne du fichier contient la taille de la matrice sous le format suivant :
    l c
    c'est-à-dire, le nombre de ligne puis un espace puis le nombre de colonnes

    Chaque ligne suivante contient les coordonnées i (ligne) et j (colonne) d'une case
    valant 1 sous le format suivant :
    """
    l, k = M.shape

    with open(fname, 'wt') as f:
        f.write(f"{l} {k}\n")

        # pour chaque ligne de la matrice
        for i in range(l):
            # pour chaque colonne de la matrice
            for j in range(k):
                c = M[i, j]
                if c == 1:
                    f.write(f"{i} {j}\n")


def load_board(fname: str) -> ndarray:
    with open(fname) as f:
        shape = f.readline()
        l, k = [int(x) for x in shape.split()]
        M = zeros((l, k), dtype="bool")
        while line := f.readline():
            i, j = [int(x) for x in line.split()]
            M[i, j] = True

        return M