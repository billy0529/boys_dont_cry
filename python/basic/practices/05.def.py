## def

# 다음의 결과와 같이 반목문을 이용해 단어의 순서를 거꾸로 해 반환하는 함수를 작성하고
# 그 함수를 이용해 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.

def wordcheck(word):
    if word == word[::-1]:
        print("This word, {0} is reversible".format(word))
    else:
        word = word[::-1]
        print(word)

a = "sejin"
wordcheck("sejin")

# 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오. 
three = ["가위","바위","보"]
def gbb(x,y):
    if x == y:print("비겼습니다.")
    elif (x == three[0] and y == three[2]) or (x == three[1] and y == three[0]):
        print("{0}가 이겼습니다.".format(three[0]))
    elif (x == three[1] and y == three[0]) or (x == three[0] and y == three[1]):
        print("{0}가 이겼습니다.".format(three[1]))
    elif (x == three[2] and y == three[1]) or (x == three[1] and y == three[0]):
        print("{0}가 이겼습니다.".format(three[2]))
a,b = input(), input()
gbb(a,b)

    

