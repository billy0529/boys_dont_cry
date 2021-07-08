# # 클래스
# 1. 메소드
# 2. 프로퍼티
# 3. 클래스 변수
# 4. 인스턴스 변수
# 5. 초기자
# 6. 소멸자# 

# 메소드
#     (1) 인스턴스 메소드
#     (2) 클래스 메소드
#     (3) 정적 메소드
class Rectangle:
    count = 0 # 클래스 변수, 해당 클래스를 사용하는 모두에게 공유
              # 클래스명.변수명으로 액세스 가능
              
    # 초기자 (initializer)
    # 파이썬에서 두개의 밑줄 (__) 시작하고 두개의 밑줄로 끝나는 레이블은 보통 특별한 의미를 갖는다). 
    def __init__(self,width,height): # __ 언더바 두개는 메소드를 private으로 만든다.
        # self. : 인스턴스변수는 각 객체인스턴스별로 별도로 존재함. self.변수명으로 사용
        self.width = width   # 객체내에서 계속 사용할수 있도록 변수 입력
        self.__area = width * height      # private 변수 __area
        self.height = height
        Rectangle.count += 1  ## 클래스명.변수명으로 엑세스 가능
    # 메소드
    def calcArea(self):
        area = self.width * self.height
        return area
    # private 메서드
    def __internalRun(self):
        pass
    #  정적 메서드
    #  self 파라미터가 없으며 인스턴스 변수에 엑세스 할수 없다. 
    #  일반적으로 인스턴스 데이타를 엑세스 할 필요가 없는 경우 클래스 메서드나 정적 메서드를 사용하는데, 
    #  이때 보통 클래스 변수를 엑세스할 필요가 있을 때는 클래스 메서드를, 
    #  이를 엑세스할 필요가 없을 때는 정적 메서드를 사용한다.
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight   
    # 클래스 메서
    # 정적 메소드와 동일하지만 self대신 cls 파라미터를 사용한다. cls로 클래스 변수에 접근한다.
    @classmethod 
    def printCount(cls):
        print(cls.count) 
    ## __add__ 는 스페셜 메소드. __add__외에도 종류가 상당히 많다.
    def __add__(self,other):
        obj = Rectangle(self.width + other.width, self.height + other.height)
        return obj

# 인스턴스 생성
r = Rectangle(2, 3)
 
# 메서드 호출
area = r.calcArea()
print("area = ", area)
 
# 인스턴스 변수 엑세스
r.width = 10    ## 인스턴스 변수(초기자변수) width를 10으로 변경
print("width = ", r.width)
 
# 클래스 변수 엑세스
# 둘다 클래스 변수를 가져오지만, r이라는 객체에서 불러오는것은 비추천
print(Rectangle.count)
print(r.count)     

# 상속
class Animal:
    def __init__(self, name):
        self.name = name
    def move(self):
        print("move")
    def speak(self):
        pass
 
class Dog (Animal):
    def speak(self):
        print("bark")
 
class Duck (Animal):
    def speak(self):
        print("quack")

dog = Dog("doggy") # 부모클래스의 생성자
n = dog.name # 부모클래스의 인스턴스변수
dog.move()   # 부모클래스의 메서드
dog.speak()  # 파생클래스의 멤버