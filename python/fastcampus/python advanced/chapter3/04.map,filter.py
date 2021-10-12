# map. filter 함수
# list, tuple, dictionary 형태로 감싸야 함

# map 예시
# 앞 공백 삭제
items = [' billy', ' sejin', ' 41', ' male']
items_nostrip = list(map(lambda x:x.lstrip(), items))
print(items_nostrip)

# filter 예시
# 조건을 만족하는 True값만 확인
items = [5,4,3,2,1,0,-1,-2,-3,-4,-5]
items_nostrip = list(filter(lambda x: x >= 3, items))
print(items_nostrip)

