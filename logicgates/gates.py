def NOT(a):
    return not a

def AND(*args):
    a = True
    for n in args:
        a = a and n
    return a

def NAND(*args):
    a = True
    for n in args:
        a = a and n
    return not a

def OR(*args):
    a = True
    for n in args:
        a = a or n
    return a

def NOR(*args):
    a = False
    for n in args:
        a = a or n
    return not a

def XNOR(a, b):
    return not a ^ b

def XOR(a, b):
    return a ^ b