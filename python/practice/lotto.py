# lotto number creater

lotto_num = []  # 빈 로또 번호 리스트 생성

import random
def getRandomNumber():
    number = random.randint(1,45)
    return number
count = 0
while True:
    if count == 6:
        break
    random_number = getRandomNumber() # 로또 번호 하나를 뽑는다.
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count = count + 1

print(lotto_num)

