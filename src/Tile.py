"""
Classe Tile permettant de creer un objet case pouvant contenir un personnage, un bloc et un objet
"""

from IA import *

class Tile :

	# Constructeur
	
	def __init__(self):
		
		self._IA = list()
		self._Bloc = Bloc.Eau
		self._Objet = Objet.Rien
		
		
	# Get List
	
	def isIA(self):
		
		if len(self._IA) == 0:
		    return False
		else:
		    return True
	
	def delIA(self):
		del self._IA[0]
	
	def _get_IA(self):
		return self._IA[0]
	
	def _get_Bloc(self):
		
		return self._Bloc
	
	def _get_Objet(self):
		
		return self._Objet
	
	
	# Set List
	
	def _set_IA(self, IA):
		_IA = list()
		self._IA.append(IA)
		
	def _set_Bloc(self, Bloc):
		
		self._Bloc = Bloc
	
	def _set_Objet(self, Objet):
		
		self._Objet = Objet
		
		
	# Attributs publics de la classe par accès à des attributs privés
	
	IA = property(_get_IA, _set_IA)
	Bloc = property(_get_Bloc, _set_Bloc)
	Objet = property(_get_Objet, _set_Objet)
