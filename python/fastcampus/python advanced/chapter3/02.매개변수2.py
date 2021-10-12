# 위치 가변 매개변수
# 키워드 가변 매개변수
# 가변 매개변수 - 개수가 정해지지 않은 매개변수
# 매개변수 앞에 *가 붙는다 (튜플형)

# 위치 가변 매개변수
def test(*args):
    print(type(args)) # 튜플
    for i in args:
        print(i)
test(10,20,30,40,50)

# 키워드 가변 매개변수 (딕셔너리형)
def test(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')
test(name="billy",age=41, sex="male", btype = "A")

# 매개 변수 작성순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

