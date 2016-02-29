"""
Classe Tile permettant de creer un objet case pouvant contenir un personnage, un bloc et un objet
"""

from IA import *
from Bloc import *
from Objet import *

class Tile :

	# Constructeur
	
	def __init__(self):
		
		self._IA = IA()
		self._Bloc = Bloc()
		self._Objet = Objet()
		
		
	# Get List
	
	def _get_IA(self):
		
		return self._IA
	
	def _get_Bloc(self):
		
		return self._Bloc
	
	def _get_Objet(self):
		
		return self._Objet
	
	
	# Set List
	
	def _set_IA(self, IA):
		
		self._IA = IA
		
	def _set_Bloc(self, Bloc):
		
		self._Bloc = Bloc
	
	def _set_Objet(self, IA):
		
		self._Objet = Objet
		
		
	# Attributs publics de la classe par accès à des attributs privés
	
	IA = property(_get_IA, _set_IA)
	Bloc = property(_get_Bloc, _set_Bloc)
	Objet = property(_get_Objet, _set_Objet)
