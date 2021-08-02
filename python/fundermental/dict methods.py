###### CLEAR ######
dict_1 = {1: "one", 2: "two"}
dict_1.clear()
print(dict_1) # {}

###### COPY ######
dict_1 = {1: "one", 2: "two"}
copy_dict_1 = dict_1.copy() # shallow copy
print(copy_dict_1) 

###### FROMKEYS ######
set_1 = {"s", "e", "j", "i", "n"}
name = ["name"]
dict_2 = dict.fromkeys(set_1, name) # create new dict
name.append("korean") # append new item to value
print(dict_2)

###### GET ######
print(dict_1.get(1)) # it returns value, value is 'one'
print(dict_2.get('s')) # ['name, 'korean']

###### ITEMS #######
print(dict_1.items()) # return tuple pairs

###### KEYS #######
print(dict_1.keys()) # return keys

###### POPITEM ######
print(dict_1.popitem()) # pop and remove last key,value
print(dict_1) # {1: 'one'}

###### SETDEFAULT ######
dict_1 = {1: 'one', 2: 'two', 3: 'three'}
dict_1.setdefault(4, 'four') # inserts key with a value to dict
quatro = dict_1.setdefault(4)
print(quatro)

###### POP ######
print(dict_1.pop(1)) # remove key 1 and value
print(dict_1)

###### VALUES ######
print(dict_1.values()) # return values only

###### UPDATE ######
dict_1.update(dict_2) # merge dict_2 to dict_1
print(dict_1) 
dict_3 = {"country": "usa"}
dict_3.update(up = "canada", down = "mexico") # update when tuple
print(dict_3) # {'country': 'usa', 'up': 'canada', 'down': 'mexico'}

