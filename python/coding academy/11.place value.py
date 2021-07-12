## 양의 정수만 입력으로 받고 그 수의 자릿수를 출력해보자.
## ex1) 3 > 1자리수, ex2) 649 > 3자리수 ....

def place_digit():
    x = 0
    while x <= 0:
        x = int(input("Please input positive number:  "))
    print("Place number of {0} is {1}".format(x,len(str(x))))


place_digit()
