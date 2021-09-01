# 문자열 메소드

# replace
print("오늘 날씨는 흐림입니다.".replace("흐림","맑음"))

# find
print("오늘 날씨는 흐림입니다.".find("흐림"))

# find
print("오늘 날씨는 흐림입니다.".count("흐림"))

# 문자열 분리
billy_split = ("billy,sejin,41,male".split(","))
print(billy_split[1])

# 문자열 연결
print(":".join(billy_split))

# 공백 삭제
print("    billy    ".lstrip())
print("    billy    ".rstrip())
print("    billy    ".strip())

print("-" * 30)

