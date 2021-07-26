names = ["이유덕","이재영","권종표","이재영","박민호","강상희","이재영","김지완","최승혁","이성연","박영서","박민호","전경헌","송정환","김재성","이유덕","전경헌"]

leekim_count = []

for i in names:
    if i[0] == "이" or i[0] == "김":
        leekim_count.append(i)

print("1번답: {0}명".format(len(leekim_count)))

print("2번답: {0}번".format(names.count("이재영")))

print("3번답: {0}".format(set(names)))

names_set_list = list(set(names))
names_set_list.sort()
print("4번답: {0}".format(names_set_list))



