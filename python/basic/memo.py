# 리터럴 무시
# 100_000_000_000 -> 100000000000

# 2진수 0b
# 8진수 0o
# 16진수 0x

# 얀산
# + - * 
# ** 제곱
# /  나누기 // 나누기후 소수점 버리기
# % 나누기후 나머지만 구함, 배수 구할때 이용

# 허수 j

# 이스케이프 시퀀스
print("줄\n바꿈")
print("\"")
print("\'")
print("\\")
print("\t 탭")

# 배수 확인
import random
number = random.randint(3,101)
if number % 3 == 0: # 3의 배수인지 확인
    print("{}는 3의 배수입니다.".format(number))
elif number % 3 != 0:
    print("{}는 3의 배수가 아닙니다.".format(number))

# .join 
myself = ["sejin", "billy", "1980"] # 문자열만 가능
print(" / ".join(myself))

# and 연산
# >>> 10 and 12
# 10  <--- x 값이 True이면 y값을 리턴
# >>> 0 and 12
# 0 <--- x 값이 False면 x값 리턴

# &, or binary 얀산
# & 이진수 and 연산 
# or or 연산
