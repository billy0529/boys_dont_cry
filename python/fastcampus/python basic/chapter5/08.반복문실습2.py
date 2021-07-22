## 반복문실습 2

# 한국어 시험 while 문 구현
# x = ["한국","서울","부산"]
# print("Let's study Korean!")
# while True:
#     first = input("%s >> 한글로 입력하세요. >> "%x[0])
#     if first == x[0]:
#        second = input("%s >> 한글로 입력하세요. >> "%x[1])
#         if second == x[1]:
#            third = input("%s >> 한글로 입력하세요. >> "%x[2])
#             if third == x[2]:break
#             else:break
#         else:break
#     else:break

# 한국어 시험 for 문 구현
word_list = ["한국","서울","부산"]
print("Let's study Korean!")
print("전체 문제 갯수: ",len(word_list))
score = 0
for word in word_list:
    print(word)
    data = input()
    if data == word:
        score += 1
print("맞은 문제 갯수: %d"%score)
print("틀린 문제 갯수: %d"%(len(word_list)-score))
