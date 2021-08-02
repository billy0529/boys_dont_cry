# lambda
import random

sum = lambda x:x + 1
print(sum(1)) # 2

def sumnum(y):
    return lambda x:x + y
g = sumnum(2)
print(g(14)) # 16

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(sum, lst))) # [2, 3, 4, 5, 6]

lst2 = [10, 20, 30, 40, 50]
print(list(map(lambda x, y:x + y, lst, lst2)))
# [11, 22, 33, 44, 55]

print((lambda x:x + 1)(10)) # 11

f = lambda x, y: x + y
print(f(50,60)) # 110

lst3 = [x ** 2 for x in range(100) if x % 2 == 0]
print(list(filter(lambda x:x * 2 <= 50, lst3)))
# [0, 4, 16]
# 0 ~ 99의 숫자중 짝수의 제곱근에 2를 곱한수가 50보다 작은수는?



