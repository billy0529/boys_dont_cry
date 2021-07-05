## 함수 실습 2

## 로또 뽑기, 중복 없이
import random

def get_random_number():
    number = random.randint(1,45)
    return number

lotto_num = []
lotto_cnt = 0   ## 무한 반복문이기때문에 6개만 생성할수 있도록 count 변수 생성
while True:
    if lotto_cnt == 6:break
    rand_num = get_random_number()    ## 함수 반환값을 따로 변수로 만들어야 한다. 안그럴시 오작동
    if rand_num not in lotto_num:     ## 숫자가 리스트안에 없을시에만 리스트에 추가함
        lotto_num.append(rand_num) 
        lotto_cnt += 1
        
lotto_num.sort()
for num in lotto_num:
    print(num,end=" ")   # end=" " 는 각 항목 사이를 공백한칸 주고 출력


