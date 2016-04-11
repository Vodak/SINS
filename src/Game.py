"""
Classe Game qui gère le jeu
"""

from Map import *

class Game:
	 
	# Constructeur:
	
	def __init__(self):
		
		self.Map = Map()
		
	# Mise en place du jeu :
		
	def play(self):
		
		# Génération de la map :
		
		self.Map.generate()
		
		# Disposition des maisons :
		
		self.Map.maison()
		
		# Invocation des IA sur la map
		
		x = 0
		y = 0
		
		while self.Map.map[x][y] != Bloc.Herbe and self.Map.map[x][y] != Bloc.Plancher and self.Map.map[x][y] != Bloc.Sable:

			x = randint(0, 95)
			y = randint(0, 71)
			
			self.Map.map[x][y].IA = IA(x, y, 21 * [randint(0, 100)])
			