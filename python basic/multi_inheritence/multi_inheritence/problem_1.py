class Teacher:
    def T_A(this):
        print("I can teach")
class Student:
    def S_A(this):
        print("I can learn")
class Youtubers:
    def Y_A(this):
        print("I can teach and learn")
class Human(Teacher,Student,Youtubers):
    pass
q=Human()
q.T_A()
q.S_A()
q.Y_A()





