## 클래스를 사용하는 이유

champion1_name = "izureal"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion2_name = "Lisin"
champion2_health = 800
champion2_attack = 95

print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion3_name = "Yasuo"
champion3_health = 750
champion3_attack = 92

print(f"{champion3_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name,attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)
basic_attack(champion3_name, champion3_attack)

print("======= 클래스를 사용하는 경우 ==========")

class Monster:
    def say(self):
        print("나는 몬스터다!")
a = Monster()   # 인스턴스 = 클래스이름()
a.say()    # 인스턴스.메소드()
