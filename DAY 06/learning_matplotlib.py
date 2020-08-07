from matplotlib import pyplot as plt
import numpy as np

# plt.style.use('fivethirtyeight')
plt.xkcd()

x = np.arange(0, 4*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin, label = "sin")
plt.plot(x, y_cos, label = "cos")

plt.xlabel('theta')
plt.ylabel('sin and cosine values')

plt.title("sin and cosine graph")
plt.legend()
# plt.grid(True)


plt.savefig('plot.png')
plt.show()




