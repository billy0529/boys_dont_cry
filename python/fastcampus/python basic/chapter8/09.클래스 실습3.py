# 클래스 실습 1
import random


class Item:

    def __init__(self, name, price, weight):
        self.name = str(name)
        self.price = int(price)
        self.weight = float(weight)
    
    def sale(self):
        print("[{}]를 판매합니다. 가격은 [{}] 입니다.".format(self.name, self.price))
    
    def discard(self):
        while True:
            isdropable = input("[{}]는 버릴수 있는 아이템입니까? (Y/y): ".format(self.name))
            if isdropable == "Y" or isdropable == "y":
                print("[{}]를 버렸습니다.".format(self.name))
                break
            elif isdropable == "N" or isdropable == "n":
                print("[{}]를 버릴수 없습니다.".format(self.name))
                break
    

class Armor(Item):

    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)
        self.effects = ("방어력 상승", "공격력 상승", "공속증가")
    
    def effect(self):
        print("[{}]의 착용효과는 [{}]입니다.".format(self.name, self.effects[random.randint(0,2)]))
    
    def ware(self):
        print("[{}]를 착용하였습니다.".format(self.name))


class Disposible(Item):

    def __init__(self, name, price, weight):
        super().__init__(name, price, weight)
        self.effects = ("15초간 무적", "텔레포트", "회피율 증가")

    def effect(self):
        print("[{}]의 사용효과는 [{}]입니다.".format(self.name, self.effects[random.randint(0,2)]))
    
    def use(self):
        print("[{}]를 사용하였습니다.".format(self.name))


mithril_armor = Armor("미스릴아머", 100000, 100)
mithril_armor.effect()
mithril_armor.discard()
potion = Disposible("포션", 100, 1)
potion.effect()
potion.use()
potion.sale()