"""
Classe Game qui gère le jeu
"""

from Map import *

class Game:
	 
	# Constructeur:
	
	def __init__(self):
		
		self._Map = Map()
		
	# Mise en place du jeu :
		
	def play(self):
		
		# Génération de la map :
		
		_Map.generate()
		
		# Disposition des maisons :
		
		_Map.maison()
		
		# Invocation des IA sur la map
		
		x = 0
		y = 0
		
		while _Map[x][y] != Bloc.Herbe and _Map[x][y] != Bloc.Plancher and _Map[x][y] != Bloc.Sable:

			x = randint(0, 95)
			y = randint(0, 71)
			
			_Map[x][y].IA = IA(x, y, 21 * [randint(0, 100)])
			