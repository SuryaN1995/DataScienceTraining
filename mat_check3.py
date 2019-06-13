import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label='first')
ax.plot(x,x**3,label='second')
ax.legend(loc=0)
plt.show()