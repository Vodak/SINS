class Tile :
	
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
