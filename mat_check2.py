import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,11)
y = x ** 2
fig,axes = plt.subplots(figsize=(8,2),nrows = 2,ncols = 1)
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()
fig.savefig('my_plot.png',dpi=1200)
plt.show()