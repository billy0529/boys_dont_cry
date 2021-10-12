# 람다함수
test = lambda x: x - 10
print(test(50))

# if문
test2 = lambda a: True if a > 0 else False
print(test2(-2))

# 함수 호출 방법
# 1. 함수 자체 호출
print((lambda a : a - 1)(10))
# 2. 변수에 담아서 호출
calc = lambda a : a - 1
print(calc(50))

# test 
# x값이 1일 경우 y 출력, x가 1이 아닐경우 y-1 출력
test = lambda x,y: print(y) if x == 1 else print(y-1)
test(2,10)
(lambda x,y: print(y) if x == 1 else print(y-1))(1,10)
