import math
import matplotlib.pyplot as plt
from matplotlib import mlab
 
 
# начальные условия
x0 = 0
y0 = 1
# шаг
h = 0.1
# отрезок [x0, xn], где x0 = 0, xn = 1
xn = 1
 
 
f = lambda x, y: y * math.cos(x)
ilist = mlab.frange(0, 10, 1)
xlist = [(x0+h*i) for i in ilist]
ylist = []
 
 
prev = y0
print("метод Эйлера")
for x in xlist:
    y = prev + h*f(x,y0)
    prev = y
    ylist.append(prev)
    print(y)
 
    
# массив со значениями точного решения  
lst = []
print("\nТочное решение:", )
for x in xlist:
    func = math.e ** math.sin(x) # точное решение
    lst.append(func)
    print(func)
 
 
 
plt.rc('font',**{'family':'verdana'})
plt.xlabel("ось абцисс")
plt.ylabel("ось ординат")
plt.plot(xlist, ylist, "b-", label="метод Эйлера")
plt.plot(xlist, lst, "g-", label="точное решение")
plt.legend()
plt.grid()
plt.show()