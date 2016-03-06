"""
Classe Map permettant de créer une map aléatoire
"""

from Tile import *


class Map:

	# constructeur

	def __init__(self):
		
		# Carte de Case de 96*72
		
		carte = [[Case] * 72 for i in range(96)] 

	# Création de la carte

	def generate(self):

		# Disposition des bordures en eau de la carte

		for i in range(95):
			map[0][i] = Bloc.Eau
			map[1][i] = Bloc.Eau
			map[70][i] = Bloc.Eau
			map[71][i] = Bloc.Eau

		for i in range(71):
			map[i][0] = Bloc.Eau
			map[i][1] = Bloc.Eau
			map[i][94] = Bloc.Eau
			map[i][95] = Bloc.Eau

		# Disposition du sable

		for i in range(2, 93):
			map[2][i] = Bloc.Sable
			map[3][i] = Bloc.Sable
			map[68][i] = Bloc.Sable
			map[69][i] = Bloc.Sable

		for i in range(2, 70):
			map[i][2] = Bloc.Sable
			map[i][3] = Bloc.Sable
			map[i][92] = Bloc.Sable
			map[i][93] = Bloc.Sable

		# Disposition de l'Hêrbe

		for i in range(4, 92):
			for j in range(4, 68):
				map[i][j] = Bloc.Herbe

		# Disposition du chemins

		for i in range(14, 82):
			map[36][i] = Bloc.Route

		for i in range(9, 63):
			map[i][48] = Bloc.Route

		for i in range(29, 65):
			map[i][14] = Bloc.Route
			map[i][61] = Bloc.Route

		for i in range(26, 48):
			map[19][i] = Bloc.Route
			map[67][i] = Bloc.Route

		# Disposition des maisons

		maison(23, 28)
		maison(10, 27)
		maison(27, 7)
		maison(37, 7)
		maison(56, 7)
		maison(10, 13)
		maison(77, 13)
		maison(61, 28)
		maison(78, 26)
		maison(10, 39)
		maison(23, 37)
		maison(61, 37)
		maison(78, 37)
		maison(25, 54)
		maison(37, 54)
		maison(51, 54)
		maison(63, 54)
		maison(81, 51)
		maison(6, 60)

		# Création des maisons

	def maison(self, xBloc, yBloc):

		# Disposition des murs

		for i in range(xBloc, xBloc + 9):
			map[i + xBloc][yBloc] = Bloc.Brique
			map[xBloc][yBloc + 6] = Bloc.Brique

		for i in range(yBloc, yBloc + 6):
			map[yBloc][i + yBloc] = Bloc.Brique
			map[xBloc + 9][yBloc] = Bloc.Brique

		# Disposition du plancher

		for i in range(xBloc + 1, xBloc + 8):
			for j in range(yBloc + 1, yBloc + 5):
				map[i][j] = Bloc.Plancher

		map[5][6] = Bloc.Plancher
