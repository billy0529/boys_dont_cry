## 상속
## : 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용

# 부모 클래스
class Monster:
    def __init__(self,name,health,attack):   ## 상속할 속성
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):                          ## 몬스터의 메소드
        print(f"[{self.name}] 지상에서 이동하기")

# 자식 클래스
class Wolf(Monster):
    pass                     ## 부모클래스를 그대로 상속

class Shark(Monster):
    def move(self):          ## 메소드 오버라이드 : shark로 재정의
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    def move(self):          ## 메소드 오버라이드 : dragon으로 재정의
        print(f"[{self.name}] 날기")

wolf = Wolf("세진",400,500)
wolf.move()
shark = Shark("샤크",3000,400)
shark.move()
dragon = Dragon("드래곤",8000,800)
dragon.move()


