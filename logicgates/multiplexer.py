def AND(a, b): return a & b
def OR(a, b): return a | b
def NOT(a): return 1 - a

def mux(I0, I1, S):
    return OR(AND(NOT(S), I0), AND(S, I1))