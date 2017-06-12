#-*- coding: utf-8 -*-

import requests
import adapter

def get_google_page(logger):
	if not isinstance(logger, adapter.Logger):
		raise TypeError("Expected object of type Logger. got {0}"\
				.format(type(logger)))

	url = "https://google.co.jp/"
	res = requests.get(url)
	if res.status_code == 200:
		logger.success_log("HTTP SUCCESS")
	else:
		logger.fail_log("HTTP FAIL")

if __name__ == "__main__":
	logger = adapter.Logger_v2()
	get_google_page(logger)
