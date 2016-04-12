"""
Classe Game qui gère le jeu
"""

from Map import *
from Animation import *


class Game:
	 
	# Constructeur:
	
	def __init__(self):
		
		self.Map = Map()
		
		self.window = sf.RenderWindow(sf.VideoMode(960, 640), "SINS")
		
		# Chargement des textures :
		
		self.textureEau = sf.Texture.from_file("../files/textures/eau.png")
		self.textureSable = sf.Texture.from_file("../files/textures/sable.png")
		self.textureHerbe = sf.Texture.from_file("../files/textures/herbe.png")
		self.texturePlancher = sf.Texture.from_file("../files/textures/plancher.png")
		self.textureMur = [sf.Texture.from_file("../files/textures/mur/normal.png"),\
					  sf.Texture.from_file("../files/textures/mur/gauche.png"),\
					  sf.Texture.from_file("../files/textures/mur/droite.png"),\
					  sf.Texture.from_file("../files/textures/mur/angle_gauche.png"),\
					  sf.Texture.from_file("../files/textures/mur/angle_droit.png")]
	
		# Chargement des sprites :
		
		self.spriteEau = sf.Sprite(self.textureEau)
		self.spriteSable = sf.Sprite(self.textureSable)
		self.spriteHerbe = sf.Sprite(self.textureHerbe)
		self.spritePlancher = sf.Sprite(self.texturePlancher)
		self.spriteMur = [sf.Sprite(self.textureMur[0]), sf.Sprite(self.textureMur[1]), sf.Sprite(self.textureMur[2]), sf.Sprite(self.textureMur[3]), sf.Sprite(self.textureMur[4])]
		
		# Scrolling :
		
		self.xMin = 0
		self.yMin = 0
		
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
			
		# Boucle principale :
		
		while self.window.is_open:
			
			for event in self.window.events:
				
				if type(event) is sf.CloseEvent:
					self.window.close()
				
				elif type(event) is sf.KeyEvent:
					if event.code is sf.Keyboard.ESCAPE:
						self.window.close()
					elif event.code is sf.Keyboard.LEFT:
						self.xMin = self.xMin - 1 if self.xMin > 0 else self.xMin
					elif event.code is sf.Keyboard.UP:
						self.yMin = self.yMin - 1 if self.yMin > 0 else self.yMin
					elif event.code is sf.Keyboard.RIGHT:
						self.xMin = self.xMin + 1 if self.xMin < 66 else self.xMin
					elif event.code is sf.Keyboard.DOWN:
						self.yMin = self.yMin + 1 if self.yMin < 52 else self.yMin
					
			
			self.window.clear()
			
			for i in range(self.xMin, self.xMin + 30):
				for j in range(self.yMin, self.yMin + 20):
					
					if self.Map.map[i][j] == Bloc.Eau:
						self.spriteEau.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteEau)
						
					elif self.Map.map[i][j] == Bloc.Sable:
						self.spriteSable.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteSable)
					
					elif self.Map.map[i][j] == Bloc.Herbe:
						self.spriteHerbe.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteHerbe)
						
					elif self.Map.map[i][j] == Bloc.Plancher  or self.Map.map[i][j] == Bloc.Route:
						self.spritePlancher.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spritePlancher)
						
					elif self.Map.map[i][j] == Bloc.Mur:
						self.spriteMur[0].position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteMur[0])
			
			self.window.display()