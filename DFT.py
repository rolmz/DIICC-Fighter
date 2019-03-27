#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import sys
import time
from pygame.locals import *

pixel = 650
Nahur = pygame.image.load("Image/Avatar/Nahur.jpg")
Servando = pygame.image.load("Image/Avatar/Servando.jpg")
Miguel = pygame.image.load("Image/Avatar/Miguel.jpg")
Cornide = pygame.image.load("Image/Avatar/Cornide.jpg")
Monasterio = pygame.image.load("Image/Avatar/Monasterio.jpg")
Jorge = pygame.image.load("Image/Avatar/Jorge.jpg")

class eleccion(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #Clase base para mostrar objetos
		self.Indicador = pygame.image.load("Image/Player1.png") #Cargar imagenes jugador
		self.rect = self.Indicador.get_rect()

		self.rect.centerx = 430
		self.rect.centery =125
		self.Velocidad = 200
		self.Mover = True
		self.elegido = False
		self.PersonajeElegido = "x" # url personaje elegido
		self.nombre = "x" # nombre personaje

	def SetImagen(self, posx, posy, imagen):
		self.Indicador = pygame.image.load(imagen)
		self.rect.centerx = posx
		self.rect.centery = posy

	def obtenerpos(self):
		return self.rect.centerx, self.rect.centery

	def dibujar(self, superficie):
		superficie.blit(self.Indicador, self.rect)

	def movimientoH(self): #Movimiento horizontal jugador
		if self.rect.centerx <= 430:
			self.rect.centerx = 430
		elif self.rect.centerx >= 870:
			self.rect.centerx = 870
			
	def movimientoV1(self): #Movimiento vertical jugador
		if self.rect.centery <= 100:
			self.rect.centery = 100
		elif self.rect.bottom >= 500:
			self.rect.bottom = 500

	def movimientoV2(self): #Movimiento vertical jugador
		if self.rect.centery <= 130:
			self.rect.centery = 130
		elif self.rect.bottom >= 530:
			self.rect.bottom = 530

	def personaje(self, P):
		x, y = self.obtenerpos()
		if x == 430:
			if y >= 100 and y <= 130:
				person = "Nahur"
			elif y >= 200 and y <= 330:
				person = "Servando"
			else:
				person = "Jorge"
		elif x == 870:
			if y >= 100 and y <= 130:
				person = "Cornide"
			elif y >= 200 and y <= 330:
				person = "Monasterio"
			else:
				person = "Miguel"
		self.__BDpersonajes(person, P)

	def __BDpersonajes(self, person, P):
		self.PersonajeElegido = "Image/" + str(P) + "/" + str(person) + ".png"
		self.nombre = person

class player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self) #Clase base para mostrar objetos
		self.ImagenJugador = pygame.image.load("Image/P1/Nahur.png") #Cargar imagenes jugador
		self.rect = self.ImagenJugador.get_rect()
		self.rect.centerx = pixel/3
		self.rect.centery = pixel - 300

		self.Vida = 100
		self.Energia = 1
		self.Fuerza = 10
		self.Velocidad = 20
		self.Victoria = 0

	def SetPosicion(self, x, y):
		self.ImagenJugador = y
		self.rect.centerx = x

	def obtenerpos(self):
		return self.rect.centerx, self.rect.centery

	def dibujar(self, superficie):
		superficie.blit(self.ImagenJugador, self.rect) #Posicionamiento de jugador en pantalla
		
	def movimientoH(self): #Movimiento horizontal jugador
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right >= 2*pixel:
				self.rect.right = 2*pixel

class menu_principal(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.Puntero = pygame.image.load("Image/Indicador.png")
		self.rect = self.Puntero.get_rect()
		self.rect.centerx = 500
		self.rect.centery = 535

	def SetPosicion(self, x, y):
		self.rect.centerx = x
		self.rect.centery = y

	def obtenerposY(self):
		return self.rect.centery

	def dibujar(self, superficie):
		superficie.blit(self.Puntero, self.rect)

	def vertical(self, posy1, posy2):
		if self.rect.centery <= posy1:
			self.rect.centery = posy1
		elif self.rect.centery >= posy2:
			self.rect.centery = posy2

	def SoN(self):
		y = self.obtenerposY()

		if y == 535:
			return 1
		elif y == 575:
			return 2
		else:
			return 3

class continuar(menu_principal):
	pass
		
	def SoN(self, posy):
		y = self.obtenerposY()

		if y == posy:
			return True
		else:
			return False

def CoGO(CYN, ventana, C, yes, no): # Funcion de continuar o salir del juego
	aux = 0
	ventana.fill((0,0,0))
	Mover_Continua = pygame.mixer.Sound("Sounds/Mover.wav")

	ventana.blit(C,(450,150))
	ventana.blit(yes,(550,335))
	ventana.blit(no,(550,435))

	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

		CYN.vertical(370,470)

		if evento.type == KEYDOWN:
			if evento.key == K_w or evento.key == K_UP:
				CYN.rect.top -= 100
				Mover_Continua.play()

			elif evento.key == K_s or evento.key == K_DOWN:
				CYN.rect.bottom += 100
				Mover_Continua.play()

			elif evento.key == K_v or evento.key ==K_RETURN:
				SeguirJugando = CYN.SoN(370)
				aux = 1

	CYN.dibujar(ventana)
	pygame.display.update()

	if aux == 1:
		return False, SeguirJugando
	else:
		return True, True

def F_elegir(J1, J2, ventana): # Funcion de eleccion de personajes
	EP = pygame.mixer.Sound("Sounds/Mover.wav") # Sonido al moverse en la eleccion
	EE = pygame.mixer.Sound("Sounds/Elegir.wav") # Sonido al elegir personaje
	ColorLinea = (0,0,0)

	J1.movimientoH()
	J1.movimientoV1()
	J2.movimientoH()
	J2.movimientoV2()

	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

		if evento.type == KEYDOWN:				
			if J1.elegido == False:
				if evento.key == K_a:
					J1.rect.left -= (2*J1.Velocidad + 40)
					EP.play()
		
				elif evento.key == K_d:
					J1.rect.right += (2*J1.Velocidad + 40)
					EP.play() 
		
				elif evento.key == K_w:
					J1.rect.top -= J1.Velocidad
					EP.play()
		
				elif evento.key == K_s:
					J1.rect.bottom += J1.Velocidad
					EP.play()
							
				elif evento.key == K_SPACE:
					J1.personaje("P1")
					J1.elegido = True
					EE.play()
																		
			if J2.elegido == False:
				if evento.key == K_LEFT:
					J2.rect.left -= (2*J2.Velocidad + 40)
					EP.play()
		
				elif evento.key == K_RIGHT:
					J2.rect.right += (2*J2.Velocidad + 40) 
					EP.play()
		
				elif evento.key == K_UP:	
					J2.rect.top -= J2.Velocidad
					EP.play()
		
				elif evento.key == K_DOWN:
					J2.rect.bottom += J2.Velocidad
					EP.play()
							
				elif evento.key == K_p:
					J2.personaje("P2")
					J2.elegido = True
					EE.play()
					
		ventana.fill((192,192,192))

		if J1.elegido == True:
			imagenJ = pygame.image.load(J1.PersonajeElegido)
			ventana.blit(imagenJ,(50,pixel-600))
			
		if J2.elegido == True:
			imagenE = pygame.image.load(J2.PersonajeElegido)
			ventana.blit(imagenE,(900,pixel-600))

		ventana.blit(Nahur,(450,25))
		ventana.blit(Servando,(450,225))
		ventana.blit(Jorge,(450,425))
		ventana.blit(Cornide,(650,25))
		ventana.blit(Monasterio,(650,225))
		ventana.blit(Miguel,(650,425))

		pygame.draw.line(ventana,ColorLinea,(450,25),(850,25),5)
		pygame.draw.line(ventana,ColorLinea,(450,225),(850,225),5)
		pygame.draw.line(ventana,ColorLinea,(450,425),(850,425),5)
		pygame.draw.line(ventana,ColorLinea,(450,625),(850,625),5)
		pygame.draw.line(ventana,ColorLinea,(450,25),(450,625),5)
		pygame.draw.line(ventana,ColorLinea,(650,25),(650,625),5)
		pygame.draw.line(ventana,ColorLinea,(850,25),(850,625),5)
		J1.dibujar(ventana)
		J2.dibujar(ventana)
		pygame.display.update()	

		if J1.elegido == True and J2.elegido == True:
			return False
		else:
			return True

def menu_inicio(menu, ventana, inicio):
	color = (255,255,255)
	fuente_menu = pygame.font.Font("Capture_it.ttf",35)
	fuente_autor = pygame.font.Font("Montserrat-SemiBold.otf",15)

	logo = pygame.image.load("Image/LogoDFT.png")
	start = fuente_menu.render("Start Game",0,color)
	controls = fuente_menu.render("Controls",0,color)
	exit = fuente_menu.render("Exit",0,color)
	autor = fuente_autor.render("Rodrigo Oliva - 2016",0,color)

	Mover_Continua = pygame.mixer.Sound("Sounds/Mover.wav")
	Elegir = pygame.mixer.Sound("Sounds/ElegirInicio.wav")

	while inicio == True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			menu.vertical(535,615)

			if evento.type == KEYDOWN:
				if evento.key == K_w or evento.key == K_UP:
					menu.rect.top -= 40
					Mover_Continua.play()

				elif evento.key == K_s or evento.key == K_DOWN:
					menu.rect.bottom += 40
					Mover_Continua.play()

				elif evento.key == K_v or evento.key == K_RETURN:
					Elegir.play()
					EntrarSalir = menu.SoN()
					inicio = False

		ventana.fill((0,0,0))
		ventana.blit(logo,(360,10))
		ventana.blit(start,(550,520))
		ventana.blit(controls,(550,560))
		ventana.blit(exit,(550,600))
		ventana.blit(autor,(1130,630))
		menu.dibujar(ventana)
		pygame.display.update()

	if inicio == False:
		if EntrarSalir == 1:
			return False, EntrarSalir
		elif EntrarSalir == 2:
			controles(menu, ventana, Elegir)
			return True, EntrarSalir
		else:
			sys.exit()

def controles(menu, ventana, Elegir):
	fuente = pygame.font.Font("Montserrat-SemiBold.otf",30)

	F1 = "                                                           Player 1               Player 2"
	F2 = "Up                                                     W                          Arrow keys"
	F3 = "Down                                               S                           Arrow keys"
	F4 = "Left                                                   A                           Arrow keys"
	F5 = "Right                                                D                           Arrow keys"
	F6 = "Punch                                              Space                 P"
	F7 = "Continue/Start Game              V                           Enter"
		
	puntero = pygame.image.load("Image/Indicador.png")
	inicio = True

	F11 = fuente.render(F1,0,(255,255,255))
	F22 = fuente.render(F2,0,(255,255,255))
	F33 = fuente.render(F3,0,(255,255,255))
	F44 = fuente.render(F4,0,(255,255,255))
	F55 = fuente.render(F5,0,(255,255,255))
	F66 = fuente.render(F6,0,(255,255,255))
	F77 = fuente.render(F7,0,(255,255,255))
	control = fuente.render("CONTROLS",0,(255,255,255))
	retornar = fuente.render("RETURN",0,(255,255,255))

	ventana.fill((0,0,0))
	ventana.blit(control,(600,10))
	ventana.blit(F11,(250,100))
	ventana.blit(F22,(250,150))
	ventana.blit(F33,(250,200))
	ventana.blit(F44,(250,250))
	ventana.blit(F55,(250,300))
	ventana.blit(F66,(250,350))
	ventana.blit(F77,(250,400))
	ventana.blit(puntero,(850,555))
	ventana.blit(retornar,(900,575))
	pygame.display.update()

	while inicio == True:
		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()
				sys.exit()

			if evento.type == KEYDOWN:
				if evento.key == K_v or evento.key == K_RETURN:
					Elegir.play()
					inicio = False
	
def ronda(Nround):
	if Nround == 1:
		n = pygame.mixer.Sound("Sounds/Round1.wav")
	elif Nround == 2:
		n = pygame.mixer.Sound("Sounds/Round2.wav")
	else:
		n = pygame.mixer.Sound("Sounds/Round3.wav")

	n.play()	

def boxing():
	pygame.init()
	pygame.font.init()
	ventana = pygame.display.set_mode((2*pixel,pixel)) #Creacion ventana
	pygame.display.set_caption("DIICC Fighter Turbo")
	color = (255,255,255)
	fondo = pygame.image.load("Image/fondo.jpg")

	jugador = player()
	enemigo = player()

	J1 = eleccion()
	J2 = eleccion()
	M = menu_principal()
	CYN = continuar()

	fuente = pygame.font.Font("Montserrat-SemiBold.otf",28)
	fuenteC = pygame.font.Font("Capture_it.ttf",90)
	fuenteYN = pygame.font.Font("Capture_it.ttf",75) 
	C = fuenteC.render("Continue?",0,color)
	yes = fuenteYN.render("Yes",0,color)
	no = fuenteYN.render("No",0,color)	
 
	SonidoGolpe = pygame.mixer.Sound("Sounds/golpe.wav")
	KO = pygame.mixer.Sound("Sounds/KO.wav")
	SI = pygame.mixer.Sound("Sounds/Si.wav")
	NO = pygame.mixer.Sound("Sounds/No.wav")

	Bround = True
	Nround = 1
	B_eleccion = False # Variable que permite tocar la cancion de elección de personajes
	B_eleccion2 = False
	B_pelea = False # Variable que permite tocar la cancion de pelea
	B_continuar = False # Variable que permite tocar la cancion en pantalla de continua/GameOver
	aux = 0
	inicio = True # Variable menu principal
	EntrarSalir = True
	
	J1.SetImagen(430,100,"Image/Player1.png")
	J2.SetImagen(430,130,"Image/Player2.png")
		
	while True:
		if inicio == True: # Menu Inicio
			pygame.mixer.music.load("Sounds/MusicaInicio.mp3")
			pygame.mixer.music.play(10)
			
			while inicio == True:
				inicio, EntrarSalir = menu_inicio(M, ventana, inicio)

			pygame.mixer.music.stop()
			inicio = False
			B_eleccion = True
			B_eleccion2 = True	
		
		elif B_eleccion == True: # Elegir Personajes
			bucle = True

			if B_eleccion2 == True:
				B_eleccion2 = False
				pygame.mixer.music.load("Sounds/CancionCaracter.mp3")
				pygame.mixer.music.play(2)
						
			while bucle == True:
				bucle = F_elegir(J1,J2,ventana)

			if bucle == False:
				time.sleep(2)
				B_eleccion = False
				B_pelea = True
				pygame.mixer.music.stop()
				
		elif B_pelea == True: # Pelea
			imagenJ = pygame.image.load(J1.PersonajeElegido)
			imagenE = pygame.image.load(J2.PersonajeElegido)
			energiaP1 = pygame.image.load("Image/P1/bar1.png")
			energiaP2 = pygame.image.load("Image/P2/bar1.png")

			P1I2 = "Image/P1/" + str(J1.nombre) + "2.png"
			P2I2 = "Image/P2/" + str(J2.nombre) + "2.png"

			ronda(Nround)
			pygame.mixer.music.load("Sounds/musica.mp3")
			pygame.mixer.music.play(2)

			jugador.SetPosicion(pixel/3, imagenJ)
			enemigo.SetPosicion(2*pixel - 200, imagenE)

			P11 = fuente.render(J1.nombre,0,color)
			P22 = fuente.render(J2.nombre,0,color)

			while Bround == True:
				jugador.movimientoH()
				enemigo.movimientoH()

				for evento in pygame.event.get():
					if evento.type == QUIT:
						pygame.quit()
						sys.exit()

					elif jugador.Vida > 0 and enemigo.Vida > 0:

						if evento.type == pygame.KEYDOWN:

							if evento.key == K_a:
								jugador.rect.left -= jugador.Velocidad # disminuye la coordenanda de la esquina izquierda del rectangulo
					
							elif evento.key == K_d:
								if (jugador.rect.right + jugador.Velocidad) < (enemigo.rect.left + 30):
									jugador.rect.right += jugador.Velocidad  # disminuye la coordenanda de la esquina derecha del rectangulo
							
							elif evento.key == K_SPACE:
								jugador.ImagenJugador = pygame.image.load(P1I2)
								jugador.dibujar(ventana)

								SonidoGolpe.play()

							elif evento.key == K_LEFT:
								if (jugador.rect.right + jugador.Velocidad) < (enemigo.rect.left + 30):
									enemigo.rect.left -= enemigo.Velocidad

							elif evento.key == K_RIGHT:
								enemigo.rect.right += enemigo.Velocidad

							elif evento.key == K_p:
								enemigo.ImagenJugador = pygame.image.load(P2I2)
								enemigo.dibujar(ventana)

								SonidoGolpe.play()
										
						elif evento.type == pygame.KEYUP:
							if evento.key == K_SPACE:
								jugador.ImagenJugador = pygame.image.load(J1.PersonajeElegido)
								jugador.dibujar(ventana)

								if (jugador.rect.right + 60) >= enemigo.rect.left: # Si P1 esta muy cerca de P2 y golpea le hace daño
									enemigo.Vida -= jugador.Fuerza
									enemigo.Energia += 1
									cadena = "Image/P2/bar" + str(enemigo.Energia) + ".png"
									energiaP2 = pygame.image.load(cadena)
								
							elif evento.key == K_p:
								enemigo.ImagenJugador = pygame.image.load(J2.PersonajeElegido)
								enemigo.dibujar(ventana)

								if (jugador.rect.right + 60) >= enemigo.rect.left: # Si P2 esta muy cerca de P1 y golpea le hace daño
									jugador.Vida -= enemigo.Fuerza
									jugador.Energia += 1
									cadena = "Image/P1/bar" + str(jugador.Energia) + ".png"
									energiaP1 = pygame.image.load(cadena)
							
					if jugador.Vida == 0 or enemigo.Vida == 0:
						pygame.mixer.music.stop()				
						KO.play()

						KOround = pygame.image.load("Image/KO.png")

						if jugador.Vida == 0:
							enemigo.Victoria += 1
							
							if enemigo.Victoria == 1:
								cadena = "Image/icono.png"
							else:
								cadena = "Image/icono2.png"

							VP2 = pygame.image.load(cadena)

						else:
							jugador.Victoria += 1
							
							if jugador.Victoria == 1:
								cadena = "Image/icono.png"
							else:
								cadena = "Image/icono2.png"

							VP1 = pygame.image.load(cadena)

				ventana.blit(fondo,(0,0))
				ventana.blit(P11,(30,0))
				ventana.blit(P22,(2*pixel-250,0))
				ventana.blit(energiaP1,(20,30))
				ventana.blit(energiaP2,(2*pixel-260,30))

				if jugador.Victoria > 0:
					ventana.blit(VP1,(265,40))

				if enemigo.Victoria > 0:
					ventana.blit(VP2, (2*pixel - 312,40))

				jugador.dibujar(ventana)
				enemigo.dibujar(ventana)
				pygame.display.update()

				if jugador.Vida == 0 or enemigo.Vida == 0:
					ventana.blit(KOround,(300,100))
					pygame.display.update()
					time.sleep(5)
					Bround = False

			if jugador.Victoria == 2 or enemigo.Victoria == 2:
				B_pelea = False
				B_continuar = True				

			Bround = True
			Nround += 1 # Numero del round
			jugador.Energia = 1
			enemigo.Energia = 1
			jugador.Vida = 100
			enemigo.Vida = 100

		elif B_continuar == True: # Continue
			juego = True

			if B_continuar == True:
				B_continuar = False
				CYN.SetPosicion(500,370)
				pygame.mixer.music.load("Sounds/Continue.mp3")
				pygame.mixer.music.play(2)

			while juego == True:
				juego, SeguirJugando = CoGO(CYN, ventana, C, yes, no) # Funcion continuar o salir del juego (Game Over)

			pygame.mixer.music.stop()
			J1.elegido = False
			J2.elegido = False
			Nround = 1
			jugador.Victoria = 0
			enemigo.Victoria = 0
		
			if SeguirJugando == True:
				SI.play()
				B_eleccion = True
				B_eleccion2 = True
				time.sleep(4)
			else:
				NO.play()
				time.sleep(4)
				inicio = True
		
boxing()