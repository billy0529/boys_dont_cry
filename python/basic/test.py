import random

def rannum():
    number = random.randint(100,300)
    return number
count = 0
emlist = []
while count <= 10:
    ran_number = rannum()
    emlist.append(ran_number)
    count = count + 1
print(emlist)