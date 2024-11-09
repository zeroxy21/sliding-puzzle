ordonne=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]





def Tab_to_List(taquin):
    res = []
    for i in range(len(taquin)):
        for j in range(len(taquin[0])):
            res.append(taquin[i][j])
    return res


def List_to_Tab(liste):
    res = []
    for i in range(0, 4):
        ligne = []
        while len(ligne) != 4:
            ligne.append(liste[0])
            del (liste[0])
        res.append(ligne)
    return res

def score_tab_1(taquin,solution):
    somme = 0
    for i in range(len(taquin)):
        for j in range(len(taquin[0])):
            if taquin[0][j] == solution[0][j]:
                somme = somme + 10 ** 16
            elif taquin[1][j] == solution[1][j]:
                somme = somme + 10 **16
            elif taquin[i][j]==solution[i][j]:
                somme=somme+10**(16-taquin[i][j])
    return somme
def score_tab_2(taquin,solution):
    somme = 0
    for i in range(len(taquin)):
        for j in range(len(taquin[0])):
            if taquin[0][j] == solution[0][j]:
                somme = somme + 10 ** 16
            elif taquin[2][0]==9:
                somme=somme+10**16
            elif taquin[2][1]==10:
                somme=somme+10**16
            elif taquin[3][0]==13:
                somme=somme+10**16
            elif taquin[3][1]==14:
                somme=somme+10**16
            elif taquin[i][j]==solution[i][j]:
                somme=somme+10**(16-taquin[i][j])
    return somme
def score_tab_3(taquin, solution):
    somme = 0
    for i in range(len(taquin)):
        for j in range(len(taquin[0])):
            if taquin[i][j] == solution[i][j]:
                somme = somme + 10 ** (16 - taquin[i][j])
    return somme





def coup_tab(taquin, sommet):
    ntaquin = [[taquin[i][j] for j in range(len(taquin[i]))] for i in range(len(taquin))]
    for i in range(len(taquin)):
        for j in range(len(taquin[0])):
            if ntaquin[i][j] == sommet:
                l, k = i, j
            elif ntaquin[i][j] == 16:
                p, q = i, j
    a = ntaquin[p][q]
    ntaquin[p][q] = ntaquin[l][k]
    ntaquin[l][k] = a
    return ntaquin

from random import randint
def maximum_indice(liste):
    indice = randint(0,len(liste)-1)
    max = liste[indice]

    for i in range(len(liste)):
        if liste[i] > max:
            max = liste[i]
            indice = i
    return indice



def find_empty_position(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 16:
                return i, j


def get_possible_moves(board):
    moves = []
    empty_ligne, empty_col = find_empty_position(board)

    if empty_ligne > 0:
        moves.append(board[empty_ligne - 1][empty_col])

    if empty_ligne < 3:
        moves.append(board[empty_ligne + 1][empty_col])

    if empty_col > 0:
        moves.append(board[empty_ligne][empty_col - 1])

    if empty_col < 3:
        moves.append(board[empty_ligne][empty_col + 1])

    return moves


def branch_and_bound_2(taquin):
    chemin = []
    solution = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    while (taquin[0],taquin[1])!=([1,2,3,4],[5,6,7,8]):
        atraiter = get_possible_moves(taquin)
        traiter = []
        for i in range(len(atraiter)):
            new_taquin = coup_tab(taquin, atraiter[i])
            traiter.append(score_tab_1(new_taquin,solution))
        best_indice = maximum_indice(traiter)
        chemin.append(atraiter[best_indice])
        new_taquin = coup_tab(taquin, atraiter[best_indice])
        taquin = new_taquin
    while (taquin[2][0],taquin[2][1],taquin[3][0],taquin[3][1])!=(9,10,13,14):
        coups= get_possible_moves(taquin)
        atraiter=[]
        for elem in coups :
            if elem not in taquin[0] and elem not in taquin[1]:
                atraiter.append(elem)
        traiter = []
        for i in range(len(atraiter)):
            new_taquin = coup_tab(taquin, atraiter[i])
            traiter.append(score_tab_2(new_taquin,solution))
        best_indice = maximum_indice(traiter)
        chemin.append(atraiter[best_indice])
        new_taquin = coup_tab(taquin, atraiter[best_indice])
        taquin = new_taquin
    while taquin!=solution:
        coups= get_possible_moves(taquin)
        atraiter=[]
        for elem in coups :
            if elem not in taquin[0] and elem not in taquin[1] and elem not in [9,10,13,14]:
                atraiter.append(elem)
        traiter = []
        for i in range(len(atraiter)):
            new_taquin = coup_tab(taquin, atraiter[i])
            traiter.append(score_tab_2(new_taquin,solution))
        best_indice = maximum_indice(traiter)
        chemin.append(atraiter[best_indice])
        new_taquin = coup_tab(taquin, atraiter[best_indice])
        taquin = new_taquin
    return chemin,taquin



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
