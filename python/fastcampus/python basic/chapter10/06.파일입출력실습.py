## 보유한 주식이 목표가에 도달 했을때의 족목별 수익금과 수익률을 출력해주는 프로그램을
# 작성해보자. 

# 수익금 = (목표가 - 매입가) * 수량
# 수익률 = (목표가/매입가 -1) * 100

import csv

def show_profit(data):
    name = data[0]
    purchase = int(data[1])
    amount = int(data[2])
    target_price = int(data[3])
    
    profit = (target_price - purchase) * amount
    profit_ratio = ((target_price / purchase - 1) * 100)
    print("{} {} {}%".format(name, profit, round(profit_ratio, 2)))

# 파일 열기
file = open("mystock.csv", "r")

reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data)    


file.close()

