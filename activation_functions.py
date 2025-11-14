import math as m
import random as rd

def S(x, w, b):
    return sum(x[i] * w[i] for i in range(len(x))) + b

def sigmoid(S):
    return 1 / (1 + m.exp(-S))

t = 1.00

x = [2.0, 4.1, 0.3, 1.6, 2.3]
w = [rd.random() for i in range(5)]
b = rd.random()

lr = 0.2
epochs = 1000

for i in range(epochs):
    s = S(x, w, b)
    y = sigmoid(s)

    for j in range(len(x)):
        dEdW = (y - t) * y * (1 - y) * x[j]
        w[j] = w[j] - lr * dEdW

    dEdb = (y - t) * y * (1 - y)
    b = b - lr * dEdb
    print(sigmoid(S(x, w, b)))