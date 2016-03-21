"""
Fichier provisoire
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

for i in range(x , x + 9):
	for j in  range(y, y + 6):
		if map[i][j] != Bloc.Herbe:
			placable = False
if placable:
	for i in range(x + 1, x + 8):
		if map[i][y - 1] == Bloc.Route:
			if not route:
				positionPorte = (i, y - 1)
			route = True
			
		elif map[i][y + 7] == Bloc.Route:
			if not route:
				positionPorte = (i, y + 7)
			route = True
			
	for j in range(y + 1, y + 5):
		if map[x - 1][j] == Bloc.Route:
			if not route:
				positionPorte = (x - 1, j)
			route = True
		
		if map[x + 10][j] == Bloc.Route:
			if not route:
				positionPorte = (x + 10, j)
			route = True

if route and placable:
	#brauique, plancher, porte
