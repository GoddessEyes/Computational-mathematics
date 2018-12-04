# -*- coding: utf-8 -*-

#Метод хорд и касательных


import math
def fun (x):
    return ((math.sin(x-1)**2)/(math.e)**(x/4))-(0.1)

def prfun(x):
    return (math.sin(2*x-2) + (1/8) * math.cos(2*x-2)-(1/8)) - math.e**-(x/4)



def horda(a, b, eps):
    while (b-a > eps):
        c = a - fun(a)/(fun(b) - fun(a))
        d = a - fun(a)/prfun(a)
        b=c
        a=d
        x_pr=(a+b)/2
    return a, b, x_pr

print(horda(float(input('First num: ')), float(input('Sec num: ')), float(input('Eps: '))))
