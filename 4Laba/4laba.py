# -*- coding: utf-8 -*-
import math


def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b-a)/float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k*h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result


def f(x):
    return math.sin**2(((x/2)+2)**2)-(x/5)

print("Используем формулу прямоугольников")
print("Интегрируемая функция: sin**2(((x/2)+2)**2)-(x/5)")
print("Точность: 0.001")

n = 2
a1 = work(f, 1, 10, n)
n *= 2
a2 = work(f, 1, 10, n)

while math.abs(a1 - a2) > 0.001:
    n *= 2
    a1 = work(f, 1, 10, n)
    n *= 2
    a2 = work(f, 1, 10, n)

print("\nОтвет:", a2, "\nКоличество разбиений:", n)




