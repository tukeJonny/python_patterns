#-*- coding: utf-8 -*-
import time
import threading

class ImmutablePost(object):
	"""
	Immutableな投稿クラス
	"""
	def __init__(self, title, description):
		self.__title = title
		self.__description = description

	@property
	def title(self):
		return self.__title

	@property
	def description(self):
		return self.__description

	def __str__(self):
		return "<Post: title={0}, description={1}>"\
				.format(self.__title, self.__description)

class PrintPostThread(object):
	"""
	投稿を表示するクラス
	"""
	def __init__(self, post):
		self.post = post

	def __call__(self):
		while True:
			try:
				print("[{0}] prints {1}"\
						.format(
							threading.current_thread().ident,
							self.post
				))
				time.sleep(0.1)
			except KeyboardInterrupt as e:
				pass

def main():
	p = ImmutablePost("test title", "blah blah blah")
	printer = PrintPostThread(p)
	threads = []
	for _ in range(5):
		th = threading.Thread(target=printer)
		th.start()
		threads.append(th)
	
	for th in threads:
		th.join()

if __name__ == "__main__":
	main()
