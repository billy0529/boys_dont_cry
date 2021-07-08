## 반복문
# 20,23,16,14,24,17,30

# data = []
# for i in range(1, 101):
#     x = int(input(i,"일차 턱걸이 횟수 >>>"))
#     data.append(x)

# 반복문 
# 반복해서 명령을 사용하고 싶을때

# 시퀀스 자료형
# 순서가 있는 자료형
# 1. 리스트, 2. 문자열, 3. range 객체, 4. 튜풀, 5. 딕셔너리

# for 문
# 리스트 사용
items = ["1980","sejin","billy"]
for item in items:
    print("정보는",item,"입니다.")
# 문자열 사용
message = "GOOD!"
for word in message:
    print(word)
# range 객체
# range(10) -> 0~9까지 해당 = range(1,10)동일
# range(시작, 끝+1, 단계) 단계는 건너뜀 
for i in range(1,10,2):
    print(i)


