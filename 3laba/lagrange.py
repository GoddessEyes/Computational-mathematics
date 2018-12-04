import numpy as np
import matplotlib.pyplot as plt
x=np.array([0,1,2,4,5,6,7,8], dtype=float)
y=np.array([0,2,4,16,25,36,49,64], dtype=float)
h=1
x_pr=3
print(x_pr)
def fun(x_pr):
    print((x_pr**2))
    

def lagranz(x,y,t):
    z=0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1; p2=p2*1   
            else: 
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z
xnew=np.linspace(np.min(x),np.max(x),100)
ynew=[lagranz(x,y,i) for i in xnew]
fun(x_pr)
print(xnew, ynew)
plt.plot(x,y,'o',xnew,ynew)
plt.grid(True)
plt.show()

