import math as m
import random as rd

def S(x, w, b):
    return (x * w) + b

def sigmoid(S):
    return 1 / (1 + m.exp(-S))

t = 1.00

x = 1.6
w = rd.random()
b = rd.random()

lr = 0.2
epochs = 100

for i in range(epochs):
    s = S(x, w, b)
    y = sigmoid(s)

    dEdW = (y - t) * y * (1 - y) * x
    dEdb = (y - t) * y * (1 - y)

    w = w - lr * dEdW
    b = b - lr * dEdb

    print(w)
    pass