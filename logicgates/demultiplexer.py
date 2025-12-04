def AND(a, b): return a & b
def OR(a, b): return a | b
def NOT(a): return 1 - a

def demux(I, S):
    Y0 = AND(I, NOT(S))
    Y1 = AND(I, S)
    return Y0, Y1