## if 문 연습

# 입력된 영어 알파벳 문자에 대해 대소문자를 구분하는 코드를 작성하십시오.
a = input()
if 'a' <= a <= 'z':   ## 비교연산은 알파벳도 가능
   print("%s 는 소문자 입니다." % a)
elif 'A' <= a <= 'Z' :
   print("%s 는 대문자 입니다." % a)



# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 소문자일 경우 대문자로 변경하고,# 
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.# 
# 출력 시 아스키코드를 함께 출력합니다.
a = input()
#소문자일경우
if a.islower():
   print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.upper(), ord(a.upper())))
#대문자일경우
elif a.isupper():
   print("%s(ASCII: %d) => %s(ASCII: %d)" % (a, ord(a), a.lower(), ord(a.lower())))
#알파벳이 아닐경우
else :
   print(a)

# 1~200 사이의 정수 가운데 7의 배수이면서 5의 배수는 아닌 모든 숫자들을 찾아# 
# 콤마(,)로 구분된 문자열을 구성해 출력하는 프로그램을 작성하십시오.
numbers = []
for i in range(1,200):
    if i % 7 == 0 and i % 5 != 0:
        numbers.append(str(i))
print(",".join(numbers))


# 100~300 사이의 숫자에서 각각의 자리 
# 숫자가 짝수인 숫자를 찾아 콤마(,)로 구분해 출력하는 프로그램을 작성하십시오
numbers = []
for i in range(100,301):
    if int(str(i)[0]) % 2 == 0 and int(str(i)[1]) % 2 == 0 and int(str(i)[2]) % 2 == 0:
        numbers.append(str(i))
print(",".join(numbers))


#답변
arr = []
for i in range(100,301):
    a = i
    t = False
    for k in range(3):
        if (i % 10) % 2 != 0:
            t = True
            break
        i = i // 10
    if t == False:
        # 조인할때 타입을 맞춰야하므로 string으로 형변환
        arr.append(str(a))
print(",".join(arr))