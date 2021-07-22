## 생성자 (__init__)함수
## self 란
## 속성 추가하기
## 메소드 추가하기


class Monster:
    def __init__(self,health,attack,speed):  ##__init__ 가장 먼저 호출되는 메소드
        ## self는 매개변수가 아니며 최초로 무조건 들어가는 것
        ## self는 매개변수 자기자신 (아래의 goblin과 wolf)
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self,num):
        self.health -= num
    def get_health(self):
        return self.health
    
    

goblin = Monster(800,120,300)
wolf = Monster(1500,200,350)
goblin.decrease_health(100)
print(goblin.get_health())
print(goblin.attack)
