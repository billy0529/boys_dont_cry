## [python] 날짜, 시간관련 모듈

import datetime 
from datetime import timedelta

# 현재시간
now = datetime.datetime.now()    # 뱐수로 저장하는 순간 시간이 고정된다.
print(now) 

nowdate = now.strftime('%Y -- %m -- %d')   ## 날짜 사이 형식을 변경할수 있다.
# %y - 뒷 두자리 연도만 %Y 4연도 모두 표현
# %D - 연도, 월까지 / 로 구분해서 2개씩 표현 21/07/21
# %d - 일 날짜만
print(nowdate)
nowtime = now.strftime('%H : %M : %S')
print(nowtime)
nowdatetime = now.strftime('%Y/%m/%d %H:%M:%S') 
print(nowdatetime)

# 문자열로 받아서 클래스로 변경가능
date = "2016-04-13 01:00:50"
mydate = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
print(mydate)

# 변경은 replace
replace_date = mydate.replace(year = 2013,month = 6, day = 1)
print(replace_date)

# 날짜만 사용시 datetime.date
# 시간만 사용시 datetime.time
date = datetime.date(2013,6,1)
time = datetime.time(2,0,5)
print(date)
print(time)

# 합치려면 combine
datetime = datetime.datetime.combine(date,time)
print(datetime)

# 각 항목에 접근하려면 timetuple
nowtuple = now.timetuple()
print(nowtuple)
print(nowtuple.tm_year) #2021

# 날짜 연산 
tomorrow = now + timedelta(days=1)  # 변수로 저장된 날짜에 하루를 더했다.
print(tomorrow)
# timedelta에 들어갈 수 있는 인자값은 아래와 같다.
# – 1주 : datetime.timedelta(weeks=1)
# – 1일 : datetime.timedelta(days=1)
# – 1시간 : datetime.timedelta(hours=1)
# – 1분 : datetime.timedelta(minutes=1)
# – 1초 : datetime.timedelta(seconds=1)
# – 1밀리초 : datetime.timedelta(milliseconds=1)
# – 1마이크로초 : datetime.timedelta(microseconds=1)
oneDatetime = datetime.strptime('2015-04-15 00:00:00', '%Y-%m-%d %H:%M:%S')
twoDatetime = datetime.strptime('2015-04-16 00:00:10', '%Y-%m-%d %H:%M:%S')
result = twoDatetime - oneDatetime   # 날자에서 날자빼기 연산
print(result)         # 1 day, 0:00:10
print(result.days)    # 1
print(result.seconds) # 10

