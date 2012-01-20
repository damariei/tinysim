__author__ = 'damariei'

import random

class Thing:

	def __init__(self):
		pass


	def construct(self, seq):
		"""
		Constructs a Thing, given a SAVE sequence
		Each sequence code must be between a-r
		i.e: 'brif'
		Returns True if successful
		"""

		#Check sequence for errors
		if not len(seq)==4:
			return False
		for code in seq:
			if code<'a' or code>'r':
				return False

		#Convert codes to numbers
		self.s = ord(seq[0:1])-ord('a')-9
		self.a = ord(seq[1:2])-ord('a')-9
		self.v = ord(seq[2:3])-ord('a')-9
		self.e = ord(seq[3:4])-ord('a')-9

		#Set seq and name
		self.seq = seq

		vowel_list = ['a','e','i','o']
		constants_list = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r']

		self.name = ''
		for i in range(0,3):
			toadd = seq[i:i+1]
			if vowel_list.count(seq[i:i+1])>0 and vowel_list.count(seq[i+1:i+2])>0:
				toadd = toadd+constants_list[random.randint(0,len(constants_list)-1)]
			elif constants_list.count(seq[i:i+1])>0 and constants_list.count(seq[i+1:i+2])>0:
				toadd += vowel_list[random.randint(0,len(vowel_list)-1)]
			self.name += toadd
			
		self.name += seq[3:4]
		self.name = self.name.capitalize()

		#Set LEAD stats
		self.maxlife = 100+(self.v*10)
		self.maxenergy = 100+(self.e*10)
		self.attack = 10+self.s
		self.defence = 10+self.a

		#Set Current stats
		self.life = self.maxlife
		self.energy = self.maxenergy

		#Set D/R Rates
		self.drainrate = 5-(self.e/2)
		self.recrate = 10+self.e

		return True

	def getSeqAsList(self):
		return [self.s,self.a,self.v,self.e]

	def compareTo(self, seq):
		"""
		Compares this Thing's sequence to another one.
		Returns a ratio of difference.
		i.e: 'abcd' with 'abcd'
		returns 0.0
		"""
		s2 = ord(seq[0:1])-ord('a')-9
		a2 = ord(seq[1:2])-ord('a')-9
		v2 = ord(seq[2:3])-ord('a')-9
		e2 = ord(seq[3:4])-ord('a')-9

		list1 = self.getSeqAsList()
		list2 = [s2,a2,v2,e2]
		diff = 0

		for i in range(len(list1)):
			diff += abs(list1[i] - list2[i])

		# Normalize the average from (0-18) to (0-100)
		diff = ((diff/4.0)*50)/9.0
		return diff