# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?# 

# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)


lst = []
eight = "8"
for i in range(1,1000001):
    for m in str(i):
        if eight == m:
            lst.append(int(m))
print(lst.count(8))

# 한줄
print(str(list(range(1, 1000001))).count('8'))