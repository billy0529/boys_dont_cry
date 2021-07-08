##


def calc(*numbers):
    count = 0
    tot = 0
    for n in numbers:
        count += 1
        tot += n

 
print(calc(1,5,2,6))  # (count, tot) 튜플을 리턴
## 함수내에서 연산은 하지만 결과값을 리턴하지 않기 때문에
## None이 출력된다.
## 함수 마지막에 return count,tot 항을 넣으면 결과값이 호출자로 리턴된다.

