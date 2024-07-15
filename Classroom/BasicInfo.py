class Base:
	def __init__ (self, name, birth, lop):
		self.name = name
		self.birth = birth
		self.lop = lop
	def getInfo(self):
		print(self.name)
		print(self.birth)	