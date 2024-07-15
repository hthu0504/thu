from Classroom.Class import Class
from Classroom.Student import Student
from Classroom.Teacher import Teacher

class manage:
    teacher = []
    student = []
    lop = []

    def Check(self, lst, namea, birtha):
        for i in range(len(lst)):
            if lst[i].name == namea and lst[i].birth == birtha:
                return i 
        return -1  # không tồn tại tên đó trong lớp 

    def CheckClass(self, lst, namea, khoae):
        for opn in range(len(lst)):
            if lst[opn].name == namea and lst[opn].khoa == khoae:
                return opn
        return -1 

    def AddStudent(self, name, lop, birth):
        if self.Check(self.student, name, birth) == -1:
           self.student.append(Student(name, lop, birth))
        else:
            print("Đã tồn tại học sinh trong lớp")
            
    def RemoveStudent(self, name, birth, lop):
        index = self.Check(self.student, name, birth)
        if index != -1:  # tồn tại học sinh
            #self.student.pop(index)
            key = input('Bạn có chắc chắn không ?')
            if(key == 'có'):
                self.student.pop(index)
                print('Đã xóa ra khỏi lớp')
            if(key == 'không'):
                print("Hủy lựa chọn")
        else:
            print('Không có học sinh này trong lớp')

    def UpdatesInfoStudent(self, name, birth, lop, new_value, key):
        index = self.Check(self.student, name, birth)
        if index != -1:
            self.student[index].details[key] = new_value
        else:
            print("Không tìm thấy học sinh")

    def AddTeacher(self, name, subj, birth, lop):
        if self.Check(self.teacher, name, birth) == -1:
            self.teacher.append(Teacher(name, subj, birth, lop))
        else:
            print("Giáo viên đã tồn tại")

    def RemoveTeacher(self, name, birth, lop):
        index = self.Check(self.teacher, name, birth)
        if index != -1: 
            #self.student.pop(index)
            key = input('Bạn có chắc chắn không ?')
            if(key == 'có'):
                self.teacher.pop(index)
                print('Đã xóa ra khỏi lớp')
            if(key == 'không'):
                print("Hủy lựa chọn")
        else:
            print('Giáo viên này không có trong lớp')

    def UpdatesInfoTeacher(self, name, birth, lop, new_value, namea ):
        index = self.Check(self.teacher, name, birth)
        if index != -1:
            self.teacher[index].details[namea] = new_value
        else:
            print("Không tìm thấy giáo viên")
        
            
    def AddClass(self, name, khoa):
        if self.CheckClass(self.lop, name, khoa) == -1:
           self.lop.append(Class(name, khoa))
        else:
            print("Đã tồn tại lớp này")

    def RemoveClass(self, name, khoa):
        opn = self.CheckClass(self.lop, name, khoa)
        if opn != -1:  # tồn tại học sinh
            #self.student.pop(opn)
            key = input('Bạn có chắc chắn không ?')
            if(key == 'có'):
                self.lop.pop(opn)
                print('Đã xóa lớp học')
            if(key == 'không'):
                print("Hủy lựa chọn")
        else:
            print('Không tồn tại lớp này')