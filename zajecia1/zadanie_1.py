#zadanie 1 predefiniowane funkcje

def invoke_functions():
    fun1 = function1_abs(-11)
    print("funkcja 1 abs z liczby -11 :",fun1)
    print("funkcja 2 len z stringu 'hellow, world' :", function2_len("hellow, world"))
    print("funkcja 3 divmod z liczb 4, 5 :", function3_divmod(4, 5))
    print("funkcja 4 max z liczb 8,9,1 :", function4_max(8, 9, 1))
    print("funkcja 5 min z liczb 8,9,1 :", function5_min(8, 9, 1))

def function1_abs(x):
    return abs(x)


def function2_len(text):
    return len(text)


def function3_divmod(x, y):
    return divmod(x, y)


def function4_max(a, b, c):
    return max(a, b, c)


def function5_min(a, b, c):
    return min(a, b, c)