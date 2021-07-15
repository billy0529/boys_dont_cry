# 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자# 

# 10 = 1, 0
# 11 = 1, 1
# 12 = 1, 2
# 13 = 1, 3
# 14 = 1, 4
# 15 = 1, 5# 

# 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개
def number(min, max):
    lst = []
    for x in range(min, max + 1):
        lst = lst + list(str(x))  
    for y in range(0,10):
        print("{0}의 갯수는 {1}개 입니다.".format(str(y),(lst.count(str(y)))))


## 딕셔너리 사용 . 위 코드에 비해 연산속도가 훨씬 빠르다.
count={ x:0 for x in range(0,10) }
for x in range(1,1001):
    for i in str(x):         # 문자열을 순서대로 하나씩 읽는다.
        count[int(i)]+=1     # i에 할당된 value값에 1씩 더한다.
print(count)