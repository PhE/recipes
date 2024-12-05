from numpy import array, ndarray


def print_board(M: ndarray):
    msg = ""
    for ligne in M:
        for cellule in ligne:
            msg = msg + str(int(cellule))
        msg = msg + "\n"
    print(msg, end="")
    return msg


def neighborhood(M: ndarray, i: int, j: int) -> list:
    if M.ndim != 2:
        return []

    l, k = M.shape
    if l < 1 or k < 1:
        return []

    # Si c est une case intérieure aux coordonnées i, j,
    # c'est-à-dire avec 0 < i < (l - 1) et 0 < j < (k - 1)
    # alors V (c) est maximal et contient les 8 cases suivantes :
    # V(c) = {mi-1,j-1 ; mi-1,j ; mi-1,j+1 ; mi,j-1 ; mi,j+1 ; mi+1,j-1 ; mi+1,j ; mi+1,j+1 }
    if 0 < i < (l - 1) and 0 < j < (k - 1):
        return [
            M[i - 1, j - 1],
            M[i - 1, j],
            M[i - 1, j + 1],
            M[i, j - 1],
            M[i, j + 1],
            M[i + 1, j - 1],
            M[i + 1, j],
            M[i + 1, j + 1],
        ]

    # Si c est une case sur la bordure de M ,
    # alors V (c) contient 5 cases.
    # Par exemple, si c = ml-1,p avec 0 < p < (k - 1) alors :
    # V (c) = {ml-1,p-1 ; ml-1,p+1 ; ml-2,p-1 ; ml-2,p ; ml-2,p+1 }
    # bordure première colonne (sauf les coins)
    if i == 0 and 0 < j < (k - 1):
        return [
            # M[i - 1, j - 1],
            # M[i - 1, j],
            # M[i - 1, j + 1],
            M[i, j - 1],
            M[i, j + 1],
            M[i + 1, j - 1],
            M[i + 1, j],
            M[i + 1, j + 1],
        ]
    # bordure dernière colonne (sauf les coins)
    if i == l - 1 and 0 < j < (k - 1):
        return [
            M[i - 1, j - 1],
            M[i - 1, j],
            M[i - 1, j + 1],
            M[i, j - 1],
            M[i, j + 1],
            # M[i + 1, j - 1],
            # M[i + 1, j],
            # M[i + 1, j + 1],
        ]
    # bordure première colonne (sauf les coins)
    if i == 0 and 0 < j < (k - 1):
        return [
            # M[i - 1, j - 1],
            # M[i - 1, j],
            # M[i - 1, j + 1],
            M[i, j - 1],
            M[i, j + 1],
            M[i + 1, j - 1],
            M[i + 1, j],
            M[i + 1, j + 1],
        ]
    # bordure première ligne (sauf les coins)
    if j == 0 and 0 < i < (l - 1):
        return [
            # M[i - 1, j - 1],
            M[i - 1, j],
            M[i - 1, j + 1],
            # M[i, j - 1],
            M[i, j + 1],
            # M[i + 1, j - 1],
            M[i + 1, j],
            M[i + 1, j + 1],
        ]
    # bordure dernière ligne (sauf les coins)
    if j == k - 1 and 0 < i < (l - 1):
        return [
            M[i - 1, j - 1],
            M[i - 1, j],
            # M[i - 1, j + 1],
            M[i, j - 1],
            # M[i, j + 1],
            M[i + 1, j - 1],
            M[i + 1, j],
            # M[i + 1, j + 1],
        ]

    # Si c est un coin de M , alors V (c) contient 3 cases.
    # Par exemple, si c = m0,0 alors :
    # V (c) = {m0,1 ; m1,0 ; m1,1 }
    # coin supérieur gauche
    if (i, j) == (0, 0):
        return [
            # M[i - 1, j - 1],
            # M[i - 1, j],
            # M[i - 1, j + 1],
            # M[i, j - 1],
            M[i, j + 1],
            # M[i + 1, j - 1],
            M[i + 1, j],
            M[i + 1, j + 1],
        ]

    return []