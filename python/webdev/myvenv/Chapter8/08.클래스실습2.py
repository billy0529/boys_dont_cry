## 클래스 실습 2

class HouseHan:
    lastname = "HAN"
    def __init__(self,name):
        self.name = name
        self.fullname = self.lastname + name
    def travel(self,location):
        self.location = location
        print("{0} will travel to {1}".format(self.name, location))


billy = HouseHan("SEJIN")
print(billy.fullname)
print(billy.travel("BUSAN"))