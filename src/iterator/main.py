#-*- coding: utf-8 -*-

class Member(object):
	def __init__(self, name, height, weight, age):
		self._name = name
		self._height = height
		self._weight = weight
		self._age = age
	
	@property
	def bmi(self):
		meter_height = self._height / 100
		return self._weight / (meter_height**2)

	def introduce(self):
		print("[*] My name is {0}! I am {1} years old. Nice to meet you!"\
				.format(self._name, self._age))

class MemberIterator(object):
	def __init__(self):
		self._member_list = []
	
	def append(self, member):
		self._member_list.append(member)
	
	def __getitem__(self, index):
		if 0 <= index < len(self._member_list):
			return self._member_list[index]
		raise IndexError

def prepare(member_iterator, n):
	for idx in range(n):
		name = "user{0}".format(idx)
		height = 175+idx
		weight = 76+idx
		age = 20+idx
		member_iterator.append(\
				Member(name, height, weight, age))
	return

if __name__ == "__main__":
	member_iterator = MemberIterator()
	prepare(member_iterator, 20)
	for member in iter(member_iterator):
		member.introduce()
		if member.bmi >= 25:
			print("Hmm... too fat.")
		


