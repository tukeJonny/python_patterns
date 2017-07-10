#-*- coding: utf-8 -*-
import threading

class Gate(object):

	def __init__(self):
		self.counter = 0
		self.name = None
		self.address = None

		self.lock = threading.Lock()
	
	def check(self):
		if not self.name[0] in self.address[0]:
			raise ValueError("***** Broken *****")
	
	def through(self, name, address):
		with self.lock:
			self.counter += 1
			self.name = name
			self.address = address
			self.check()
	
	def __str__(self):
		return "[{0}] ({1},{2})"\
				.format(self.counter,self.name,self.address)


class UserThread(object):

	def __init__(self, gate, name, address):
		self.gate = gate
		self.name = name
		self.address = address
	
	def run(self):
		print("[*] Begin {0}".format(self.name))
		while True:
			print(gate)
			self.gate.through(self.name,self.address)

if __name__ == "__main__":
	gate = Gate()
	users = [
		("alice", "alice@example.com",),
		("bobby", "bobby@example.com",),
		("chris", "chris@example.com",)
	]
	threads = []
	for name, address in users:
		user = UserThread(gate, name, address)
		th = threading.Thread(target=user.run)
		threads.append(th)
		th.start()
	
	for thread in threads:
		thread.join()

