##
## 1. 1~9 사이의 정수 a를 입력받아 
## a + aa + aaa + aaaa 의 값을 계산하는 프로그램을 작성하십시오.

# 작성
a = int(input("number? <1-9>"))
print(a + int(str(a)+str(a)) + 
    int(str(a)+str(a)+str(a)) +
    int(str(a)+str(a)+str(a)+str(a)))


# for문 답
a = int(input()) #입력받기
t = 0   #배수계산을 위한 변수
s = 0   #합을 계산하기 위한 변수
for i in range(1, 5): #1부터 4까지 반복
    t = t*10 + 1   #1, 11, 111, 1111 만듬
    s += a*t    # a + aa+ aaa+ aaaa 를 한다.
print(s)    #결과값 출력