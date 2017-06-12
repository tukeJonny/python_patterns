#-*- coding: utf-8 -*-

class Printer(object):
	"""
	デバッグメッセージを生成するクラスのバージョン１.
	十分にテストされており、動作が保障されている
	"""
	
	@staticmethod
	def success(msg):
		return("[+] {0}".format(msg))
	
	@staticmethod
	def fail(msg):
		return("[-] {0}".format(msg))
