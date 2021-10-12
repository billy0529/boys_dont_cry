# 클래스와 객체

class pass_class:
    pass

# 클라스 안: self.속성명
# 클래스 밖: 객체명.속성명

class Unit:
    
    count = 0

    def __init__(self,name,hp,shield,damage):
        self.name = name # 인스턴스 속성
        self.hp = hp
        self.__shield = shield  # 클래스밖에서 사용할수없는 속성
        self.damage = damage
        print(f"[{self.name}] 이/가 생성되었습니다.")
        Unit.count += 1
        print("현재 총 {}개의 유닛이 생성되었습니다.".format(Unit.count))

    def __str__(self):
        return f"[{self.name}] 체력: {self.hp} 실드: {self.__shield} 공격력: {self.damage}"
        
    def battle(self):
        print("전투력: {}".format(self.hp+self.__shield+self.damage))
    

probe = Unit("프로브",20,20,5)
zealot = Unit("질랏",100,60,15)
dragoon = Unit("드라군",100,80,20)

# 스트링 메소드를 불러옴
print(probe) # 위와 동일
zealot.battle()
# print(probe.shield) # 숨겨진 속성을 출력하려해서 오류발생
probe.__shield = 100
probe._Unit__shield = 200 # 숨겨진 속성을 강제로 불러와서 인자 입력
print(probe) # shield 값이 200으로 바뀜
