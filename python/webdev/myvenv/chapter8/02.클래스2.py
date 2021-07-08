class Monster:
    def say(self):
        print("나는 몬스터다!")

goblin = Monster()
goblin.say()

# 파이썬은 자료형도 클래스다.
a = 10
b = "문자열객체"
c = True

print(type(a)) # <class 'int'>
print(type(b)) # <class 'str'> 
print(type(c)) # <class 'bool'>

print(b.__dir__())  # 문자열 b에 대한 메소드 확인
