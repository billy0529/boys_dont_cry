## 오버라이드, 클래스 변수

## 클래스 변수
## : 인스턴스들이 모두 공유하는 변수

import random
class Monster:
    max_num = 1000     ## 클래스 변수 모든 자식에게 상속
    def __init__(self,name,health,attack):   ## 상속할 속성
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1    ## 몬스터생성시 1씩 감소

    def move(self):                          ## 몬스터의 메소드
        print(f"[{self.name}] 지상에서 이동하기")

class Wolf(Monster):
    pass                     ## 부모클래스를 그대로 상속

class Shark(Monster):
    def move(self):          ## 메소드 오버라이드 : shark로 재정의
        print(f"[{self.name}] 헤엄치기")

class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self,name,health,attack):
        super().__init__(name,health,attack)  ## 부모의 init 속성을 가져옴
        self.skills = ("불뿜기","꼬리치기","날개치기")

    def move(self):          ## 메소드 오버라이드 : dragon으로 재정의
        print(f"[{self.name}] 날기")

    def skill(self):
        print(f"[{self.name}] 스킬 사용 {self.skills[random.randint(0,2)]}") # 스킬 무작위 사용

wolf = Wolf("세진",400,500)
wolf.move()
print(wolf.max_num)

shark = Shark("샤크",3000,400)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤",8000,800)
dragon.skill()
print(dragon.max_num)


