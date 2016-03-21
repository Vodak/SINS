"""
Classe Map permettant de créer une map aléatoire
"""

from Tile import *
from maths import *


class Map:

	# constructeur

	def __init__(self):
		
		# Carte de Case de 96*72
		
		self.map = [[Case] * 72 for i in range(96)] 

	# Création de la carte

	def generate(self):

		# Disposition des bordures en eau de la carte

		for i in range(95):
			self.map[0][i] = Bloc.Eau
			self.map[1][i] = Bloc.Eau
			self.map[70][i] = Bloc.Eau
			self.map[71][i] = Bloc.Eau

		for i in range(71):
			self.map[i][0] = Bloc.Eau
			self.map[i][1] = Bloc.Eau
			self.map[i][94] = Bloc.Eau
			self.map[i][95] = Bloc.Eau

		# Disposition du sable

		for i in range(2, 93):
			self.map[2][i] = Bloc.Sable
			self.map[3][i] = Bloc.Sable
			self.map[68][i] = Bloc.Sable
			self.map[69][i] = Bloc.Sable

		for i in range(2, 70):
			self.map[i][2] = Bloc.Sable
			self.map[i][3] = Bloc.Sable
			self.map[i][92] = Bloc.Sable
			self.map[i][93] = Bloc.Sable

		# Disposition de l'Hêrbe

		for i in range(4, 92):
			for j in range(4, 68):
				self.map[i][j] = Bloc.Herbe

		# Disposition du chemins

		for i in range(14, 82):
			self.map[36][i] = Bloc.Route

		for i in range(9, 63):
			self.map[i][48] = Bloc.Route

		for i in range(29, 65):
			self.map[i][14] = Bloc.Route
			self.map[i][61] = Bloc.Route

		for i in range(26, 48):
			self.map[19][i] = Bloc.Route
			self.map[67][i] = Bloc.Route

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
			self.map[i + xBloc][yBloc] = Bloc.Brique
			self.map[xBloc][yBloc + 6] = Bloc.Brique

		for i in range(yBloc, yBloc + 6):
			self.map[yBloc][i + yBloc] = Bloc.Brique
			self.map[xBloc + 9][yBloc] = Bloc.Brique

		# Disposition du plancher

		for i in range(xBloc + 1, xBloc + 8):
			for j in range(yBloc + 1, yBloc + 5):
				self.map[i][j] = Bloc.Plancher

		self.map[5][6] = Bloc.Plancher
	
	# fonction renvoyant la distance minimale entre 2 blocs, en considérant les cases où il est impossible de se déplacer
	
	def getDistance(xDepart, yDepart, xObjectif, yObjectif):
		carte = [[0] * 72 for i in range(96)]
		carte2 = [[-1] * 72 for i in range(96)]
		pile = [(xDepart, yDepart)]
		
		for i in range(72):
			for j in range(96):
				carte[i][j] = abs(xObjectif - i) + abs(yObjectif - j)
		
		carte2[xDepart][yDepart] = 0
		
		while carte2[xObjectif][yObjectif] == -1:
			# à faire plus tard car trop complexe
