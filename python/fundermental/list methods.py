###### INDEX ######
lst_num = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
lst_str = ["s", "e", "j", "i", "n", "h", "a", "n"]
print(lst_num.index(1)) #0
print(lst_num.index(2)) #5
print(lst_num.index(3)) #1

# 'n' after the 5th index is searched
index = lst_str.index('n', 5)   # 7
print('The index of n:', index)

# 'n' after the 3rd to 5th index is searched
index = lst_str.index('n', 3, 5)   # 4
print('The index of n:', index)

###### APPEND ######
lst_str.append("billy") # only 1 argument
print(lst_str[8]) # billy

###### EXTEND ######
lst_hundreds = [100, 200, 300]
tuple_hundreds = 400, 500, 600
set_hundreds = {700, 800, 900}
lst_num.extend(lst_hundreds)
lst_num.extend(tuple_hundreds)
lst_num.extend(set_hundreds)
print(lst_num)  # list plus tuple's, dict's, set's args

###### INSERT ######
lst_str.insert(5, "N/A") # add "N/A" to lst_str[5]
print(lst_str)

###### REMOVE ######
lst_str.remove("N/A") # only 1 argument
print(lst_str)

###### COUNT ######
print(lst_num.count(1))
print(lst_str.count("n"))

###### POP ######
lst_num.pop(1) # 3
print(lst_num)  # print without 3, lst_num[1]
lst_num.pop() # 900
print(lst_num) # pop last item, 900
lst_num.pop(-1) # 700
print(lst_num) # pop last item again, 700

###### REVERSE ######
lst_num.reverse()
print(lst_num)
print(lst_num[::-1])  # same operator using slicing
reversed(lst_num) # reversed method
print(lst_num)

###### SORT ######
lst_str.sort(key = len, reverse = True) # use any method to key
print(lst_str)
family = [{'name':'billy', 'age':41, 'sex':'male'},
    {'name':'jane', 'age':10, 'sex':'female'},
    {'name':'bomi', 'age':40, 'sex':'female'},
    {'name':'yui', 'age':7, 'sex':'female'}]

family.sort(key=lambda x: x.get('name'))
print(family, end="\n\n")
family.sort(key=lambda x: x.get('age'))
print(family)

###### COPY ######
lst_num2 = [1, 2, 3, 4, 5]
lst_num3 = lst_num2.copy()
print(lst_num3) # shallow copy

###### CLEAR ######
lst_num.clear()
lst_str.clear()
print(lst_num, lst_str)   ## [] [] emptying the list
