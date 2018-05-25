#%matplotlib inline 
import numpy as np
import matplotlib.pyplot as plt

#x範圍是0-3，等距切成20個點
x = np.linspace(0, 3, 20)
#y範圍是0-3，等距切成20個點
y = np.linspace(0, 9, 20)
plt.plot(x, y)
plt.show()

#"ro"代表會把所有的點飆出來（會露點）
plt.plot(x, y, "ro")
plt.show()