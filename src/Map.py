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
		
		self.map = [[0] * 72 for i in range(96)]
		
		self.ecole = False
		self.hopital = False
		self.psychiatre = False
		self.cuisinier = False

	# Création de la carte

	def generate(self):
		
		# Disposition des bordures en eau de la carte
		for i in range(96):
			for j in range(72):
				self.map[i][j] = Tile()
		
		for i in range(72):
			self.map[0][i].Bloc = Bloc.Eau
			self.map[1][i].Bloc = Bloc.Eau
			self.map[94][i].Bloc = Bloc.Eau
			self.map[95][i].Bloc = Bloc.Eau

		for i in range(96):
			self.map[i][0].Bloc = Bloc.Eau
			self.map[i][1].Bloc = Bloc.Eau
			self.map[i][70].Bloc = Bloc.Eau
			self.map[i][71].Bloc = Bloc.Eau

		# Disposition du sable

		for i in range(2, 70):
			self.map[2][i].Bloc = Bloc.Sable
			self.map[3][i].Bloc = Bloc.Sable
			self.map[92][i].Bloc = Bloc.Sable
			self.map[93][i].Bloc = Bloc.Sable

		for i in range(2, 93):
			self.map[i][2].Bloc = Bloc.Sable
			self.map[i][3].Bloc = Bloc.Sable
			self.map[i][68].Bloc = Bloc.Sable
			self.map[i][69].Bloc = Bloc.Sable

		# Disposition de l'Hêrbe

		for i in range(4, 92):
			for j in range(4, 68):
				self.map[i][j].Bloc = Bloc.Herbe
		
		# Disposition du chemins

		routes = open("../files/map/1", "r")
		
		for j in range(72):
			for i in range(96):
				self.map[i][j].Bloc = Bloc.Route if routes.read(1) == "1" else self.map[i][j].Bloc
	# Création des maisons
	
	def maison(self):
		
		(x, y) = (randint(0, 84), randint(0, 63))
		
		route = False
		positionPorte = (x, y)
		placable = False
		
		while not placable or not route:
			
			(x, y) = (randint(0, 84), randint(0, 63))
		
			route = False
			positionPorte = (x, y)
			placable = True
		
			for i in range(x - 1, x + 10):
				for j in  range(y - 1, y + 7):
					if self.map[i][j].Bloc != Bloc.Herbe:
						placable = False
			
			if placable:
				
				for i in range(x + 1, x + 7):
					if self.map[i][y - 2].Bloc == Bloc.Route:
						if not route:
							positionPorte = (i, y)
						route = True
						
					elif self.map[i][y + 7].Bloc == Bloc.Route:
						if not route:
							positionPorte = (i, y + 5)
						route = True
						
				for j in range(y + 1, y + 5):
					if self.map[x - 2][j].Bloc == Bloc.Route:
						if not route:
							positionPorte = (x, j)
						route = True
					
					elif self.map[x + 10][j].Bloc == Bloc.Route:
						if not route:
							positionPorte = (x + 8, j)
						route = True
			
			
		# Disposition des murs :
		for i in range(x, x + 9):
			self.map[i][y].Bloc = Bloc.Mur
			self.map[i][y + 5].Bloc = Bloc.Mur
		for j in range(y + 1, y + 6):
			self.map[x][j].Bloc = Bloc.Mur
			self.map[x + 8][j].Bloc = Bloc.Mur
		
		# Disposition du plancher :
		for k in range(x + 1, x + 8):
			for l in range(y + 1, y + 5):
				self.map[k][l].Bloc = Bloc.Plancher
		
		self.map[positionPorte[0]][positionPorte[1]].Bloc = Bloc.Plancher
		
		# Aménagement des maisons
		
		if not self.ecole :
			decale = 0
			
			if self.map[x + 5][y].Bloc == Bloc.Plancher:
				decale = -2
			elif self.map[x + 3][y + 5] == Bloc.Plancher or self.map[x + 5][y + 5] == Bloc.Plancher or self.map[x + 5][y + 5] == Bloc.Plancher:
				decale = -1
			
			self.map[x + 3 + decale][y + 4].Objet = Objet.ChaiseEcole
			self.map[x + 5 + decale][y + 4].Objet = Objet.ChaiseEcole
			self.map[x + 7 + decale][y + 4].Objet = Objet.ChaiseEcole
			
			self.map[x + 3 + decale][y + 3].Objet = Objet.TableEcole
			self.map[x + 5 + decale][y + 3].Objet = Objet.TableEcole
			self.map[x + 7 + decale][y + 3].Objet = Objet.TableEcole
			
			self.map[x + 5 + decale][y + 1].Objet = Objet.Tableau
			self.map[x + 5 + decale][y + 2].Objet = Objet.PlaceProf
			
			self.ecole = True
		
		elif not self.hopital :
			self.map[x + 4][y + 2].Objet = Objet.LitMedecin
			self.map[x + 3][y + 2].Objet = Objet.ChaiseMedecin
			
			self.map[x + 7][y + 2].Objet = Objet.LitMedecin
			self.map[x + 6][y + 2].Objet = Objet.ChaiseMedecin
			
			self.map[x + 4][y + 4].Objet = Objet.LitMedecin
			self.map[x + 3][y + 4].Objet = Objet.ChaiseMedecin
			
			self.map[x + 7][y + 4].Objet = Objet.LitMedecin
			self.map[x + 6][y + 4].Objet = Objet.ChaiseMedecin
			
			self.hopital = True
			
		elif not self.psychiatre :
			self.map[x + 4][y + 2].Objet = Objet.LitPsychiatre
			self.map[x + 3][y + 2].Objet = Objet.ChaisePsychiatre
			
			self.map[x + 7][y + 2].Objet = Objet.LitPsychiatre
			self.map[x + 6][y + 2].Objet = Objet.ChaisePsychiatre
			
			self.map[x + 4][y + 4].Objet = Objet.LitPsychiatre
			self.map[x + 3][y + 4].Objet = Objet.ChaisePsychiatre
			
			self.map[x + 7][y + 4].Objet = Objet.LitPsychiatre
			self.map[x + 6][y + 4].Objet = Objet.ChaisePsychiatre
			
			self.psychiatre = True
		
		elif not self.cuisinier :
			self.map[x + 3][y + 2].Objet = Objet.Chaise
			self.map[x + 3][y + 3].Objet = Objet.Table
			self.map[x + 3][y + 4].Objet = Objet.Chaise
			
			self.map[x + 6][y + 2].Objet = Objet.Chaise
			self.map[x + 6][y + 3].Objet = Objet.Table
			self.map[x + 6][y + 4].Objet = Objet.Chaise
			
			self.map[x + 8][y + 4].Objet = Objet.EntreeFour
			self.map[x + 8][y + 3].Objet = Objet.Four
			
			self.cuisinier = True
		
		else:
			self.map[x + 2][y + 2].Objet = Objet.Lit
			self.map[x + 4][y + 2].Objet = Objet.Lit
			self.map[x + 5][y + 4].Objet = Objet.Chaise
			self.map[x + 6][y + 4].Objet = Objet.Table
			self.map[x + 7][y + 4].Objet = Objet.Chaise
			self.map[x + ][y + ].Objet = Objet.Four