#-*- coding: utf-8 -*-
import threading

class Data(object):

	def __init__(self, fname, content):
		self._lock = threading.Lock()
		self._fname = fname
		self._content = content
		self._changed = True
	
	def update(self, new_content):
		with self._lock:
			print("[{0}] Change Data content!"\
					.format(threading.current_thread().ident))
			content = new_content
			self._changed = True
			print("[!] changed = {0}".format(self._changed))
			print("[{0}] Exiting..."\
					.format(threading.current_thread().ident))

	def save(self):
		with self._lock:
			if not self._changed:
				print("[{0}] Data content hasn't updated."\
						.format(threading.current_thread().ident))
				return # balking!
			
			print("[{0}] Update Data content..."\
					.format(threading.current_thread().ident))
			# Save
			with open(self._fname, "w") as f:
				f.write(self._content)
				self._changed = False
				print("[!] changed = {0}".format(self._changed))
			print("[{0}] Update Completed!"\
					.format(threading.current_thread().ident))
			print("[{0}] Exiting..."\
					.format(threading.current_thread().ident))
