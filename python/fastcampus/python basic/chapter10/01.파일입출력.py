
# w : 쓰기모드 write
# a : 추가모드 append
# r : 읽기모드 read

# 순서: 파일 열기 - 작업 - 닫기

# w : 덮어쓰기
# a : 이어쓰기
# import pickle

# "r"   Opens a file for reading only.
# "r+"  Opens a file for both reading and writing.
# "rb"  Opens a file for reading only in binary format.
# "rb+" Opens a file for both reading and writing in binary format.
# "w"   Opens a file for writing only.
# "a"   Open for writing.  The file is created if it does not exist.
# "a+"  Open for reading and writing.  
#       The file is created if it does not exist.

# 파일 쓰기
file = open("data.txt", "w", encoding="utf-8")
file.write("1. 파이썬기본")
file.close()

file1 = open("data.txt", "a", encoding="utf-8")
file1.write("\n2. 파이썬심화")
file1.write("\n3. 자세히")
file1.close()

file2 = open("data.txt")
file_read = file2.read()
print(file_read)
file2.close()

