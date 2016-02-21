from Tile import *


class Map:

	#
	# constructeur
	#

	def __init__(self):
		
		# Carte de Case de 96*72
		
		carte = [[Case] * 72 for i in range(96)] 

	#
	# Créatage de la carte
	#

	def generate(self):

		# Disposition des bordures en eau de la carte

		for i in range(95):
			carte[0][i] = Bloc.Eau
			carte[1][i] = Bloc.Eau
			carte[70][i] = Bloc.Eau
			carte[71][i] = Bloc.Eau

		for i in range(71):
			carte[i][0] = Bloc.Eau
			carte[i][1] = Bloc.Eau
			carte[i][94] = Bloc.Eau
			carte[i][95] = Bloc.Eau

		# Disposition du Saaaaable

		for i in range(2, 93):
			carte[2][i] = Bloc.Sable
			carte[3][i] = Bloc.Sable
			carte[68][i] = Bloc.Sable
			carte[69][i] = Bloc.Sable

		for i in range(2, 70):
			carte[i][2] = Bloc.Sable
			carte[i][3] = Bloc.Sable
			carte[i][92] = Bloc.Sable
			carte[i][93] = Bloc.Sable

		# Disposition de l'Hêêêêêrbeuuuh

		for i in range(4, 92):
			for j in range(4, 68):
				carte[i][j] = Bloc.Herbe

		# Disposition de la roux-teux

		for i in range(14, 82):
			carte[36][i] = Bloc.AutorouteA76DirectionDijon

		for i in range(9, 63):
			carte[i][48] = Bloc.AutorouteA76DirectionDijon

		for i in range(29, 65):
			carte[i][14] = Bloc.AutorouteA76DirectionDijon
			carte[i][61] = Bloc.AutorouteA76DirectionDijon

		for i in range(26, 48):
			carte[19][i] = Bloc.AutorouteA76DirectionDijon
			carte[76][i] = Bloc.AutorouteA76DirectionDijon

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

		#
		# Créatage des maisons
		#

	def maison(self, xBloc, yBloc):

		# Disposition des murs

		for i in range(xBloc, xBloc + 9):
			carte[i + xBloc][yBloc] = Bloc.MurBrique
			carte[xBloc][yBloc + 6] = Bloc.MurBrique

		for i in range(yBloc, yBloc + 6):
			carte[yBloc][i + yBloc] = Bloc.MurBrique
			carte[xBloc + 9][yBloc] = Bloc.MurBrique

		# Disposition du plancher

		for i in range(xBloc + 1, xBloc + 8):
			for j in range(yBloc + 1, yBloc + 5):
				carte[i][j] = Bloc.Plancher

		carte[5][6] = Bloc.Plancher
