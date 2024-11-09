ordonne = [[1, 2, 3], [4,5,6], [7, 8, 9]]

test = [[1, 2, 3], [6, 5, 4], [9, 7, 8]]


def Tab_to_List(taquin):
    res = []
    for i in range(len(taquin)):
        for j in range(len(taquin[0])):
            res.append(taquin[i][j])
    return res


def List_to_Tab(liste):
    res = []
    for i in range(0, 3):
        ligne = []
        while len(ligne) != 3:
            ligne.append(liste[0])
            del (liste[0])
        res.append(ligne)
    return res


def score_tab(taquin, solution):
    somme = 0
    for i in range(len(taquin)):
        for j in range(len(taquin[0])):
            if taquin[i][j] == solution[i][j]:
                somme = somme + 10 ** (9 - taquin[i][j])
    return somme




def coup_tab(taquin, sommet):
    ntaquin = [[taquin[i][j] for j in range(len(taquin[i]))] for i in range(len(taquin))]
    for i in range(len(taquin)):
        for j in range(len(taquin[0])):
            if ntaquin[i][j] == sommet:
                l, k = i, j
            elif ntaquin[i][j] == 9:
                p, q = i, j
    a = ntaquin[p][q]
    ntaquin[p][q] = ntaquin[l][k]
    ntaquin[l][k] = a
    return ntaquin


def maximum_indice(liste):
    max = liste[0]
    indice = 0
    for i in range(len(liste)):
        if liste[i] > max:
            max = liste[i]
            indice = i
    return indice



def find_empty_position(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 9:
                return i, j


def get_possible_moves(board):
    moves = []
    empty_ligne, empty_col = find_empty_position(board)

    if empty_ligne > 0:
        moves.append(board[empty_ligne - 1][empty_col])

    if empty_ligne < 2:
        moves.append(board[empty_ligne + 1][empty_col])

    if empty_col > 0:
        moves.append(board[empty_ligne][empty_col - 1])

    if empty_col < 2:
        moves.append(board[empty_ligne][empty_col + 1])

    return moves


def branch_and_bound(taquin, solution):
    chemin = []
    while taquin != solution:

        atraiter = get_possible_moves(taquin)
        traiter = []
        for i in range(len(atraiter)):
            new_taquin = coup_tab(taquin, atraiter[i])
            traiter.append(score_tab(new_taquin, solution))

        best_indice = maximum_indice(traiter)

        chemin.append(atraiter[best_indice])

        new_taquin = coup_tab(taquin, atraiter[best_indice])

        taquin = new_taquin

    return chemin


from random import randint

def melange(taquin, N):
    while N != 0:
        coups_possibles = get_possible_moves(taquin)
        n = len(coups_possibles)
        a = randint(0, n - 1)
        sommet = coups_possibles[a]
        taquin = coup_tab(taquin, sommet)
        N = N - 1
    return taquin


