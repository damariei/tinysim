__author__ = 'damariei'

import random


# Game Utility Classes/Functions

def genSeq():
	s = random.randint(0,17)
	a = random.randint(0,17)
	v = random.randint(0,17)
	e = random.randint(0,17)
	seq = chr(s+ord('a'))+chr(a+ord('a'))+chr(v+ord('a'))+chr(e+ord('a'))
	return seq

class InputBuffer:

	def __init__(self):
		self.buffer = ''

	def add(self, char):
		self.buffer = str(self.buffer)+chr(char)

	def get(self):
		return self.buffer

	def clear(self):
		self.buffer = ''

	def getandclear(self):
		tmp = self.buffer
		self.buffer = ''
		return tmp

	def count(self):
		return len(self.buffer)