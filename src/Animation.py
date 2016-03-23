"""
Classe animation permettant de créer et d'utiliser des animations à partir d'images et de temps entre elles
"""

import sfml as sf

class Animation:
    
    # Constructeur
    
    def __init__(self, tableau, temps):
        self.tableau = tableau
        self.temps = temps

    # Classe utiliser lançant l'animation
    
    def utiliser(self, fenetre):
        fenetre.clear(sf.Color.White)
        
        # Chaque image est affichée un certain temps
        
        for i in range(len(self.tableau)):
            sf.draw(self.tableau[i])
            sf.display()
            sf.sleep(self.temps)
