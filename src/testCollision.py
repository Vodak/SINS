"""
Fichier provisoir
"""
from Map import *

carte = Map()
carte.generate()

(x, y) = (5, 5)

pointA = (x, y)
pointB = (x + 9, y + 6)

route = False
positionPorte = (x, y)
placable = True

for i in range(x, x + 9):
	if map[i][y - 2] == Bloc.Route:
		route = True
		positionPorte = map[i][y - 2]
	elifmap[i][y + 8] == Bloc.Route:
		route = True
		positionPorte = map[i][y + 8]

for j in range(y, y + 6):
	if map[x -2][j] == Bloc.Route or map[x + 11][j] == Bloc.Route:
		route = True

for i in range(x , x + 9):
	for j in  range(y, y + 6):
		if map[i][j] != Bloc.Herbe:
			placable = False

if route and placable:
	#braique, plancher, porte
