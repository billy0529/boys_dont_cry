
# 배열 [a, b, c, d]를 입력하면 배열[bcd, acd, abd, abc]를 출력하는 코드를 작성하시오.# 
# (단, 나눗셈 사용 금지)# 
# 입출력되는 배열은 어떤 형식이든 상관없습니다


def triple(x):
    lst = []
    lst.append((x[1] * x[2] * x[3])) 
    lst.append((x[0] * x[2] * x[3]))
    lst.append((x[0] * x[1] * x[3])) 
    lst.append((x[0] * x[1] * x[2]))
    print(lst)


triple([2,6,3,7])
