# A씨는 두 개의 버전을 비교하는 프로그램을 작성해야 한다.# 
# 버전은 다음처럼 "." 으로 구분된 문자열이다.# 
# 버전 예) 1.0.0, 1.0.23, 1.1# 
# 두 개의 버전을 비교하는 프로그램을 작성하시오.# 
# 다음은 버전 비교의 예이다.
# 0.0.2 > 0.0.1
# 1.0.10 > 1.0.3

def version_check(x,y):
    x_s, y_s = x.split("."), y.split(".")
    for i in range(0,len(x_s)):
        x_s[i] = int(x_s[i])
    for i in range(0,len(y_s)):
        y_s[i] = int(y_s[i])
    x_s[0], x_s[1] = x_s[0] * 100, x_s[1] * 10
    y_s[0], y_s[1] = y_s[0] * 100, y_s[1] * 10
    if sum(x_s) > sum(y_s):
        print("{0} > {1}".format(x,y))
    else:
        print("{0} > {1}".format(y,x))


    
        