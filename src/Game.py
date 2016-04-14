"""
Classe Game qui gère le jeu
"""

from Map import *
from Animation import *

class Game:
	 
	# Constructeur:
	
	def __init__(self):
		
		self.Map = Map()
		
		self.clock = sf.Clock()
		
		self.window = sf.RenderWindow(sf.VideoMode(960, 640), "SINS")
		
		self.key = {"UP": False, "DOWN": False, "RIGHT": False, "LEFT": False}
		
		# Chargement des textures :
			
		# Blocs :
		self.textureEau = sf.Texture.from_file("../files/textures/eau.png")
		self.textureSable = sf.Texture.from_file("../files/textures/sable.png")
		self.textureHerbe = sf.Texture.from_file("../files/textures/herbe.png")
		self.texturePlancher = sf.Texture.from_file("../files/textures/plancher.png")
		self.textureRoute = sf.Texture.from_file("../files/textures/route.png")
		self.textureMur = [sf.Texture.from_file("../files/textures/mur/normal.png"),\
					  sf.Texture.from_file("../files/textures/mur/gauche.png"),\
					  sf.Texture.from_file("../files/textures/mur/droite.png"),\
					  sf.Texture.from_file("../files/textures/mur/angle_gauche.png"),\
					  sf.Texture.from_file("../files/textures/mur/angle_droit.png")]
		
		# IA :
		self.textureIA = sf.Texture.from_file("../files/textures/IA.png")
	
		# Objets :
		self.textureBanc = sf.Texture.from_file("../files/textures/banc.png")
		self.textureLit = sf.Texture.from_file("../files/textures/lit.png")
		self.textureLitMedecin = sf.Texture.from_file("../files/textures/litMedecin.png")
		self.textureLitPsy = sf.Texture.from_file("../files/textures/lit.png")
		self.textureChaise = sf.Texture.from_file("../files/textures/chaise.png")
		self.textureChaiseEcole = sf.Texture.from_file("../files/textures/chaise.png")
		self.textureChaiseMedecin = sf.Texture.from_file("../files/textures/chaise.png")
		self.textureChaisePsy = sf.Texture.from_file("../files/textures/chaisePsy.png")
		self.textureTable = sf.Texture.from_file("../files/textures/table.png")
		self.textureTableEcole = sf.Texture.from_file("../files/textures/table.png")
		self.textureFour = sf.Texture.from_file("../files/textures/four.png")
		self.textureTableau = sf.Texture.from_file("../files/textures/tableau.png")
		self.textureBancPeche = sf.Texture.from_file("../files/textures/banc.png")
		
		# Chargement des sprites :
		
		# Blocs :
		self.spriteEau = sf.Sprite(self.textureEau)
		self.spriteSable = sf.Sprite(self.textureSable)
		self.spriteHerbe = sf.Sprite(self.textureHerbe)
		self.spritePlancher = sf.Sprite(self.texturePlancher)
		self.spriteRoute = sf.Sprite(self.textureRoute)
		self.spriteMur = [sf.Sprite(self.textureMur[0]), sf.Sprite(self.textureMur[1]), sf.Sprite(self.textureMur[2]), sf.Sprite(self.textureMur[3]), sf.Sprite(self.textureMur[4])]
		
		# IA :
		self.spriteIA = sf.Sprite(self.textureIA)
		
		# Objets :
		self.spriteBanc = sf.Sprite(self.textureBanc)
		self.spriteLit = sf.Sprite(self.textureLit)
		self.spriteLitMedecin = sf.Sprite(self.textureLitMedecin)
		self.spriteLitPsy = sf.Sprite(self.textureLit)
		self.spriteChaise = sf.Sprite(self.textureChaise)
		self.spriteChaiseEcole = sf.Sprite(self.textureChaiseEcole)
		self.spriteChaiseMedecin = sf.Sprite(self.textureChaiseMedecin)
		self.spriteChaisePsy = sf.Sprite(self.textureChaisePsy)
		self.spriteTable = sf.Sprite(self.textureTable)
		self.spriteTableEcole = sf.Sprite(self.textureTableEcole)
		self.spriteFour = sf.Sprite(self.textureFour)
		self.spriteTableau = sf.Sprite(self.textureTableau)
		self.spriteBancPeche = sf.Sprite(self.textureBancPeche)
		
		
		# Scrolling :
		
		self.xMin = 0
		self.yMin = 0
		
	# Mise en place du jeu :
		
	def play(self):
		
		# Génération de la map :
		
		self.Map.generate()
		
		# Disposition des maisons :
		for i in range(18):
			self.Map.maison()
		
		# Invocation des IA sur la map
		
		x = randint(0, 95)
		y = randint(0, 71)
		
		while self.Map.map[x][y].Bloc != Bloc.Herbe and self.Map.map[x][y].Bloc != Bloc.Plancher and self.Map.map[x][y].Bloc != Bloc.Sable:
			
			x = randint(0, 95)
			y = randint(0, 71)
			
		self.Map.map[x][y].IA = IA(x, y, 21 * [randint(0, 100)])
		
		x = randint(0, 95)
		y = randint(0, 71)
		
		while self.Map.map[x][y].Bloc != Bloc.Herbe and self.Map.map[x][y].Bloc != Bloc.Plancher and self.Map.map[x][y].Bloc != Bloc.Sable and self.Map.map[x][y].isIA():
			
			x = randint(0, 95)
			y = randint(0, 71)
			
		self.Map.map[x][y].IA = IA(x, y, 21 * [randint(0, 100)])
		
		# Boucle principale :
		
		while self.window.is_open:
			
			# gestion des evenements
			
			for event in self.window.events:
			
				if type(event) is sf.CloseEvent:
					self.window.close()
				
				elif type(event) is sf.KeyEvent:
					if event.code is sf.Keyboard.ESCAPE:
						self.window.close()
					elif event.code is sf.Keyboard.LEFT:
						self.key["LEFT"] = event.pressed
					elif event.code is sf.Keyboard.UP:
						self.key["UP"] = event.pressed
					elif event.code is sf.Keyboard.RIGHT:
						self.key["RIGHT"] = event.pressed
					elif event.code is sf.Keyboard.DOWN:
						self.key["DOWN"] = event.pressed
					
			
			if self.key["LEFT"]:
				self.xMin = self.xMin - 1 if self.xMin > 0 else self.xMin
			if self.key["RIGHT"]:
				self.xMin = self.xMin + 1 if self.xMin < 66 else self.xMin
			if self.key["UP"]:
				self.yMin = self.yMin - 1 if self.yMin > 0 else self.yMin
			if self.key["DOWN"]:
				self.yMin = self.yMin + 1 if self.yMin < 52 else self.yMin
			
			# gestion des IA
			
			x = list()
			y = list()
			
			for i in range(96):
				for j in range(72):
					if self.Map.map[i][j].isIA():
						x.append(i)
						y.append(j)
			
			if(self.clock.elapsed_time.milliseconds > 1000):
				self.clock.restart()
				
				for i in range(len(x)):
						
						# update des valeurs de l'ia
						
						self.Map.map[x[i]][y[i]].IA.fatigue += 1
						self.Map.map[x[i]][y[i]].IA.faim += 1
						self.Map.map[x[i]][y[i]].IA
						
						# déplacement de l'ia
					
						direction = self.Map.map[x[i]][y[i]].IA.getDirection(self.Map.map)
						
						if direction == Direction.Bas and not self.Map.map[x[i]][y[i]+1].isIA():
							self.Map.map[x[i]][y[i]].IA.y += 1
							self.Map.map[x[i]][y[i]+1].IA = self.Map.map[x[i]][y[i]].IA
							self.Map.map[x[i]][y[i]].delIA()
						elif direction == Direction.Haut and not self.Map.map[x[i]][y[i]-1].isIA():
							self.Map.map[x[i]][y[i]].IA.y -= 1
							self.Map.map[x[i]][y[i]-1].IA = self.Map.map[x[i]][y[i]].IA
							self.Map.map[x[i]][y[i]].delIA()
						elif direction == Direction.Gauche and not self.Map.map[x[i]-1][y[i]].isIA():
							self.Map.map[x[i]][y[i]].IA.x -= 1
							self.Map.map[x[i]-1][y[i]].IA = self.Map.map[x[i]][y[i]].IA
							self.Map.map[x[i]][y[i]].delIA()
						elif direction == Direction.Droite and not self.Map.map[x[i]+1][y[i]].isIA():
							self.Map.map[x[i]][y[i]].IA.x += 1
							self.Map.map[x[i]+1][y[i]].IA = self.Map.map[x[i]][y[i]].IA
							self.Map.map[x[i]][y[i]].delIA()
						
						
			
			# affichage de la carte
			
			self.window.clear()
			
			for i in range(self.xMin, self.xMin + 30):
				for j in range(self.yMin, self.yMin + 20):
					
					# affichage des blocs
					
					if self.Map.map[i][j].Bloc == Bloc.Eau:
						self.spriteEau.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteEau)
						
					elif self.Map.map[i][j].Bloc == Bloc.Sable:
						self.spriteSable.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteSable)
					
					elif self.Map.map[i][j].Bloc == Bloc.Herbe:
						self.spriteHerbe.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteHerbe)
						
					elif self.Map.map[i][j].Bloc == Bloc.Plancher:
						self.spritePlancher.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spritePlancher)
					
					elif self.Map.map[i][j].Bloc == Bloc.Route:
						self.spriteRoute.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteRoute)
					
					elif self.Map.map[i][j].Bloc == Bloc.Mur:
						
						if self.Map.map[i-1][j].Bloc == Bloc.Herbe:
							if self.Map.map[i][j+1].Bloc == Bloc.Herbe:
								self.spriteMur[0].position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
								self.window.draw(self.spriteMur[0])
							elif self.Map.map[i][j-1].Bloc == Bloc.Mur or self.Map.map[i][j-1].Bloc == Bloc.Plancher:
								self.spriteMur[1].position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
								self.window.draw(self.spriteMur[1])
							else:
								self.spriteMur[3].position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
								self.window.draw(self.spriteMur[3])
								
						elif self.Map.map[i+1][j].Bloc == Bloc.Herbe:
							if self.Map.map[i][j+1].Bloc == Bloc.Herbe:
								self.spriteMur[0].position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
								self.window.draw(self.spriteMur[0])
							elif self.Map.map[i][j-1].Bloc == Bloc.Mur or self.Map.map[i][j-1].Bloc == Bloc.Plancher:
								self.spriteMur[2].position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
								self.window.draw(self.spriteMur[2])
							else:
								self.spriteMur[4].position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
								self.window.draw(self.spriteMur[4])
						else:
							self.spriteMur[0].position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
							self.window.draw(self.spriteMur[0])
						
					
					# affichage des objets
					
					if self.Map.map[i][j].Objet == Objet.Banc:
						self.spriteBanc.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteBanc)
					
					elif self.Map.map[i][j].Objet == Objet.Lit:
						self.spriteLit.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteLit)
					
					elif self.Map.map[i][j].Objet == Objet.ChaiseEcole:
						self.spriteChaiseEcole.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteChaiseEcole)
					
					elif self.Map.map[i][j].Objet == Objet.TableEcole:
						self.spriteTableEcole.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteTableEcole)
					
					elif self.Map.map[i][j].Objet == Objet.Four:
						self.spriteFour.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteFour)
					
					elif self.Map.map[i][j].Objet == Objet.Chaise:
						self.spriteChaise.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteChaise)
					
					elif self.Map.map[i][j].Objet == Objet.Table:
						self.spriteTable.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteTable)
					
					elif self.Map.map[i][j].Objet == Objet.Tableau:
						self.spriteTableau.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin - 1))
						self.window.draw(self.spriteTableau)
					
					elif self.Map.map[i][j].Objet == Objet.LitMedecin:
						self.spriteLitMedecin.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteLitMedecin)
					
					elif self.Map.map[i][j].Objet == Objet.ChaiseMedecin:
						self.spriteChaiseMedecin.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteChaiseMedecin)
					
					elif self.Map.map[i][j].Objet == Objet.LitPsychiatre:
						self.spriteLitPsy.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteLitPsy)
					
					elif self.Map.map[i][j].Objet == Objet.ChaisePsychiatre:
						self.spriteChaisePsy.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteChaisePsy)
					
					elif self.Map.map[i][j].Objet == Objet.BancPeche:
						self.spriteBancPeche.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteBancPeche)
					
					# affichage des IA
					
					if self.Map.map[i][j].isIA():
						self.spriteIA.position = sf.Vector2(32 * (i - self.xMin), 32 * (j - self.yMin))
						self.window.draw(self.spriteIA)
						
			self.window.display()