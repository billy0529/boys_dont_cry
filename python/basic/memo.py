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

#.format 
# :< Left aligns the result (within the available space)
# :> Right aligns the result (within the available space)
# :^ Center aligns the result (within the available space)
# := Places the sign to the left most position
# :+ Use a plus sign to indicate if the result is positive or negative
# :- Use a minus sign for negative values only
# :  Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :, Use a comma as a thousand separator
# :_ Use a underscore as a thousand separator
# :b Binary format
# :c Converts the value into the corresponding unicode character
# :d Decimal format
# :e Scientific format, with a lower case e
# :E Scientific format, with an upper case E
# :f Fix point number format
# :F Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g General format
# :G General format (using a upper case E for scientific notations)
# :o Octal format
# :x Hex format, lower case
# :X Hex format, upper case
# :n Number format
# :% Percentage format
"{0:b}".format(37)     # convert to binary. result 100101
int("100101",2) # convert binary to decimal

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
# 비교연산자 == != <> >= <=

# 할당연산자 
a = 10
a = a * 10
a *= 10 # 위와 동일

# 멤버쉽연산자 
a = [1,2,3,4]
b = 3 in a
print(b)

# 바이트리터럴
a = b"123" # 앞에 b를 붙여서 바이트리터럴 (아스키코드)처리한다

# break, continue
i = 0
sum = 0
while True:
    i += 1
    if i == 5:
        continue # while문을 다시 시작한다.
    if i > 10:
        break
    sum += i
print(sum)

# range 함수 (min,max,step) max값은 -1 해야한다. 0부터 시작이므로
for i in range(10): # 루프를 10번 사용하도록 range함수를 이렇게 활용한다.
    print("Hello")

# 리스트 인덱싱
# -1 마지막, -2는 마지막에서 두번째, (::-1)는 거꾸로 reverse

# 리스트 comprehension 
# 리스트 안에서 for문을 사용한다.
# [표현식 for 요소 in 컬렉션 [if 조건식]]
# [이렇게 실행하라, 항목 i에 대해서, 만약 i가 이 조건일때만.(문장 순서가 반대)]
# 아래는 0~9 까지수를 각각 제곱한갑중 3의 배수만 출력
list = [n ** 2 for n in range(10) if n % 3 == 0]
print(list)

# 세트 comprehension
# {출력표현식 for 요소 in 입력Sequence [if 조건식]}
# [이렇게 실행하라, 항목 i에 대해서, 만약 i가 이 조건일때만.(문장 순서가 반대)]
oldlist = [1, 1, 2, 3, 3, 4]
newlist = {i*i for i in oldlist} # 리스트 항목한개씩 제곱한다.
print(newlist) # {16,1,9,4} 

# 딕셔너리 comprehension
# {Key:Value for 요소 in 입력 Sequence [if 조건식]}
id_name = {1: '박진수', 2: '강만진', 3: '홍수정'}
name_id = {val:key for key,val in id_name.items()} # 키와 value를 뒤바꾼다.
print(name_id) # {'박진수': 1, '강만진': 2, '홍수정': 3}
##
def isodd(val):
    return val % 2 == 1
mydict = {x:x*x for x in range(101) if isodd(x)} # 1-100중 숫자를 키, 숫자제곱을 밸류. 단 홀수만.
print(mydict)