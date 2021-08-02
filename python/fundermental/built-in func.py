###### ABS ######
number = -20
print(abs(number)) # getting absolute number

###### ALL ######
numbers = [1, 2, 3, 0]
print(all(numbers)) # if one value is fault, return fault
empty = []
print(all(empty)) # if empty, true
print(all(["hello", "world", "0"])) # string all true
# same with dictionary

###### ANY ######
print(any(numbers)) # at least one is true, return true
print(any("")) # empty false

###### BIN ######
print(bin(8)) # return binary, 0b1000, considered as string

###### CALLABLE ######
print(callable(5)) # check if the object is callable, True
def five():
    print("Test")
y = five
print(callable(y)) # False

###### CHR ######
print(chr(97)) # getting unicode string from integor

###### COMPILE ######
codeInString = 'a = 5\nb=6\nsum=a+b\nprint("sum =",sum)'
codeObejct = compile(codeInString, 'sumstring', 'exec')
exec(codeObejct)
### change to AST object or string form to code object

###### CLASSMETHOD ######
class Test:
    name = "billy"
    
    def printName(cls):
        print("name:", cls.name)
Test.printName = classmethod(Test.printName)
Test.printName

###### DELATTR ######
class Coordinate:
    x = 10; y = 20
delattr(Coordinate, 'x') # del class' attribute. 
del Coordinate.y # same

###### DICT ######
numbers = dict(x = 1, y = 2); print(numbers)
dict_1 = dict(zip([1,2,3], ['x','y','z']))
print(dict_1)

###### DIR ######
numbers = [1,2,3]
print(dir(numbers)) # getting valid attributes 

class Test:
    name = "billy"
sejin = Test()
print(dir(sejin))  # .....'name']

###### DIVMOD ######
print(divmod(1,2)) # 2//1 = x, 2%1 = y  (x, y)

###### ENUMERATE ######
billy = ["sejin", "41", "male"]
enu_billy = enumerate(billy)
print(list(enu_billy)) # can use dict, set etc
enu_billy = enumerate(billy, 40)
print(list(enu_billy)) # start with seq no 40

###### STATICMETHOD ######
class Math:
    def sumnum(x,y):
        return x + y
Math.sumnum = staticmethod(Math.sumnum)
print (Math.sumnum(5, 10))

###### FILTER ######
random_list = [1, 'a', 0, False, True, '0']
filtered_list = filter(None, random_list)
print('The filtered elements are:')
for element in filtered_list:
    print(element)

###### EVAL ######
print(eval("1 + 2")) # 3
print(eval("3 > 4")) # false
print(eval("abs(-100)")) # 100
## getting string, return expression

###### FORMAT ######
print(format(12, "f")) # 12.000000

###### FROZENSET ######
print(frozenset(billy)) # getting set but its unchangable

###### GETATTR ######
class Billy:
    name = "sejin"
print(getattr(Billy, "name")) # sejin
print(Billy.name) # sejin

###### GLOBALS ######
name = "billy"
globals()['name'] = "sejin"
print(name) # sejin, change global variable

###### EXEC ######
# program = input('Enter a program:') # input own codes
# exec(program)

###### HASATTR ######
class Billy:
    name = "sejin"
print(hasattr(Billy, "name")) # True
print(hasattr(Billy, "age")) # False

###### HELP ######
# help(list.index) # exit :q

###### HEX ######
print(hex(255)) # 0xff

###### HASh ######
print(hash(16.1)) # return hash value

###### ID ######
print(id(name)) # return ID value

###### ISINSTANCE ######
print(isinstance(billy, list)) # True
print(isinstance(billy, (list, dict))) # list or dict True
print(isinstance(billy, tuple)) # False

###### ISSUBCLASS ######
class Test: a = 1
class Test1(Test): b = 1
print(issubclass(Test1, Test)) # True

###### ITER ######
billy_iter = iter(billy)
print(next(billy_iter)) # sejin
print(next(billy_iter)) # 41
print(next(billy_iter)) # male

###### LOCALS ######
print(locals())

###### LEN ######
testDict = {1: 'one', 2: 'two'}
print(testDict, 'length is', len(testDict))

###### MAX ######
num = [1, 2, 3, 4, 5, 6]
print(max(num)) # 6
print(max(billy)) # sejin, ordered alphabetically

###### MIN ######
print(min(num)) # 1
print(min(billy)) # 41

###### MAP ######
def sum_num(x):
    return x + 1
print(list(map(sum_num, num))) # [2,3,4,5,6,7]
# can replace for, append list
def lst_sum(x,y):
    return x + y
num2 = [10, 20, 30, 40, 50]
print(list(map(lst_sum, num, num2))) # [11, 22, 33, 44, 55]
print(list(map(lambda x, y:x + y, num, num2))) # same result

###### NEXT ######
# check ITER() function
import random
iteran = iter(lambda: random.randint(0,50), 15) # stop when 15
print(next(iteran))



