"""
Classe Metier qui est une énumeration
"""

from enum import Enum

class Metier(Enum):
    Aucun = 0
    Medecin = 1
    Psychiatre = 2
    Cuisinier = 3
    Pecheur = 4
    Professeur = 5