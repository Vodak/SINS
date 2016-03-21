"""
Fichier provisoir
"""
from Map import *

carte = Map()
carte.generate()

x = 0
y = 0
maison = map[x][y]

for i in range(96):
	for j in range(72):
	
	if map[i+2][j] == bloc.Route or map[i][j+2] == bloc.Route or map[i-2][j] == bloc.Route or map[i][j-2] == bloc.Route or map[i+2][j+1] == bloc.Route or map[i+2][j-1] == bloc.Route or map[i-2][j+1] == bloc.Route or map[i-2][j-1] == bloc.Route or map[i+1][j+2] == bloc.Route or map[i-1][j+2] == bloc.Route or map[i+1][j-2] == bloc.Route or map[i-1][j-2] == bloc.Route:
		if map[i+1][j] == bloc.Herbe and map[i+1][j+1] == bloc.Herbe and map[i+1][j-1] == bloc.Herbe and map[i][j+1] == bloc.Herbe and map[i][j-1] == bloc.Herbe and map[i-1][j] == bloc.Herbe and map[i-1][j+1] == bloc.Herbe and map[i-1][j-1] == bloc.Herbe:
			
