def inc(x):
    return x + 1


def dec(x):
    return x - 1

# Operate is a higher order function

def operate(func, x):
    result = func(x)
    return result

a = operate(inc,10)
b = operate(dec,10)
print(a)
print(b)