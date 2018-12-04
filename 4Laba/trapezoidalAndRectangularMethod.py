# -*- coding: utf-8 -*-

from trapezoidal import trapezoidal
from rectangular import rectangular

from math import exp

g = lambda x: exp(-x**2)
a = 0; b = 2
print ('%7s   %22s %22s' % ('n', 'прямоугольники', 'трапеции'))
for i in range(1, 22):
	n = 2**i
	r = rectangular(g, a, b, n)
	t = trapezoidal(g, a, b, n)
	print ('%7d %20.16f %20.16f' % (n, r, t))
	