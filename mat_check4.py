import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x ** 2

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8])
ax.plot(x,y,color="purple",lw='1',ls='-',marker='o',ms=20,mfc='red',mew=2,mec='green')
plt.show()