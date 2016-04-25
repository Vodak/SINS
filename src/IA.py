"""
Classe d'intelligence artificielle avec des attributs et des méthodes gérant leur actions
"""

from Action import *
from Metier import *
from math import *
from enum import Enum

class Bloc(Enum):
    Eau = 0
    Sable = 1
    Herbe = 2
    Plancher = 3
    Mur = 4
    Route = 5

class Objet(Enum):
    Rien = 0
    Banc = 1
    Checkpoint = 2
    Lit = 3
    ChaiseEcole = 4
    TableEcole = 5
    Four = 6
    EntreeFour = 7
    Chaise = 8
    Table = 9
    PlaceProf = 10
    Tableau = 11
    LitMedecin = 12
    ChaiseMedecin = 13
    LitPsychiatre = 14
    ChaisePsychiatre = 15
    BancPeche = 16
    
class Direction(Enum):
    Aucune = 0
    Haut = 1
    Droite = 2
    Bas = 3
    Gauche = 4

class IA:
    
    # Constructeur
    
    def __init__(self, x , y, envie):
        self._vie = 100
        self._fatigue = 00
        self._faim = 0
        self._bonheur = 100
        self._maladie = 0
        
        self._charisme = 0
        self._intelligence = 0
        self._force = 0
        self._soumission =0
        self._endurance = 0
        
        self._age = 0
        self._sexe = "rien"
        
        self._x = x
        self._y = y
        
        self._envie = envie
        self._metier = Metier.Aucun
    
    # liste des get
    
    def _get_vie(self):
        return self._vie
    
    def _get_fatigue(self):
        return self._fatigue
    
    def _get_faim(self):
        return self._faim
    
    def _get_bonheur(self):
        return self._bonheur
    
    def _get_maladie(self):
        return self._maladie
    
    def _get_charisme(self):
        return self._charisme
    
    def _get_intelligence(self):
        return self._intelligence
    
    def _get_force(self):
        return self._force
    
    def _get_soumission(self):
        return self._soumission
    
    def _get_endurance(self):
        return self._endurance
    
    def _get_age(self):
        return self._age
    
    def _get_sexe(self):
        return self._sexe
    
    def _get_x(self):
        return self._x
    
    def _get_y(self):
        return self._y
    
    def _get_envie(self):
        return self._envie
    
    def _get_metier(self):
        return self._metier
    
    # list des set
    
    def _set_vie(self, vie):
        if vie < 0:
            self._vie = 0
        elif vie > 100:
            self._vie = 100
        else:
            self._vie = vie
    
    def _set_fatigue(self, fatigue):
        if fatigue < 0:
            self._fatigue = 0
        elif fatigue > 100:
            self._fatigue = 100
        else:
            self._fatigue = fatigue
    
    def _set_faim(self, faim):
        if faim < 0:
            self._faim = 0
        elif faim > 100:
            self._faim = 100
        else:
            self._faim = faim
    
    def _set_bonheur(self, bonheur):
        if bonheur < 0:
            self._bonheur = 0
        elif bonheur > 100:
            self._bonheur = 100
        else:
            self._bonheur = bonheur
    
    def _set_maladie(self, maladie):
        if maladie < 0:
            self._maladie = 0
        elif maladie > 100:
            self._maladie = 100
        else:
            self._maladie = maladie
    
    def _set_charisme(self, charisme):
        if charisme < 0:
            self._charisme = 0
        elif charisme > 100:
            self._charisme = 100
        else:
            self._charisme = charisme
    
    def _set_intelligence(self, intelligence):
        if intelligence < 0:
            self._intelligence = 0
        elif intelligence > 100:
            self._intelligence = 100
        else:
            self._intelligence = intelligence
    
    def _set_force(self, force):
        if force < 0:
            self._force = 0
        elif force > 100:
            self._force = 100
        else:
            self._force = force
    
    def _set_soumission(self, soumission):
        if soumission < 0:
            self._soumission = 0
        elif soumission > 100:
            self._soumission = 100
        else:
            self._soumission = soumission
    
    def _set_endurance(self, endurance):
        if endurance < 0:
            self._endurance = 0
        elif endurance > 100:
            self._endurance = 100
        else:
            self._endurance = endurance
    
    def _set_age(self, age):
        if age < 0:
            self._age = 0
        else:
            self._age = age
    
    def _set_sexe(self, sexe):
        self._sexe = sexe
    
    def _set_x(self, x):
        self._x = x
    
    def _set_y(self, y):
        self._y = y
    
    def _set_envie(self, envie):
        self._envie = envie
    
    def _set_metier(self, metier):
        self._metier = metier
        
    # fonctions pour utiliser l'intelligence artificielle
    
    def getAction(self, carte):
        
        collision = [[0] * 72 for i in range(96)]
        direction = [[Direction.Aucune] * 72 for i in range(96)]
        distance = [[-1] * 72 for i in range(96)]
        
        # tableau des collisions
        
        for i in range(96):
            for j in range(72):
                if carte[i][j].Bloc == Bloc.Mur or carte[i][j].Bloc == Bloc.Eau:
                    collision[i][j] = 1
                    distance[i][j] = -2
                if carte[i][j].Objet == Objet.TableEcole or carte[i][j].Objet == Objet.Four or carte[i][j].Objet == Objet.Table:
                    collision[i][j] = 1
                    distance[i][j] = -2
        
        # tableau des directions et des distances, algorithme de pathfinding
        
        direction[self._x][self._y] = Direction.Aucune
        distance[self._x][self._y] = 0
        
        fini = False
        
        while not fini:
            
            for i in range(self._x, 1, -1):
                for j in range(self._y, 1, -1):
                    if distance[i][j] >= 0:
                        if distance[i-1][j] != -2 and (distance[i-1][j] == -1 or distance[i][j] + 1 < distance[i-1][j]):
                            distance[i-1][j] = distance[i][j] + 1   
                            direction[i-1][j] = Direction.Gauche
                        if distance[i+1][j] != -2 and (distance[i+1][j] == -1 or distance[i][j] + 1 < distance[i+1][j]):
                            distance[i+1][j] = distance[i][j] + 1
                            direction[i+1][j] = Direction.Droite
                        if distance[i][j-1] != -2 and (distance[i][j-1] == -1 or distance[i][j] + 1 < distance[i][j-1]):
                            distance[i][j-1] = distance[i][j] + 1
                            direction[i][j-1] = Direction.Haut
                        if distance[i][j+1] != -2 and (distance[i][j+1] == -1 or distance[i][j] + 1 < distance[i][j+1]):
                            distance[i][j+1] = distance[i][j] + 1
                            direction[i][j+1] = Direction.Bas
        
            for i in range(self._x, 95 ):
                for j in range(self._y, 1, -1):
                    if distance[i][j] >= 0:
                        if distance[i-1][j] != -2 and (distance[i-1][j] == -1 or distance[i][j] + 1 < distance[i-1][j]):
                            distance[i-1][j] = distance[i][j] + 1   
                            direction[i-1][j] = Direction.Gauche
                        if distance[i+1][j] != -2 and (distance[i+1][j] == -1 or distance[i][j] + 1 < distance[i+1][j]):
                            distance[i+1][j] = distance[i][j] + 1
                            direction[i+1][j] = Direction.Droite
                        if distance[i][j-1] != -2 and (distance[i][j-1] == -1 or distance[i][j] + 1 < distance[i][j-1]):
                            distance[i][j-1] = distance[i][j] + 1
                            direction[i][j-1] = Direction.Haut
                        if distance[i][j+1] != -2 and (distance[i][j+1] == -1 or distance[i][j] + 1 < distance[i][j+1]):
                            distance[i][j+1] = distance[i][j] + 1
                            direction[i][j+1] = Direction.Bas
        
            for i in range(self._x, 1, -1):
                for j in range(self._y, 71):
                    if distance[i][j] >= 0:
                        if distance[i-1][j] != -2 and (distance[i-1][j] == -1 or distance[i][j] + 1 < distance[i-1][j]):
                            distance[i-1][j] = distance[i][j] + 1   
                            direction[i-1][j] = Direction.Gauche
                        if distance[i+1][j] != -2 and (distance[i+1][j] == -1 or distance[i][j] + 1 < distance[i+1][j]):
                            distance[i+1][j] = distance[i][j] + 1
                            direction[i+1][j] = Direction.Droite
                        if distance[i][j-1] != -2 and (distance[i][j-1] == -1 or distance[i][j] + 1 < distance[i][j-1]):
                            distance[i][j-1] = distance[i][j] + 1
                            direction[i][j-1] = Direction.Haut
                        if distance[i][j+1] != -2 and (distance[i][j+1] == -1 or distance[i][j] + 1 < distance[i][j+1]):
                            distance[i][j+1] = distance[i][j] + 1
                            direction[i][j+1] = Direction.Bas
        
            for i in range(self._x, 95):
                for j in range(self._y, 71):
                    if distance[i][j] >= 0:
                        if distance[i-1][j] != -2 and (distance[i-1][j] == -1 or distance[i][j] + 1 < distance[i-1][j]):
                            distance[i-1][j] = distance[i][j] + 1   
                            direction[i-1][j] = Direction.Gauche
                        if distance[i+1][j] != -2 and (distance[i+1][j] == -1 or distance[i][j] + 1 < distance[i+1][j]):
                            distance[i+1][j] = distance[i][j] + 1
                            direction[i+1][j] = Direction.Droite
                        if distance[i][j-1] != -2 and (distance[i][j-1] == -1 or distance[i][j] + 1 < distance[i][j-1]):
                            distance[i][j-1] = distance[i][j] + 1
                            direction[i][j-1] = Direction.Haut
                        if distance[i][j+1] != -2 and (distance[i][j+1] == -1 or distance[i][j] + 1 < distance[i][j+1]):
                            distance[i][j+1] = distance[i][j] + 1
                            direction[i][j+1] = Direction.Bas
                         
            fini = True
            
            for i in range(1, 95):
                for j in range(1, 71):
                    if distance[i][j] == -1:
                        fini = False
        
        # test pour chaque interraction
        
        choix = (0, 0, 0)
        
        for i in range(1, 95):
            for j in range(1, 71):
                
                interraction = 0
                
                # interraction avec les objets
                
                if carte[i][j].Objet != Objet.Rien and distance[i][j] != -2:
                    
                    important = False
                    
                    # calcul des envies
                    
                    # très importants
                    
                    if carte[i][j].Objet == Objet.Lit and self._fatigue >= 50:
                        interraction += (self._fatigue + self._envie[2] + 101 - self._vie) / sqrt(distance[i][j] + 1)
                        important = True
                        
                    if carte[i][j].Objet == Objet.EntreeFour and self._faim >= 50:
                        interraction += (self._faim + self._envie[4] + 101 - self._vie + (50 if self._metier == Metier.Cuisinier else 0)) / sqrt(distance[i][j] + 1)
                        important = True
                        
                    if carte[i][j].Objet == Objet.LitMedecin and self._vie <= 50: 
                        interraction += (self._maladie + self._envie[7] + 101 - self._vie) / sqrt(distance[i][j] + 1)
                        important = True
                        
                    if carte[i][j].Objet == Objet.LitPsychiatre and self._bonheur <= 50:
                        interraction += (self._envie[9] + 202 - self._bonheur - self._vie) / sqrt(distance[i][j] + 1)
                        important = True
                    
                    if not important:
                        
                        # importants
                        
                        if carte[i][j].Objet == Objet.BancPeche:
                            interraction += (2 * self._envie[11] + (50 if self._metier == Metier.Pecheur else 0)) / sqrt(distance[i][j] + 1)
                        elif carte[i][j].Objet == Objet.ChaiseEcole:
                            interraction += (0.8 * (self._envie[6] + 25) + (100 if (self._age >= 5 and self._age <= 15) else 15)) / sqrt(distance[i][j] + 1)
                        elif carte[i][j].Objet == Objet.PlaceProf:
                            interraction += (self._envie[5] + (50 if self._metier == Metier.Professeur else 0)) / sqrt(distance[i][j] + 1)
                        elif carte[i][j].Objet == Objet.ChaiseMedecin:
                            interraction += (self._envie[8] + (50 if self._metier == Metier.Medecin else 0)) / sqrt(distance[i][j] + 1)
                        elif carte[i][j].Objet == Objet.ChaisePsychiatre:
                            interraction += (self._envie[10] + (50 if self._metier == Metier.Psychiatre else 0)) / sqrt(distance[i][j] + 1)
                        
                        # peu importants
                        
                        elif carte[i][j].Objet == Objet.Banc:
                            interraction += (0.8 * (self._envie[2] + self._fatigue)) / sqrt(distance[i][j] + 1) if self._fatigue < 50 else (0.5 * (self._envie[2] + self._fatigue)) / sqrt(distance[i][j] + 1)
                        elif carte[i][j].Objet == Objet.Chaise:
                            interraction += (0.8 * (self._envie[0] + self._fatigue)) / sqrt(distance[i][j] + 1) if self._fatigue < 50 else (0.5 * (self._envie[0] + self._fatigue)) / sqrt(distance[i][j] + 1)
                        elif carte[i][j].Objet == Objet.Checkpoint:
                            interraction += (1.2 * (self._envie[1] - self._fatigue)) / sqrt(distance[i][j] + 1)
                        
                    if interraction > choix[2]:
                        choix = (i, j, interraction)
                
                # interractions avec les autres IA
                
                if carte[i][j].isIA() and carte[i][j].IA != self:
                    
                    # calcul d'envie d'interraction
                    
                    if interraction > choix[2]:
                        choix = (i, j, interraction)
        
        # détermination de la direction à suivre
        
        x = choix[0]
        y = choix[1]
        
        directionRetour = direction[x][y]
        
        while x != self._x or y != self._y:
            directionRetour = direction[x][y]
            
            if direction[x][y] == Direction.Haut:
                y += 1
            elif direction[x][y] == Direction.Droite:
                x -= 1
            elif direction[x][y] == Direction.Bas:
                y -= 1
            elif direction[x][y] == Direction.Gauche:
                x += 1
        
        return directionRetour, True if distance[x][y] <= 1 else False
        
    # Attributs publics de la classe par accès à des attributs privés
    
    vie = property(_get_vie, _set_vie)
    fatigue = property(_get_fatigue, _set_fatigue)
    faim = property(_get_faim, _set_faim)
    bonheur = property(_get_bonheur, _set_bonheur)
    maladie = property(_get_maladie, _set_maladie)
    charisme = property(_get_charisme, _set_charisme)
    intelligence = property(_get_intelligence, _set_intelligence)
    force = property(_get_force, _set_force)
    soumission = property(_get_soumission, _set_soumission)
    endurance = property(_get_endurance, _set_endurance)
    age = property(_get_age, _set_age)
    sexe = property(_get_sexe, _set_sexe)
    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)
    envie = property(_get_envie, _set_envie)
    metier = property(_get_metier, _set_metier)
