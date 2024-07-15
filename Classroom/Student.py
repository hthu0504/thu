from Classroom.BasicInfo import Base

class Student(Base):
	def __init__ (self, name, lop, birth):
		super().__init__(name, birth, lop)
		self.name = name
		self.lop = lop
		self.birth = birth
		self.details = {}
	def getInfo(self):
		print(self.name)
		print(self.birth)
		print(self.lop)

