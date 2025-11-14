import math as m

def S(x, w, b):
    return (x * w) + b

def sigmoid(S):
    return 1 / (1 + m.exp(-S))