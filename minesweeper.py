#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minesweeper.py
#  

# import du module random
import random
##########################################################################
## constantes
##########################################################################


SIZE = 10

HIDDEN_EMPTY = '0E'
HIDDEN_BOMB  = 'XX'
HIDDEN_FLAG  = '0F'
VISIBL_EMPTY = '1E'
VISIBLE_FLAG = '0F'

# construire le header (concaténation de 2 listes)
HEADER = ['0 '] + [chr(65+x)+' ' for x in range(SIZE)]
#HEADER = ['0 ', 'A ', 'B ', 'C ', 'D ', 'E ', 'F ', 'G ', 'H ', 'I ', 'J ']

##########################################################################
## mécanique de matrice: création, consultation, affectation de valeurs  #
##########################################################################

def create_matrix(size=SIZE):
	""" création d'une matrie avec taille par défaut
	"""
	matrix=[]
	for i in range (0,size):
		line = [HIDDEN_EMPTY]*size
		matrix.append(line)
	return matrix

def set_value(x,y, matrix, value):
	""" obtenir la valeur d'un point de la matrice
	"""
	print ("DEBUG : affecter {} à la position {},{}".format(value,x,y))
	matrix[x][y] = value
	return matrix
	

def get_value(x,y, matrix):
	""" attribuer une valeur à un point de la matrice
	"""
	return matrix[x][y]

##########################################################################
##  simple affichage de la matrice
##########################################################################

def display_matrix(matrix):
	""" Afficher la matrice avec numérotation
	"""
	# afficher ligne vide
	print ("\naffichage de la matrice : \n")

	# header
	# ~ size = len(matrix)
	# ~ header = []
	# ~ header.append('0 ') # 1er col = 0
	# numérotation alphabétique à partir de col 1
	# ~ for x in range(size):
		# ~ header.append(chr(65+x)+' ')
		
	print (HEADER)
	
	i=0
	for line in matrix:
		i+=1
		prefix = [str(i) + ' '] # ajout d'un espace pour l'alignement
		line = prefix + line
		print (line)
		
	# afficher ligne vide
	print("\n")


##########################################################################
##  interractions via input
##########################################################################

def ask_something_to_player(something):
	""" poser une question retourner la réponse (string)
	"""
	return input(something)
	
def ask_yes_or_no(something):
	""" simple controle oui/non 
	"""
	question = something + "O/n ? :"
	answer = ask_something_to_player(question)
	if answer in ['O','o','Y','y','Oui','oui','Yes','yes']:
		return True
	else:
		return False
	
##########################################################################
## Mécanique de jeu à implémenter
########################################################################## 


def random_valid_position_in_matrix(SIZE):
	""" choix d'une position au hasard
	"""
	x = random.randint(0, SIZE-1)
	y = random.randint(0, SIZE-1)
	return x, y
	
	
##########################################################################
##  Fonction principale
########################################################################## 

def main():
	""" déroulé du programme
	"""
	play = True
	while play:
		
		play = ask_yes_or_no("Voulez vous continuer à jouer ? ")
		
		# créer et afficher la matrice
		matrix = create_matrix(SIZE)
		display_matrix(matrix)
		
		# placer une bombe au hasard
		randomX, randomY = random_valid_position_in_matrix(SIZE)
		matrix = set_value(randomX,randomY, matrix, HIDDEN_BOMB)
		
		#afficher la matrice
		display_matrix(matrix)
	
	print ("fin de la partie, bye")
	return 0

# appel de la fonction principale
main()

