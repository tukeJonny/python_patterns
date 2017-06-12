#-*- coding: utf-8 -*-
import abc
import Qtrac
import datetime

import debugmsg

@Qtrac.has_methods("success_log", "fail_log")
class Logger(metaclass=abc.ABCMeta): pass

class Logger_v2(object):
	"""
	日付をつけてみた. version2
	"""
	printer = debugmsg.Printer()

	@staticmethod
	def success_log(msg):
		now = datetime.datetime.now()
		msg = Logger_v2.printer.success(msg)
		print("{0} - {1}".format(now, msg))
	
	@staticmethod
	def fail_log(msg):
		now = datetime.datetime.now()
		msg = Logger_v2.printer.fail(msg)
		print("{0} - {1}".format(now, msg))
