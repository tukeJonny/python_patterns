#-*- coding: utf-8 -*-
import copy

from framework import Prototype 

class MessageBox(Prototype):
	def __init__(self, decochar='*'):
		self.decochar = decochar

	def use(self, s):
		print(self.decochar * (len(s)+4))
		print("{decochar} {0} {decochar}"\
				.format(s, decochar=self.decochar))
		print(self.decochar * (len(s)+4))
	
	def create_clone(self):
		p = copy.deepcopy(self)
		return p

class UnderlinePen(Prototype):
	def __init__(self, ulchar='*'):
		self.ulchar = ulchar
	
	def use(self, s):
		print(s)
		print(self.ulchar * len(s))
	
	def create_clone(self):
		p = copy.deepcopy(self)
		return p
