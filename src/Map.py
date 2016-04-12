"""
Classe Map permettant de créer une map aléatoire
"""

from Tile import *
from math import *
from random import *


class Map:

	# constructeur

	def __init__(self):
		
		# Carte de Case de 96*72
		
		self.map = [[Tile] * 72 for i in range(96)] 

	# Création de la carte

	def generate(self):

		# Disposition des bordures en eau de la carte

		for i in range(71):
			self.map[0][i] = Bloc.Eau
			self.map[1][i] = Bloc.Eau
			self.map[94][i] = Bloc.Eau
			self.map[95][i] = Bloc.Eau

		for i in range(95):
			self.map[i][0] = Bloc.Eau
			self.map[i][1] = Bloc.Eau
			self.map[i][70] = Bloc.Eau
			self.map[i][71] = Bloc.Eau

		# Disposition du sable

		for i in range(2, 70):
			self.map[2][i] = Bloc.Sable
			self.map[3][i] = Bloc.Sable
			self.map[92][i] = Bloc.Sable
			self.map[93][i] = Bloc.Sable

		for i in range(2, 93):
			self.map[i][2] = Bloc.Sable
			self.map[i][3] = Bloc.Sable
			self.map[i][68] = Bloc.Sable
			self.map[i][69] = Bloc.Sable

		# Disposition de l'Hêrbe

		for i in range(4, 92):
			for j in range(4, 68):
				self.map[i][j] = Bloc.Herbe

		# Disposition du chemins

		for i in range(9, 63):
			self.map[36][i] = Bloc.Route

		for i in range(14, 82):
			self.map[i][48] = Bloc.Route

		for i in range(29, 65):
			self.map[i][14] = Bloc.Route
			self.map[i][61] = Bloc.Route

		for i in range(26, 48):
			self.map[19][i] = Bloc.Route
			self.map[67][i] = Bloc.Route


	# Création des maisons

	def maison(self):
		(x, y) = (randint(0, 84), randint(0, 63))
		
		pointA = (x, y)
		pointB = (x + 9, y + 6)
		
		route = False
		positionPorte = (x, y)
		placable = True
		
		ecole = False
		hopital = False
		psychiatre = False
		
		for i in range(x , x + 9):
			for j in  range(y, y + 7):
				if self.map[i][j] != Bloc.Herbe:
					placable = False
		if placable:
			for i in range(x + 1, x + 8):
				if self.map[i][y - 1] == Bloc.Route:
					if not route:
						positionPorte = (i, y - 1)
					route = True
					
				elif self.map[i][y + 7] == Bloc.Route:
					if not route:
						positionPorte = (i, y + 7)
					route = True
					
			for j in range(y + 1, y + 6):
				if self.map[x - 1][j] == Bloc.Route:
					if not route:
						positionPorte = (x - 1, j)
					route = True
				
				if self.map[x + 10][j] == Bloc.Route:
					if not route:
						positionPorte = (x + 10, j)
					route = True
		
		if route and placable:
			# Disposition des murs :
			for i in range(x + 1, x + 8):
				self.map[i][y] = Bloc.Mur
				self.map[i][y + 5] = Bloc.Mur
			for j in range(y + 1, y + 6):
				self.map[x][j] = Bloc.Mur
				self.map[x + 8][j] = Bloc.Mur
			
			# Disposition du plancher :
			for k in range(x + 2, x + 7):
				for l in range(y + 2, y + 5):
					self.map[k][l] = Bloc.Plancher
					
			# Aménagement des maisons
			if not ecole :
				self.map[x + 4][y + 2] = Objet.ChaiseEcole
				self.map[x + 4][y + 4] = Objet.ChaiseEcole
				
				self.map[x + 5][y + 2] = Objet.TableEcole
				self.map[x + 5][y + 4] = Objet.TableEcole
				
				self.map[x + 8][y + 3] = Objet.Tableau
				self.map[x + 7][y + 3] = Objet.PlaceProf
				
				ecole = True
			
			if not hopital :
				self.map[x + 4][y + 2] = Objet.LitMedecin
				self.map[x + 3][y + 2] = Objet.ChaiseMedecin
				
				self.map[x + 7][y + 2] = Objet.LitMedecin
				self.map[x + 6][y + 2] = Objet.ChaiseMedecin
				
				self.map[x + 4][y + 4] = Objet.LitMedecin
				self.map[x + 3][y + 4] = Objet.ChaiseMedecin
				
				self.map[x + 7][y + 4] = Objet.LitMedecin
				self.map[x + 6][y + 4] = Objet.ChaiseMedecin
				
				hopital = True
				
			if not psychiatre :
				self.map[x + 4][y + 2] = Objet.LitPsychiatre
				self.map[x + 3][y + 2] = Objet.ChaisePsychiatre
				
				self.map[x + 7][y + 2] = Objet.LitPsychiatre
				self.map[x + 6][y + 2] = Objet.ChaisePsychiatre
				
				self.map[x + 4][y + 4] = Objet.LitPsychiatre
				self.map[x + 3][y + 4] = Objet.ChaisePsychiatre
				
				self.map[x + 7][y + 4] = Objet.LitPsychiatre
				self.map[x + 6][y + 4] = Objet.ChaisePsychiatre
				
				psychiatre = True