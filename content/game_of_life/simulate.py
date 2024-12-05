from utils import neighborhood, print_board, ndarray


def next_turn(M: ndarray) -> ndarray:
    l, k = M.shape

    M2 = M.copy()
    M2.fill(0)

    # pour chaque ligne de la matrice
    for i in range(l):
        # pour chaque colonne de la matrice
        for j in range(k):
            c = M[i, j]
            vc = neighborhood(M, i, j)
            # vc1 = len(c for c in vc if c == 1)
            vc1 = sum(vc)
            # règle 1. Si c = 1 et qu'il y a exactement deux ou trois cases égales à 1 dans V (c)
            # alors c = 1 au tour suivant; Sinon c = 0
            if c == 1:
                if vc1 == 2 or vc1 == 3:
                    c2 = 1
                else:
                    c2 = 0
            # règle 2. Si c = 0 et qu'il y a exactement trois cases à 1 dans V (c)
            # alors c = 1 au tour suivant,
            # sinon c = 0
            else:
                if vc1 == 3:
                    c2 = 1
                else:
                    c2 = 0

            # on place la cellule dans la nouvelle matrice
            M2[i, j] = c2

    return M2


def simulate(M0: ndarray, max_turns: int) -> ndarray:
    print("Initial board:")
    print_board(M0)
    M = M0.copy()
    for n in range(max_turns):
        M = next_turn(M)
        print(f"Turn {n}/{max_turns}:")
        print_board(M)

    return M
