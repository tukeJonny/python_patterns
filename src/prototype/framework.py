#-*- coding: utf-8 -*-

import copy

class Prototype(object):

	def use(self):
		raise NotImplementedError

	def create_clone(self):
		return copy.deepcopy(self)


class Manager(object):
	def __init__(self):
		self.__showcase = dict()
	
	def register(self, name, proto):
		self.__showcase[name] = proto
	
	def create(self, name):
		return copy.deepcopy(self.__showcase[name])
