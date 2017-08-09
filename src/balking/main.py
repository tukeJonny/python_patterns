#-*- coding: utf-8 -*-
import data, threads

def main():
	dataObj = data.Data("test.txt", "<FIRST CONTENT>")

	saver = threads.Saver(dataObj)
	updater = threads.Updater(dataObj)

	saver.start()
	updater.start()


if __name__ == "__main__":
	main()
