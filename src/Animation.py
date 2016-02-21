import sfml as sf

class Animation:
    
    def __init__(self, tableau, temps):
        self.tableau = tableau
        self.temps = temps


    def play(self, fenetre):
        fenetre.clear(sf.Color.White)
        
        for i in range(len(tableau)):
            sf.draw(tableau[i])
            sf.display()
            sf.sleep(temps)
