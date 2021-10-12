# 1. 맵 함수
# 사용이유 
# 기존 리스트를 수정해서 새로운 리스트를 만들때

# 사용방법
# map(함수, 순서가 있는 자료형)

# 10 곱하기
lst = 1,2,3,4,5
list_10times = list(map(lambda x: x * 10, lst))
print(list_10times) # [10,20,30,40,50]

# 공백제거
items = '   billy    ', '    sejin    ', '    41    ', '    male    '
items_nostrip = list(map(lambda x:x.strip(),items))
print(items_nostrip)

# 딕셔너리 활용
# 키값 계산
numberkey = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
numberkeys = list(map(lambda x:x*2,numberkey))
print(numberkeys) # 'oneone', 'twotwo', 'threethree', 'fourfour', 'fivefive'

# 밸류값 계산
numberkey = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
numberkeys = list(map(lambda x:x*10,[numberkey[i] for i in numberkey]))
# 리스트 내포 사용 [연산 for 인자 in 반복가능객체]
# number[i]는 밸류값 호출
print(numberkeys) # 10,20,30,40,50

# 2. Filter 함수
# 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때 
numberket_filter = list(filter(lambda x: x % 2 == 0, [numberkey[i] for i in numberkey]))
print(numberket_filter) # 2, 4