#-*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Factory(metaclass=ABCMeta):
	@abstractmethod
	def _create_product(self, name):
		pass

	@abstractmethod
	def _register_product(self, product):
		pass

	def create(self, name):
		self.__p = self._create_product(name)
		self._register_product(self.__p)
		return self.__p
