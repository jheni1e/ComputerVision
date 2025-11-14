import math as m
import random as rd

def S(x, w, b):
    return (x * w) + b

def sigmoid(S):
    return 1 / (1 + m.exp(-S))

t = 1.00

x = [2.0, 4.1, 0.3, 1.6, 2.3]
w = [rd.random() for i in range(5)]
b = rd.random()

lr = 0.2
epochs = 1000

for i in range(epochs):
    for j in range(len(x)):
        s = S(x[j], w[j], b)
        
        y = sigmoid(s)

        dEdW = (y - t) * y * (1 - y) * x[j]

        w[j] = w[j] - lr * dEdW

        print(sigmoid(S(x[j], w[j], b)))
        
    dEdb = (y - t) * y * (1 - y)
    b = b - lr * dEdb
    pass