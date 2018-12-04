# -*- coding: utf-8 -*-

def trapezoidal(f, a, b, n):
	""" 
	Вычисляет приближенное значение интеграла с помощью формулы трапеций
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
	h = float(b - a)/n
	result = 0.5*(f(a) + f(b))
	for i in range(1, n):
		result += f(a + i*h)
	result *= h
	return result

def application():
	from math import exp
	v = lambda x: 3*x**2*exp(x**3)
	n = int(input('n: '))
	numerical = trapezoidal(v, 0, 1, n)

	# Сравнение с точным решением
	V = lambda x: exp(x**3)
	exact = V(1) - V(0)

	error = exact - numerical #abs((exact - numerical)/exact*100)
	print ('Число частичных отрезков: %d, значение интеграла: %.15f, погрешность: %g' % (n, numerical, error))

if __name__ == '__main__':
 	application()
