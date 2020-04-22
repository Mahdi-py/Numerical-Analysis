import math
import numpy as np


def f(x):
    x = float(x)
    y = (math.e ** x) / x
    return y


def fillaray(nn):
    xi = float(a)
    for i in range(0, nn - 1):
        xi = xi + h
        barry.append(xi)


def multi():
    for i in range(0, len(barry)):
        barry[i] = f(barry[i])
    for i in range(len(barry)):
        if i % 2 == 0:
            # print("odd",barry[i])
            barry[i] = barry[i] * 4
        if i % 2 != 0:
            # print("even",barry[i])
            barry[i] = barry[i] * 2
    # print(barry)


def final():
    sumarray = float(0)
    for i in range(0, len(barry)):
        sumarray = barry[i] + sumarray

    # print(h/3,"[ ",functionx(a),"+",barry,"+",functionx(b)," ]")
    simp = sumarray + f(a) + f(b)
    simp = (h / 3) * simp
    return simp


a = float(1)
b = (2)
n = float(5)
simp = float(0)

barry = []
barry = []
h = (float(b) - float(a)) / float(1000)
fillaray(1000)
multi()
exact = final()

for i in range(10, 110, 10):
    barry = []
    h = (float(b) - float(a)) / float(i)

    fillaray(i)
    # print(barry)
    multi()
    simp = final()
    # print(barry)
    # print("a =", a, ",b =", b, ",h =", h)
    print(i, "|Approximation:", simp, "|Error:", np.abs(exact - simp))
'''
    n = 200
    
    barry = []
    h = (float(b) - float(a)) / float(n)
    print("a =", a, ",b =", b, ",h =", h)
    fillaray()
    print(barry)
    loop()
    simp = final()
    # print(barry)
    print(n, "-approximation: ", simp,"--",)
'''
