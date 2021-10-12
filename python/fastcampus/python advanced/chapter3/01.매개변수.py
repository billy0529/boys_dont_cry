# 매개변수 1 실습

# 위치 매개변수 (기본)
def test(x,y):
    print(x)
    print(y)
test(1,2)


# 기본 매개변수
def test(x, y = 100):
    print(x)
    print(y)
test(20)


# 키워드 매개변수
def test(x,y):
    print(x)
    print(y)
test(y = 50, x = 100)
