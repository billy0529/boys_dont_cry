## 튜플
## 시퀀스 자료형 (순서가 있는 자료형)
## 수정,추가,삭제 불가 (read only)
## 리스트보다 메모리 적게 점유
## 데이터 손실의 염려가 없음

#튜플 생성
a = 1,2,3
a = 1, # 한개항목 생성 콤마 제거할경우 int로 인식


#리스트 <-> 튜플
a = 1,2,3
b = list(a)
c = [4,5,6]
d = tuple(c)
print(type(b)) # list type
print(type(d)) # tuple type
f = list(range(10)) 
g = tuple(f) # range 10값을 튜플로

# 변수 자리바꿈
a,b = b,a

#패킹, 언패킹
numbers = 3,4,5
a,b,c = numbers
print(a,b,c) # 3 4 5 

# 튜플 함수 / 리스트도 동일
a = 10,20,30,40,30
a.index(20) # 인덱스 답은 1
a.count(30) # 값갯수 2개가 있으므로 2
max(a) # 값중 최대값 40
min(a) # 값중 최소값 10
sum(a) # 합계
