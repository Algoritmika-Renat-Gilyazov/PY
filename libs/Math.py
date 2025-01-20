
def sum(*args):
    x = 0
    for n in args:
        x += n
    return x
def multiply(*args):
    x = 1
    for n in args:
        x *= n
    return x
def power(base, *args):
    for n in args:
        base **= n
    return base
def middle(*args):
    a = 0
    x = 0
    for n in args:
        x += n
        a += 1
    return x / a