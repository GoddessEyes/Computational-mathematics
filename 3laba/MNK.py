# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt 

def estimate_coef(x, y): 
	# количество точек
	n = np.size(x) 

	# среднее для векторов x и y
	m_x, m_y = np.mean(x), np.mean(y) 

	# вычисление перекрестного отклонения и отклонения от x
	SS_xy = np.sum(y*x) - n*m_y*m_x 
	SS_xx = np.sum(x*x) - n*m_x*m_x 

	# вычисление коэффициентов регрессии
	b_1 = SS_xy / SS_xx 
	b_0 = m_y - b_1*m_x 

	return(b_0, b_1) 

def plot_regression_line(x, y, b): 
	# отображение фактических точек в виде графика
	plt.scatter(x, y, color = "m", 
			marker = "o", s = 30) 

	# Вектора (предсказанн. вект. ОТкл) 
	y_pred = b[0] + b[1]*x 

	# построение линии
	plt.plot(x, y_pred, color = "g") 

	# Лэйблы 
	plt.xlabel('x') 
	plt.ylabel('y') 

	# Функция показа 
	plt.show() 

def main(): 
	# Массив чисел (Х соотносится с У по индексу массиву) 
	x = np.array([0, 1, 2, 15, 8]) 
	y = np.array([1, 3, 2, 10, 3]) 

	# оценки коэффициентов
	b = estimate_coef(x, y) 
	print("Приблизительные коэффициенты:\nb_0 = {} \nb_1 = {}".format(b[0], b[1])) 

	# Отрисовка линии
	plot_regression_line(x, y, b) 

if __name__ == "__main__": 
	main() 
