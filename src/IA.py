"""
Classe d'intelligence artificielle avec des attributs et des méthodes gérant leur actions
"""

class IA:
    
    # Constructeur
    
    def __init__(self):
        self._vie = 100
        self._fatigue = 0
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
    
    # get list
    
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
    
    # set list
    
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
