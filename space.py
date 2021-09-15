import pygame  # necessaire pour charger les images et les sons

class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.position = 400
        self.image = pygame.image.load("vaisseau.png")
        self.sens = "O"
        self.vitesse = 1

    def deplacer(self) :
        if (self.sens == "droite") and (self.position < 740):
            self.position = self.position + self.vitesse
        elif (self.sens == "gauche") and (self.position > 0):
           self.position = self.position - self.vitesse
    
    def tirer(self):
        self.sens = "0"
    
class Balle():
    def __init__(self, tireur):
        self.tireur = tireur
        self.depart = tireur.position + 16
        self.hauteur = 492
        self.image = pygame.image.load("balle.png")
        self.etat = "chargee"
        
    def bouger(self):
        if self.etat == "attente":
            self.depart = self.tireur.position + 16
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - 5
        
        if self.hauteur > 0:
            self.etat = "chargee"

class Ennemi():
    def __init__(self, NbEnnemi):
        self.depart = self.tireur.position + 16
        self.hauteur = 0
        
        for NbEnnemi1:
            self.type =
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        
        for NbEnnemi2:
            self.type =
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 2
        
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
