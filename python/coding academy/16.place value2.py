# (난이도:기초) 숫자를 입력받으면 그에해당하는 자릿수를 출력하는 코드를 작성하라.

def place_digit(x):
    print("{}의 자릿수".format(10 ** (len(str(x)) - 1)))

place_digit(5000)