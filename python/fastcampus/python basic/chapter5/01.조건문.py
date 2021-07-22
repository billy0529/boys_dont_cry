## 조건문,py
## 비밀번호 1234 확인. 공백일경우 경고, 비번 불일치시 경고.

passwd = input("비밀번호: ")
origin_pass = "1234"
if origin_pass == passwd:print("비밀번호 확인!"),print("로그인성공")
elif passwd == "":print("공백입니다."),print("처음부터 다시 진행해주세요")
else:print("비밀번호가 일치하지 않습니다."),print("로그인 실패!")




