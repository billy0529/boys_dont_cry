## 보유한 주식이 목표가에 도달 했을때의 족목별 수익금과 수익률을 출력해주는 프로그램을
# 작성해보자. 

# 수익금 = (목표가 - 매입가) * 수량
# 수익률 = (목표가/매입가 -1) * 100


import csv

data = [
    "종목", "매입가", "수량", "목표가",
    "삼성전자", "85000", "10", "90000",
    "NAVER", "380000", "5", "400000",
    "LG", "30000", "20", "53000"
]

file = open("mystock.csv", "w", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)

file = open("mystock.csv","r", encoding="utf-8-sig")
reader = list(csv.reader(file))
file.close()


# class Bene_margin:
# 
#     def __init__(self, row):
#         self.name = data[row][0]
#         self.purchase = data[row][1]
#         self.qty = data[row][2]
#         self.target = data[row][3]
#     
#     def benefit(self):
#         return (self.target - self.purchase) * self.qty
#         # 수익금 = (목표가 - 매입가) * 수량
# 
#     def margin(self):
#         return round(((self.target / self.purchase - 1 ) * 100), 2) 
#         # 소수점 2자리까지
#         # 수익률 = (목표가/매입가 -1) * 100
# 
#     def data_name(self):
#         return self.name
#         # 종목이름
# 
# samsung = Bene_margin(1)
# print(samsung.data_name(), samsung.benefit(), samsung.margin())
# naver = Bene_margin(2)
# print(naver.data_name(), naver.benefit(), naver.margin())
# lg = Bene_margin(3)
# print(lg.data_name(), lg.benefit(), lg.margin())
# 