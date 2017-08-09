#-*- coding: utf-8 -*-
import time
import threading

class Saver(threading.Thread):
	"""
	自動保存機能
	"""
	def __init__(self, dataObj):
		super().__init__()
		self._dataObj = dataObj

	def run(self):
		while True:
			print("[*] Loop Saver...")
			self._dataObj.save()
			time.sleep(1000)

class Updater(threading.Thread):
	"""
	コンテンツを更新するスレッド
	"""
	def __init__(self, dataObj):
		super().__init__()
		self._dataObj = dataObj

	def run(self):
		idx=0
		while True:
			print("[*] Loop Updater...")
			self._dataObj.update("No.{0}".format(idx))
			time.sleep(1000)
			self._dataObj.save()

