#-*- coding: utf-8 -*-

from framework import Manager
from products import MessageBox, UnderlinePen

def main():
	manager = Manager()

	u = UnderlinePen('~')

	m = MessageBox('*')

	manager.register("Underline", u)
	manager.register("MessageBox", m)

	p1 = manager.create("Underline")
	p1.use("Hello, world")

	p2 = manager.create("MessageBox")
	p2.use("Hello, world")

if __name__ == '__main__':
	main()
