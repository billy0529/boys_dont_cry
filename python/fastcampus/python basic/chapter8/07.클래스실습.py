## 사칙연산 클래스

import sys
class Calculator:
    def setdata(self,first,second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second

    def mul(self):
        return self.first + self.second
  
    def div(self):
        return self.first // self.second

    def sub(self):
        return self.first - self.second
    
billy = Calculator()
billy.setdata(12,4)
print(billy.sum())
print(billy.div())
print(billy.sub())
print(billy.mul())



