## class 실습2
class HundredSumCal:
  
    hundred = 200              ## 부모클래스의 클래스 변수는 상속된지만 상속 클래서에서 명시할경우
    thousand = 1000            ## 상속 클래스의 클래스변수를 따름

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def sum(self):
        z = (self.x + self.y) * self.hundred
        return z


class Another(HundredSumCal):   
 
    hundred = 100                 
    ## 클래스 변수는 클래스 별로 따로 할당된다 (상속도 마찬가지)

    def mul(self):
        z = self.x * self.y * self.hundred + self.thousand  
        # thousand는 부모에서 가져오고 hundred는 자식 클래스의 클래수 변수 사용
        return z

a = HundredSumCal(4,2)
b = Another(10,10)
print(a.sum()) # 1200
print(b.mul()) # 11000

