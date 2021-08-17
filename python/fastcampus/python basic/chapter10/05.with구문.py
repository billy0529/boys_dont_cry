with open("data.txt","r+", encoding="utf-8") as file:
    file.write("1. Chapter1\n")
    file.write("2. Chapter2\n")
    file.write("3. Chapter3")

with open("data.txt", "r+") as file:
     data = file.read()
     print(data)

