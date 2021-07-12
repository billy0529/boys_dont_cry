# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second) 일까요?
# 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됩니다.

# 3이 들어가면 무조건 60씩 더하게끔 계산
# 아 수학고자는 절대 이렇게 생각 할수가 없다.
sumsec = 0
for hour in range(0,24):
    for minute in range(0,60):
        if "3" in str(hour) or "3" in str(minute):
            sumsec += 60
print(sumsec)