#!usr/bin/python
#conding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import seaborn
x=np.linspace(-3,3,50,endpoint=True)
y1=1/(x+3)
y2=np.sqrt(9-x*x)
y3=abs(2*x)
y4=-3*abs(np.sin(x))
plt.figure(figsize = (2,2))
plt.plot(x,y1)
plt.show()
plt.figure(figsize = (2,2))
plt.plot(x,y2,x,-y2)
plt.show()
plt.figure(figsize = (2,2))
plt.plot(x,y3)
plt.show()
plt.figure(figsize = (2,2))
plt.plot(y4,x)
plt.show()
