#-*- coding: utf-8 -*-
import time
import random
from threading import Thread

class Sender(Thread):
	
	def __init__(self, queue):
		super().__init__()
		self.daemon = True
		self.queue = queue

	def run(self):
		while True:
			num = random.randint(0,256)
			self.queue.put("Hello {0}".format(num))
			print("[==>] send {0}".format(num))
			time.sleep(1)
