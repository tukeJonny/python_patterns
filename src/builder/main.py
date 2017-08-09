#-*- coding: utf-8 -*-
import abc
import requests
from bs4 import BeautifulSoup

class Builder(metaclass=abc.ABCMeta):
	"""
	ビルダーの抽象基底クラス
	"""
	@abc.abstractmethod
	def fetch(self, url):
		"""
		:url: 対象URL
		:return: 対象URLから取得してきたhtmlのstr
		"""
		pass

	@abc.abstractmethod
	def scrape(self, html):
		"""
		:html: fetch()によって取得したhtml
		:return: HTMLのスクレイピング結果(Json)
		"""
		pass

	@abc.abstractmethod
	def stringify(self, dObj):
		"""
		scrape()から得た結果を文字列化する
		:dObj: 辞書オブジェクト
		:return: 辞書オブジェクトを文字列化したもの
		"""
		pass

class Director(object):
	"""
	Builderの使い方を把握していて、結果を返す
	"""
	def __init__(self, builder):
		self.__builder = builder

	def construct(self, url):
		html = self.__builder.fetch(url)
		result = self.__builder.scrape(html)
		text = self.__builder.stringify(result)
		print(text)

class WikipediaBuilder(object):
	def fetch(self, url):
		resp = requests.get(url)
		html = resp.content.decode()
		from IPython import embed; embed()
		return html

	def scrape(self, html):
		bsObj = BeautifulSoup(html)
		table = bsObj.find('table', {'class': 'infobox vevent'})
		from IPython import embed; embed()
	
	def stringify(self, dObj):
		s = "="*20
		for key, value in dObj.items():
			s += "{0}: {1}\n".format(key,value)
		s = "="*20
		return s

if __name__ == '__main__':
	url = 'https://ja.wikipedia.org/wiki/Python'

	wbuilder = WikipediaBuilder()
	director = Director(wbuilder)

	director.construct(url)
