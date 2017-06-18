#-*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Product(metaclass=ABCMeta):
	@abstractmethod
	def do_action(self):
		pass

