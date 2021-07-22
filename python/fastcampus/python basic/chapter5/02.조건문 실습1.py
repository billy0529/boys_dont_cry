# 조건문 실습1
# 구독자가 1000명 이상일경우 수익 창출 가능 메시지 출력

subscribers = int(input("현재 구독자 수를 입력하세요 >>> "))
income_subs = 1000
if subscribers >= income_subs:print("수익 창출이 가능합니다!")
elif subscribers < income_subs:print("수익 창출이 불가합니다!")

## 조건문 실습2
## 10시간 이상 공부 휴대폰 잠금해제, 5시간이상 휴대폰 30분 사용, 그 이하 불가능 

studyhour = int(input("공부시간을 입력하세요 >>> "))
if studyhour >= 10:print("휴대폰 잠금이 해제됩니다.")
elif studyhour < 10 and studyhour >= 5:print("휴대폰을 30분간 사용가능합니다.")
else:print("휴대폰 사용이 불가능합니다.")