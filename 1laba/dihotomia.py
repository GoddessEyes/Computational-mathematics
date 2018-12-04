# -*- coding: utf-8 -*-

#Метод половинного деления

import math

def fun (x):
    return ((math.sin(x-1)**2)/(math.e)**(x/4))-(0.1)



def dihotomia(a, b, eps):

    while (b - a) > eps:

        x = (a + b) / 2
        fx = fun(x)
        fa = fun(a)
        if ((fx * fa) < 0):
            a = x
        else:
            b = x
    return x

print(dihotomia(float(input("First num: ")), float(input("Second num: ")), float(input("E= "))))




