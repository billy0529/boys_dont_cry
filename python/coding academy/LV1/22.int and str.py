# 문자와 숫자가섞인 문자열을 입력받을때 구별하여출력해라
# input:
# "c910m6ia 1ho"
# output:
# str : cma ho
# int : 91061

def number(x):
    num_arg, str_arg = "", "" 
    for i in str(x):
        if i.isdigit():
            num_arg = num_arg + i
        else:
            str_arg = str_arg + i
    print("str : ", str_arg)
    print("num : ", num_arg)