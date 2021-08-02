# 1. 파이썬 객체를 pickle로 저장하기
from os import lseek
import pickle

billy = {
    "name": "billy",
    "age": 41,
    "sex": "male"
}

file = open("billy.pickle","wb") # wb: write binary
pickle.dump(billy, file)
file.close()# 


# 2. pickle 파일을 파이썬으로 가져오기# 
file = open("billy.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()

