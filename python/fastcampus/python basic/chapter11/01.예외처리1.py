## 예외처리


number = input("Number: ")
division = input("Division: ")

try: # 예외 발생 가능
    print(round((int(number) / int(division)), 3))
except ValueError as err: # 예외 발생시 실행
    print("숫자를 입력하지 않았습니다.", err)
except ZeroDivisionError as err: #0으로 나누는 오류시
    print("0으로 나눌수 없습니다.", err)
else: # 예외가 발생하지 않으면 실행됨
    print("예외가 발생하지 않고 잘 실행되었습니다.")
finally: # 예외가 발생하던 안하던 실행됨, 리소스를 무조건 반환해야할때 사용
    print("실행 종료")

# print("프로그램이 끝났나요?")