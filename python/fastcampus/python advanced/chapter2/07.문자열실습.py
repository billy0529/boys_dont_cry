# x시간 y분을 문자열로 받아서 모두 분으로 환산하는 실습
# 예) 1시간 30분 => 출력 90분

# time = "10시간"
# 
# if time.find('시간') == -1:
#     result = int(time.split('분')[0])
# else:
#     if time.find('분') == -1:
#         result = int(time.split('시간')[0]) * 60
#     else:
#         sub = time.split('시간')
#         result = int(sub[0]) * 60 + int(sub[1].split('분')[0])
# print(result, "분")
#



time = input("시간을 입력하세요(x시간 x분) >>> ")

if time.find("시간") == -1:
    result = int(time.split("분")[0])
else:
    if time.find("분") == -1:
        result = int(time.split("시간")[0]) * 60
    else:
        sub = time.split('시간')
        result = int(sub[0]) * 60 + int(sub[1].split('분')[0])
print(result)