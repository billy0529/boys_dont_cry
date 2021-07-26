import random
import os

# 계산기

class FourCal:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def sum(self):
        z = self.x + self.y
        return z

    def div(self):
        z = self.x // self.y
        return z
    
    def sub(self):
        z = self.x - self.y
        return z
    
    def mul(self):
        z = self.x * self.y
        return z
    

class Square(FourCal):    ## 상속후에 square 메소드 추가

    def square(self):
        z = self.x ** self.y
        return z


class SafeFourCal(FourCal):   ## 상속후에 div 메소드에 대해 오버라이딩 (함수 편집)

    def div(self):
        if self.y == 0:
            return 0          ## 0으로 나눠도 오류를 뿜지 않음
        else:
            return self.x // self.y


a = FourCal(60,30)
b = FourCal(100,50)
c = Square(20,20)
d = SafeFourCal(40,0)
print(a.sum())
print(b.sum())

print(a.mul())
print(b.mul())

print(a.div())
print(b.sub())
print(c.sum())

print(c.square())
print(d.div())




