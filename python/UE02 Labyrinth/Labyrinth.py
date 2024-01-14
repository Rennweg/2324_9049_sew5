import argparse
from copy import copy

paths = []
def suchen(zeile, spalte, lab, visited, path = []):
    count = 0
    if visited[zeile][spalte] or lab[zeile][spalte] == '#':
        return 0
    if lab[zeile][spalte] == 'A':
        paths.append(copy(path))
        return 1
    path.append((zeile, spalte))
    visited[zeile][spalte] = True
    count = (suchen(zeile + 1, spalte, lab, visited, path) + suchen(zeile - 1, spalte, lab, visited, path)
             + suchen(zeile, spalte + 1, lab, visited, path) + suchen(zeile, spalte - 1, lab, visited, path))
    visited[zeile][spalte] = False
    path = path[:-1]
    return count



def printLab(lab):
    for i in lab:
        for j in i:
            print(j, end='')
        print()



parser = argparse.ArgumentParser(description='calculate number of ways through a labyrinth', add_help=True)

# cords
parser.add_argument('--xstart', '-x', default=1, type=int, help='x-coordinate to start')
parser.add_argument('--ystart', '-y', default=1, type=int, help='y-coordinate to start')

# print
parser.add_argument('--print', '-p', action="store_true", help='print output of every solution')
parser.add_argument('--time', '-t', action="store_true", help='print total calculation time (in milliseconds)')
parser.add_argument('--delay', '-d', default=None, type=int, help='delay after printing a solution (in milliseconds)')

# input-file VERPFLICHTEND
parser.add_argument('input_file', help='Pfad zur Eingabedatei')

# Parsing der Befehlszeilenargumente
args = parser.parse_args()

# Zugriff auf die Argumente
input_file = args.input_file
x = args.xstart
y = args.ystart
p = args.print
t = args.time
d = args.delay


lab = open(input_file).read().strip().split('\n')

# 2D bool list als visited
vis = [[False for _ in range(len(lab))] for _ in range(len(lab[0]))]






