# 리스트 내포

# 표현식 for 변수 in 순회가능한 데이터
numbers = [i for i in range(10)]
print(numbers)

# if 문 추가
numbers = [i for i in range(10) if i % 2 == 2]
print(numbers)


# if만 추가할시 else 없이
# 앞글자가 "a"일경우만 출력
words = ['apple', 'watch', 'apolo', 'star', 'abocado']
# 리스트 내포 미 사용
empty_words = []
for i in words:
    if i[0] == "a":
        empty_words.append(i)
print(empty_words)

# 리스트 내포 사용
words_filter = [i for i in words if i[0] == "a"]
print(words_filter)


# if와 else를 같이 사용시
# else 사용시에는 if가 앞에 나온다.
# None 항목은 "empty"로 바꾼다.
drugs = ['오메가3', None, '비타민c500', None, '홍삼절편']
drugs_filter = [i if i is not None else 'empty' for i in drugs]
print(drugs_filter)

