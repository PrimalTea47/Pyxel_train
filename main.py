import pyxel

pyxel.init(400,300, title='Fenetre pyxel test')

#position initiale
carreX, carreY = 175,125

#implémentation déplacements du rectangle
def deplacements(x,y):
	if pyxel.btn(pyxel.KEY_UP):
		y -= 10
	if pyxel.btn(pyxel.KEY_DOWN):
		y += 10

	if pyxel.btn(pyxel.KEY_RIGHT):
		x += 10
	if pyxel.btn(pyxel.KEY_LEFT):
		x -= 10

	return x,y



#boucle update
def update():
	if pyxel.btn(pyxel.KEY_Q):
		pyxel.quit()

	global carreX, carreY
	carreX,carreY = deplacements(carreX,carreY)
	


def draw():
	#30 verifications/seconde

	pyxel.cls(0) #afficher écran noir à chaque retour ded boucle pour uniquement afficher la fenetre actualisée
	pyxel.rect(carreX, carreY,50,50,8)

pyxel.run(update,draw)