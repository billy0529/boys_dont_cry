## 함수 실습


def printSumAvg(x,y,z): 
    """
    합계와 평균
    """
    total = x+y+z
    avg = total / 3
    print("합계: {0}".format(total), "평균: {0}".format(int(avg)))
    print(f"합계: {total} 평균: {int(avg)}") # 문자열 포매팅 다른 방식
printSumAvg(5,7,9)

