## 리스트 실습
result = [33,40,12,63,52]
result.append(9)
print(result[2:6]) # 2~5항목 까지 슬라이싱
result[1] = 50 # 40을 50으로
print(result)
result.sort() # 정렬
print(result)

# 실습 2
chinning = []
chinning.append(20)
chinning.append(23)
chinning.append(16)
chinning.append(14)
chinning.append(24)
chinning.append(27)
chinning.append(30)
print(chinning)
avrg = sum(chinning) / len(chinning)
print(int(avrg)) # 나숫셈으로 실수값이 정수형으로 변환. 실수값으로 출력시 22.0으로 나옴