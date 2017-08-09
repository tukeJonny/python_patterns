#-*- coding: utf-8 -*-
import time

import queue
import sender, receiver

def main():
	q = queue.Queue()
	s = sender.Sender(q)
	r = receiver.Receiver(q)

	s.start()
	r.start()

	while True:
		time.sleep(1)

if __name__ == "__main__":
	main()
