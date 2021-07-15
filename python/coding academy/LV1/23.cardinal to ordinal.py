# 기수(Cardinal)를 입력하면 영어 서수(Ordinal)로 출력하는 함수를 작성합니다.
import re
def ordinal(*x):
    lst = []
    for i in x:
        if re.match("1$", str(i)):
            i = str(i) + "st"
            lst.append(i)
        elif re.match("2$", str(i)):
            i = str(i) + "nd"
            lst.append(i)
        elif re.match("3$", str(i)):
            i = str(i) + "rd"
            lst.append(i)
        else:
            i = str(i) + "th"
            lst.append(i)
    print(lst)

## 나머지 연산 사용
def num(n):
    if n%10==1 and n%100!=11:
        return str(n)+"st"
    elif n%10==2 and n%100!=12:
        return str(n)+"nd"
    elif n%10==3 and n%100!=13:
       return str(n)+"rd"
    else:
        return str(n)+"th"


ordinal(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)