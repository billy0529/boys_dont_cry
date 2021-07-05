## 반복문 실습
## 구구단

# dan = int(input("몇단을 입력할까요? >>> "))
# for i in range(1,10):
#     print(dan,"*",i,"=",dan*i)


## 실습2
## 무한반복은 while, 유한반복은 for

while True:
    print(" <<< 번호를 입력하세요 >>> \n 1. 게임시작 \n 2. 랭킹보기 \n 3. 게임을 종료합니다.")
    numb = int(input("번호: "))
    if numb == 1:print("게임을 시작합니다.")
    elif numb == 2:print("실시간 랭킹")
    elif numb == 3:print("게임을 종료합니다.");break
    else:print("다시 입력해주세요")
