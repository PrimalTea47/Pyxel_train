import pyxel

pyxel.init(400,300, title='Fenetre pyxel test')


#boucle update
def update():
	if pyxel.btn(pyxel.KEY_Q):
		pyxel.quit()

	#implémentation déplacements du rectangle
	


def draw():
	pyxel.cls(0) #afficher écran noir à chaque retour ded boucle pour uniquement afficher la fenetre actualisée
	pyxel.rect(175,125,50,50,8)

pyxel.run(update,draw)