class DSstudent:
    def __init__(self, stu_id, name):
        self.stu_id=stu_id
        self.name=name
    
    def show_info(self):
        print(f"학번: {self.stu_id}, 이름: {self.name}")
    
student = DSstudent(20251236, "강다은")
student.show_info()