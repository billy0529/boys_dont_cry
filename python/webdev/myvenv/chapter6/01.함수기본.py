## 함수
## 함수는 가독성향상, 쉬운 반복작업, 편한 유지보수
# 함수 예제
# 아래에서 함수를 사용하지 않으면 print문 2줄을 사용자별로 따로 작성해야함
def printMessage(name,date):
    print("안녕하세요. ", name, "님")
    print("현재 프리미엄 서비스 사용기간이 ", date, "일 남았습니다.")
printMessage("한세진",41)

# 기본 함수
def printhello():
    print("Hello")
printhello()

# 매개변수가 있는 함수
def sum(a,b):
    print(a+b)
sum(1,2)

# 반환값이 있는 함수, 반환값이란 함수 바깥으로 값을 빼주는것
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number
print(getRandomNumber())

# 매개변수와 반환값이 있는 함수
def numbers(x,y):
    z = x * y
    return z
print(numbers(7,3))

