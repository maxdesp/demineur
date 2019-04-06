#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  minesweeperObject.py
#  

SIZE = 10

HIDDEN_EMPTY = '0E'
HIDDEN_BOMB  = 'XX'
HIDDEN_FLAG  = '0F'
VISIBL_EMPTY = '1E'
VISIBLE_FLAG = '0F'

class Matrix():
	
	def __init__(self, size):
		self.size=size
		self.matrix = []
		 
		for i in range (0, self.size):
			line = [HIDDEN_EMPTY]*size
			self.matrix.append(line)
			
			
	def build_matrix(self):
		for i in range(self.size):
			for j in range(self.size):
				
				block = Block(HIDDEN_EMPTY, i,j)
				self.matrix[i][j] = block
				
	
	def get_block(self, x,y):
		return self.matrix[x,y]
		
	def set_block(self, block, x,y):
		self.matrix[x][y] = block
				
	def display_matrix(self):
		print("\n affichage de la matrice:")
		i=0
		for line in self.matrix:
			print (line)
	

		
				

class Block():
	def __init__(self, value, x, y):
		self.value=value
		self.x = x
		self.y = y
		self.position = [x, y]
	
	
	### les deux fonctions ci-dessous sont des méthodes techniques
	### qui permettent à la fonction "print" d'afficher correctement un objet
	### print(block) va afficher la valeur du block grâce à elles
	def __str__(self):
		return self.value
		
	def __repr__(self):
		return self.__str__()
		


def main():
	matrix = Matrix(SIZE)

	matrix.build_matrix()
	matrix.display_matrix()
	
	bomb = Block(HIDDEN_BOMB, 5,5)
	
	matrix.set_block(bomb, bomb.x, bomb.y)
	
	matrix.display_matrix()
	
	return 0
	
main()
