import pyxel

class Platformer:
    def __init__(self):
        pyxel.init(400, 300, title='Fenetre pyxel test')

        # Position initiale
        self.carreX, self.carreY = 175, 125
        # Taille du pas
        self.pas = 3
        # Vitesse verticale initiale
        self.gravity_speed = 0
        # Gravité
        self.gravity = 0.2

        pyxel.run(self.update, self.draw)

    # Boucle update
    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        # Appliquer la gravité
        self.gravity_speed += self.gravity
        self.carreY += self.gravity_speed

        # Déplacements
        self.carreX, self.carreY = self.deplacements(self.carreX, self.carreY)

        # Limiter le rectangle en bas de l'écran
        if self.carreY >= 250:
            self.carreY = 250
            # Réinitialiser la vitesse verticale lorsque le rectangle touche le sol
            self.gravity_speed = 0

    def draw(self):
        pyxel.cls(0)  # Afficher écran noir à chaque retour ded boucle pour uniquement afficher la fenetre actualisée
        pyxel.rect(self.carreX, self.carreY, 50, 50, 8)  # Rectangle mobile
        pyxel.rect(50, 50, 50, 5, 4)  # Plateforme 1
        pyxel.rect(300, 250, 50, 5, 4)  # Plateforme 2

    # Implémentation déplacements du rectangle
    def deplacements(self, x, y):

    	if pyxel.btn(pyxel.KEY_SPACE):
    		y -= self.pas

    	if pyxel.btn(pyxel.KEY_RIGHT) and x < 340:
    		x += self.pas

    	if pyxel.btn(pyxel.KEY_LEFT) and x > 10:
    		x -= self.pas

    	return x,y

Platformer()
