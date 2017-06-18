#-*- coding: utf-8 -*-
import random

def get_cake(refresh=False):
	class Cake(object):
		def __init__(self, number):
			self.__lock = False
			self.__pieces = number
	
		def get(self):
			if not self.__pieces > 0:
				raise Exception()
			self.__pieces -= 1
			return random.randint(1, 1000)

		def __str__(self):
			return "<Cake({0}): remain {1} pieces>".format(
				id(self),
				self.__pieces
			)

	if refresh:
		get_cake.cake = None
	
	if get_cake.cake:
		assert get_cake.cake is not None
		return get_cake.cake

	randnum = random.randint(1, 10)
	print("[+] Get Cake ({0} pieces)".format(randnum))
	get_cake.cake = Cake(randnum)

	assert get_cake.cake is not None
	return get_cake.cake
get_cake.cake = None
