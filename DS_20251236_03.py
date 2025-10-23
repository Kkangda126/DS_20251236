class Student:
    def __init__(self, stu_id, name):
        self.stu_id = stu_id
        self.name = name
    
    def show_info(self):
        print(f"학번: {self.stu_id}, 이름: {self.name}")

class UndergraduateStudent(Student):
    def __init__(self, name, major):
        super().__init__(name)
        self.name = name
        self.major = major
    
    def introduce(self):
        print(f"저는 학부생 {self.name}입니다. 전공은 {self.major}입니다.")


stu1 = UndergraduateStudent("202501", "김민수", "컴퓨터공학과")

stu1.showinfo()
stu1.introduce()