class Calculator:
    def __init__(billy):
        billy.result = 0
    
    def add(billy, num):
        billy.result += num
        return billy.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
