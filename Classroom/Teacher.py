from Classroom.BasicInfo import Base

class Teacher(Base):
	def __init__ (self, name, subj, birth, lop):
		super(). __init__ (name, birth, lop)
		self.name = name
		self. birth = birth
		self.subj = subj
		self.lop = lop
		self.lop = []
		self.details = {}
	def getInfo(self):
		print(self.name)
		print(self.birth)
		print(self.subj)
		print(self.lop)	