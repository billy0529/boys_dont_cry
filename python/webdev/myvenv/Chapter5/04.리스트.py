## 리스트
animals = ["가물치","벼메뚜기","비단뱀","도롱뇽"]
empty = []
print(animals[2]) # 비단뱀
print(animals[-1]) # 도롱뇽
animals.append("고라니") # 고라니 추가
animals[1] = "청개구리" # 벼메뚜기를 청개구리로
del animals[0] # 가물치 삭제
print(animals[1:3]) # 비단뱀 도롱뇽 출력
print(animals[:]) # 전체 출력
print(animals[:3])
print(animals[1:]) 
print(len(animals)) # 항목 갯수 4
animals.sort() # ㄱ,ㄴ 순서로 정렬 
animals.sort(reverse=True) # 역순



