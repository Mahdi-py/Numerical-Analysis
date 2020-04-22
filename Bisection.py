import math
import matplotlib.pyplot as plt
import numpy as np
def bisectionIteration(f,a,b,N):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    for n in range(1,N+1):
        m_n = (a_n + b_n)/2
        f_m_n = f(m_n)
        if f(a_n)*f_m_n < 0:
            a_n = a_n
            b_n = m_n
        elif f(b_n)*f_m_n < 0:
            a_n = m_n
            b_n = b_n
        elif f_m_n == 0:
            print("Found exact solution.")
            return m_n
        else:
            print("Bisection method fails.")
            return None
    return str ((a_n + b_n)/2)+" Between ("+str(a_n)+","+str(b_n)+")"

def bisection(f, a, b, E):
    '''
    :param f: Function
    :param a: the starting of the interval
    :param b: the ending of the interval
    :param E: error accourcy
    :return: returns an approximation with the interval
    '''
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    a_n = a
    b_n = b
    i = 0
    print('i    a   b   c   f(c)    Error')
    while True:
        c = (a_n + b_n) / 2
        fc = f(c)
        print(str(i)+"    "+str(a_n)+"    "+str(b_n)+"    "+str(c)+"    "+str(fc)+"    "+str(abs(b_n - c)))
        if abs(fc) <= E or abs(b_n - c) <= E:
            break
        if f(a_n) * fc < 0:
            a_n = a_n
            b_n = c
        elif f(b_n) * fc < 0:
            a_n = c
            b_n = b_n
        i=i+1
    return str((a_n + b_n) / 2) + " Between (" + str(a_n) + "," + str(b_n) + ")"
def NoOfIteration(a,b,Error):
    return (math.log((b-a)/Error)) / math.log(2)

f = lambda x: x**5 - 2*x - 5
print(bisection(f,0,3,0.00001))

x = np.arange(-10,10,0.00001)
y= x**5 - 2*x - 5
plt.figure()
plt.plot(x,y)
plt.xlim(-2,5)
plt.ylim(-10,5)
# draw axes
plt.axvline(x=0, color='#A9A9A9')
plt.axhline(y=0, color='#A9A9A9')
plt.show()
plt.close()
