#-*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from framework.product import Product

class UserTemplate(metaclass=ABCMeta):
	def __init__(self, name):
		self.name = name
	
	@abstractmethod
	def do_action(self):
		pass

class UsualUser(Product, UserTemplate):
	"""
	普通のユーザ
	"""

	def __init__(self, name):
		super().__init__(name)
	
	def do_action(self):
		print("こんにちは。{0}と言います".format(
			self.name))

class FuckinUser(Product, UserTemplate):
	"""
	***なユーザ
	"""

	def __init__(self, name):
		super().__init__(name)
	
	def do_action(self):
		print("{0}。名前だよ名前！！".format(
			self.name))


