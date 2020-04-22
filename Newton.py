def Newton(f,fd,x0,n):
    '''
    :param f: function
    :param fd: dervative of the function
    :param x0: the intial value
    :param n: number of iterations
    :return: approximation by using newton formula
    '''
    x=0;
    tmp=0;
    print("It no    xi  f(xi)   |xi+1 - xi|")
    for i in range(0,n):
        print(str(i)+"       "+str(x0)+"      "+str(f(x0))+"      "+str(abs(tmp-x0)))
        x=x0-f(x0)/fd(x0)
        tmp=x0;
        x0=x
    return x0;
f = lambda x: x**3+4*x+1 # the funtion
fd = lambda x: 3*x**2 + 4 # the derivative
print( Newton(f,fd,1.5,1) )
