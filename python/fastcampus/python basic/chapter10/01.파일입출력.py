
# w : 쓰기모드 write
# a : 추가모드 append
# r : 읽기모드 read

# 순서: 파일 열기 - 작업 - 닫기

# w : 덮어쓰기
# a : 이어쓰기
# import pickle

# 파일 쓰기
file = open("data.txt", "w", encoding="utf-8")
file.write("1. 파이썬기본")
file.close()

# 파일 추가
file = open("data.txt", "a")
file.write("\n2. 파이썬심화")
file.close()

# 파일 전체 읽기 
file = open("data.txt", "r", encoding="utf-8")
# data = file.read()
# print(data)
# file.close()

# 파일 한 줄 읽기
while True:
    data = file.readline()
    print(data, end = "")
    if data == "":
        break
file.close()