#-*- coding: utf-8 -*-
import time
import threading

from Cake import get_cake

class Eater(object):
	def __init__(self, cake):
		self.__cake = cake

	def eat(self):
		while True:
			tid = threading.get_ident()
			print("[{0}]".format(tid))

			try:
				num = self.__cake.get()
			except:
				print("	|_ Hmm... There is no more cake of pieces...")
				break

			print("	|_Look at cake ({0})".format(self.__cake))
			if num > 500:
				print("	|_Eat a piece of cake! yummy!!")
			else:
				print("	|_Eat a piece of cake...this piece is so bad taste...")
			time.sleep(1)

def main():
	threads = []
	for _ in range(3):
		eater = Eater(get_cake())
		th = threading.Thread(target=eater.eat)
		threads.append(th)
		th.start()
	
	for thread in threads:
		thread.join()

if __name__ == '__main__':
	main()
