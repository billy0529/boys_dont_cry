import pay_module ## 동일 폴더에 생성한 모듈 불러오기

# 변수 사용
print(pay_module.version)

# 함수 사용
pay_module.printAuthor()

# 클래스 사용
pay_info = pay_module.Pay("800529", 10000, "2021-07-24")
print(pay_info.get_pay_info())

print(pay_module.__name__)