# -*- coding: utf-8 -*-

def rectangular(f, a, b, n):
	""" 
	Вычисляет приближенное значение интеграла с помощью формулы прямоугольников
	f - подынтегральная функция
	a, b - пределы интегрирования
	n - количество частичных отрезков
	"""
	h = int(b - a)/int(n)
	result = f(a+0.5*h)
	for i in range(1, n):
		result += f(a + 0.5*h + i*h)
	result *= h
	return result

def application():
	from math import exp
	v = lambda x: 3*x**2*exp(x**3)
	n = int(input('n: '))
	numerical = rectangular(v, 0, 1, n)

	# Сравнение с точным решением
	V = lambda x: exp(x**3)
	exact = V(1) - V(0)
	error = exact - numerical
	print ('Число частичных отрезков: %d, значение интеграла: %.15f, погрешность: %g' % (n, numerical, error))

if __name__ == '__main__':
	application()
