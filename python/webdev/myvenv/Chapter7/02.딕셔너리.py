## 딕셔너리
## 시퀀스 자료형. 순서가 있다.
## 키와 데이터는 한쌍

stock_a = {"삼성전자":[82000,85000], "LG전자":(150000, 200000)}
stock_b = {
    "삼성전자": [81000,81500,82000,81500,82000],
    "LG전자" : (150000,149000,148000,151000,152000)
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단가" : 81000
    }
}

# print(stock_a)
# print(stock_b)
# print(stock_c)

## 딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])  # 삼성전자 항목 안에 보유수량 데이터를 출력

## 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a)

## 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

# 함수
stock_d = {
    "삼성전자" : 82000,
    "SK하이닉스" : 370000,
    "NAVER" : 370000,
    "카카오" : 133000
}
print(stock_d.items())   # 키, 데이터 쌍
print(stock_d.keys())    # 키
print(stock_d.values())  # 데이터

# 각 항목을 for문으로 한개씩 빼내기
for item in stock_d.items():
    print(item[0]) # [0]은 키값, [1]은 데이터값
for key in stock_d.keys():
    print(key) 
for value in stock_d.values():
    print(value) 
