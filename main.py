import pyxel
import random


class Platformer:
	def __init__(self):
		pyxel.init(400,300, title='Fenetre pyxel test')

		#position initiale
		self.carreX, self.carreY = 175,125
		
		pyxel.run(self.update,self.draw)

	

	#boucle update
	def update(self):
		if pyxel.btn(pyxel.KEY_Q):
			pyxel.quit()

		self.carreX,self.carreY = self.deplacements(self.carreX,self.carreY)
		


	

	def draw(self):
		#30 verifications/seconde

		pyxel.cls(0) #afficher écran noir à chaque retour ded boucle pour uniquement afficher la fenetre actualisée
		pyxel.rect(self.carreX, self.carreY,50,50,8) #rectangle mobile
		pyxel.rect(300,200,10,10,random.randint(1,15))



	#implémentation déplacements du rectangle
	def deplacements(self,x,y):
		if pyxel.btn(pyxel.KEY_UP) and y > 10:
			y -= 10
		if pyxel.btn(pyxel.KEY_DOWN) and y < 240:
			y += 10

		if pyxel.btn(pyxel.KEY_RIGHT) and x < 340:
			x += 10
		if pyxel.btn(pyxel.KEY_LEFT) and x > 10:
			x -= 10

		return x,y




Platformer()