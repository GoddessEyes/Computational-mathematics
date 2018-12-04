# -*- coding: utf-8 -*-
#Метод итераций


import math



def fun (x):
    return ((math.sin(x-1)**2)/(math.e)**(x/4))-(0.1)

def prfun(x):
    return (math.sin(2*x-2) + (1/8) * math.cos(2*x-2)-(1/8)) - math.e**-(x/4)

def prfuntwo(x):
    return (-(31/16)*math.sin**2 * (x - 1) - math.sin(x - 1) * math.cos(x - 1) + 2*math.cos**2 * (x-1)) * math.e**(-x/4)



def iter (a,b, eps):
    x_sled = a
    x_pred = b

    while (math.fabs(x_pred - x_sled) > eps):
        x_pred = x_sled
        x_sled = x_pred-0.1*fun(x_pred)


    x_pr = x_sled
    x_pr = (a+b)/2
   
    fun(x_pr)
        
    

print(iter(float(input("First num: ")), float(input("Second num: ")), float(input("E= "))))