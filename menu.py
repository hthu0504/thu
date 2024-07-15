from Classroom.Student import Student

from manage import manage

def main():
    while True:
        print("\nMenu:")
        print("1. Thêm học sinh")
        print("2. Xóa học sinh")
        print("3. Sửa thông tin học sinh")
        print("4. Thêm giáo viên")
        print("5. Xóa giáo viên")
        print("6. Sửa thông tin giáo viên")
        print("7. Thêm lớp học")
        print("8. Xóa lớp học")
        print("9. Thoát")
        
        choice = input("Chọn tùy chọn: ")
        
        hi = manage()
        if choice == '1':
            name = input("Nhập tên học sinh: ")
            lop = input("Nhập lớp: ")
            birth = input("Nhập năm sinh: ")
            hi.AddStudent(name, lop, birth)
        
        elif choice == '2':
            name = input("Nhập tên học sinh: ")
            lop = input("Nhập lớp: ")
            birth = input('Năm sinh: ')
            hi.RemoveStudent(name, birth, lop)

        elif choice == '3':
            name = input('Nhập tên học sinh: ')
            birth = input('Nhập năm sinh: ')
            index = hi.Check(hi.student, name, birth)
            if index == -1:
                print('Không có học sinh này trong lớp')
            else:
                while True:
                    key = input('Nhập thông tin cần cập nhật (hoặc nhập "done" để kết thúc): ')
                    if key == 'done':
                        break
                    elif key == 'lớp':
                        new_value = input('Nhập lớp cần cập nhật: ')
                        hi.student[index].lop = new_value
                    elif key == 'năm sinh':
                        new_value = input('Nhập năm sinh cần cập nhật: ')
                        hi.student[index].birth = new_value
                    else:
                        new_value = input(f'Nhập giá trị mới cho {key}: ')
                        hi.student[index].details[key] = new_value
                    print('Thông tin học sinh đã được cập nhật')

        
        elif choice == '4':
            name = input("Nhập tên giáo viên: ")
            subj = input("Nhập môn học: ")
            lop = input("Nhập lớp: ")
            birth = input("Nhập năm sinh: ")
            hi.AddTeacher(name, subj, lop, birth)

        elif choice == '5':
            name = input("Nhập tên giáo viên: ")
            birth = input("Nhập năm sinh: ")
            lop = input('Xóa khỏi lớp: ')
            hi.RemoveTeacher(name, birth, lop)

        elif choice == '6':
            name = input('Nhập tên giáo viên: ')
            birth = input('Nhập năm sinh: ')
            index = hi.Check(hi.teacher, name, birth)
            if index == -1:
                print('Không có giáo viên này trong lớp')
            else:
                while True:
                    key = input('Nhập thông tin cần cập nhật (hoặc nhập "done" để kết thúc): ')
                    if key == 'done':
                        break
                    elif key == 'lớp':
                        new_value = input('Nhập lớp cần cập nhật: ')
                        hi.teacher[index].lop = new_value
                    elif key == 'năm sinh':
                        new_value = input('Nhập năm sinh cần cập nhật: ')
                        hi.teacher[index].birth = new_value
                    else:
                        new_value = input(f'Nhập giá trị mới cho {key}: ')
                        hi.teacher[index].details[key] = new_value
                    print('Thông tin giáo viên đã được cập nhật')

        elif choice == '7':
            name = input('Nhập tên lớp: ')
            khoa = input('Nhập khóa: ')
            hi.AddClass(name, khoa)

        elif choice == '8':
            name = input('Xóa lớp: ')
            khoa = input('Nhập khóa: ')
            hi.RemoveClass(name, khoa)
        
        elif choice == '9':
            print("Thoát chương trình")
            break
        
        else:   
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

if __name__ == "__main__":
    main()


