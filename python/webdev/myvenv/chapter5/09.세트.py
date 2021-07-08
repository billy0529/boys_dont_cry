## 세트


## 중복 적용안됨, 순서 없음

myset = {1,1,3,3,5,5,7,7,9,9}
print(myset) #{1,3,5,7,9}

# 리스트변환
mylist = [1,10,100,1,10,100,1000]
myset2 = set(mylist)
print(myset2) # {1000,1,10,100}

#추가 삭제
myset2.add(500)
print(myset2) # {1000,1,10,100,500}
myset2.update({600,700,700,800,800,900})   # 여러개는 update 사용
print(myset2) # {1000,1,10,100,500,600,700,800,900}
myset2.remove(600)  # 600만 삭제
myset2.clear()  # 전부 삭제

# 집합 연산
a = {1,3,5}
b = {1,2,5}
# 교집합
i = a & b
i = a.intersection(b) # 위와 동일
print(i) # {1,5}
# 합집합 
u = a | b
u = a.union(b)
print(u) # {1,2,3,5}
# 차집합 
d = a - b
d = a.difference(b)
print(d) # {3}
