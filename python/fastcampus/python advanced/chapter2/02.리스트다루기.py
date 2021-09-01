# 리스트 다루기

# append 요소 추가

# pop, remove, del 리스트 요소 삭제 
billy = ["sejin", "41", "billy", "male"]
billy.pop(0) # "sejin" 삭제
print(billy)
billy.remove("41") # "41" 데이터 삭제
print(billy)
del billy[1] # "male" 삭제
print(billy) 

# index
print(billy.index("billy"))

# count
print(billy.count("billy"))

# clear 모든 요소 삭제
billy.clear()
print(billy)

# sort 정렬
numbers = [123,52334,634,1634,12526,75334]
numbers.sort()
print(numbers)

# enumerate - for 문에서 인덱스, 요소를 같이 출력
for index, number in enumerate(numbers, 1): # 인덱스 1부터
    print(index, number)

