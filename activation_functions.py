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

epochs = 100
for i in range(epochs):
    print(sigmoid(S(x, w, b)))
    pass