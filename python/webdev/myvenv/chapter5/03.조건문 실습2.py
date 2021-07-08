## 조건문 실습3
## 20000원 이상은 치킨 먹기

# cash = int(input("현재 가진 금액은? >>> "))

# if cash >= 20000:print("오늘 저녁은 치킨!")
# elif cash < 20000 and cash >= 10000:print("오늘 저녁은 떡볶이!")
# elif cash < 10000 and cash >= 2000:print("오늘 저녁은 편의점 김밥") 

## 조건문 실습 4
## 80이상 100 이하 불합격, 80이하 합격, 그외 잘못 입력

scores = [] # 빈 리스트
scores.append(int(input("국어 >>> "))) # 리스트에 한개씩 추가
scores.append(int(input("수학 >>> "))) # 리스트에 두번째항 추가
scores.append(int(input("영어 >>> "))) # 리스트에 세번째 항 추가
print("국어: %d"%scores[0]," 수학: %d"%scores[1]," 영어: %d"%scores[2]) #formatting 구버전
print("국어: {0}".format(scores[0])," 수학: {0}".format(scores[1])," 영어: {0}".format(scores[2])) #위와 동일 신버전
print(f"국어: {scores[0]}", f" 수학: {scores[1]}", f" 영어: {scores[2]}") # fstring formatting
def total_scores():  # 점수를 합산해주는 함수
    return sum(scores) # sum으로 리스트내부의 항목을 전부 더한다
def number_scores(): # 점수항목의 갯수를 표현하는 함수
    return len(scores) # len으로 리스트내의 항목 갯수 확인. 예제에서는 3개
average = total_scores() / number_scores() # 총합 나누기 항목 개수 즉 평균을 낸다.
if 80 <= average <= 100: print("불합격!") # 100~80 사이는 불합격, 80이하는 합격
elif average < 80:print("합격")
else:print("잘못 입력하셨습니다.")