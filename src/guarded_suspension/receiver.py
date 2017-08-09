#-*- coding: utf-8 -*-
from threading import Thread

class Receiver(Thread):
	
	def __init__(self, queue):
		super().__init__()
		self.daemon = True
		self.queue = queue

	def run(self):
		while True:
			num = self.queue.get()
			print("[<==] received {0}".format(num))
