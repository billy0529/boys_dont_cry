## for while

# 다음의 결과와 같이 5명의 학생의 점수에 대해 60 이상일 때 합격 메시지를 출력하고,# 
# 60미만일 때 불합격 메시지를 출력하는 프로그램을 만드십시오
student1 = int(input("Please input Student1's Score >>> "))
student2 = int(input("Please input Student2's Score >>> "))
student3 = int(input("Please input Student3's Score >>> "))
student4 = int(input("Please input Student4's Score >>> "))
student5 = int(input("Please input Student5's Score >>> "))
scores = [student1, student2, student3, student4, student5]
studentnumber = 1
for i in scores:
    if i >= 60:
        print("student{0}님 합격입니다.".format(studentnumber))
        studentnumber += 1
    else:
        print("student{0}님 불합격입니다.".format(studentnumber))
        studentnumber += 1
    
#답변
result = [88, 30, 61, 55, 95]
for i in range(0, 5):
   if result[i] >= 60:
      ispass = "합격"
   else:
      ispass = "불합격"
   print("%d번 학생은 %d점으로 %s입니다." % (i+1, result[i], ispass))

# 1부터 100까지의 숫자를 for 문과 range 함수를 이용해 출력하십시오.
for i in range(1,101):
    print(i)

# 1부터 100사이의 숫자 중 짝수를 for 문을 이용해 다음과 같이 출력하십시오.
for i in range(1,101):
    if i % 2 == 0:
        print(i)

# & 연산으로
for i in range(1, 101):
   if not (i & 1):   # 1~100중 한개씩 1과 and 연산하여 0 결과값만 출력. 결과적으로 짝수만
      print(i, end = " ")

# 1부터 100사이의 숫자 중 3의 배수의 총합을 for 문을 이용해 출력하십시오.
total = []
for i in range(1,101):
    if i % 3 == 0:total.append(i)
print(sum(total))

# 다른방식
result = 0
for i in range(1, 101):
   if not (i % 3):
      result += i
print("1부터 100사이의 숫자 중 3의 배수의 총합: {0}".format(result))

