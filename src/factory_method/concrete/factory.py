#-*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from framework.factory import Factory
from concrete.user import (
	UsualUser,
	FuckinUser,
)

class FactoryTemplate(metaclass=ABCMeta):
	def __init__(self):
		self._registered = []
	
	@abstractmethod
	def _create_product(self, name):
		pass

	@abstractmethod
	def _register_product(self, user):
		pass

class UsualUserFactory(Factory, FactoryTemplate):
	def __init__(self):
		super().__init__()
	
	def _create_product(self, name):
		return UsualUser(name)
	
	def _register_product(self, usual_user):
		self._registered.append(usual_user.name)

class FuckinUserFactory(Factory, FactoryTemplate):
	def __init__(self):
		super().__init__()
	
	def _create_product(self, name):
		return FuckinUser(name)

	def _register_product(self, fuckin_user):
		self._registered.append(fuckin_user.name)

