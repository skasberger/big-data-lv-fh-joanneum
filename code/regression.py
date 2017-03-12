import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])
coefficients = np.polyfit(x, y, 2)
polynomial = np.poly1d(coefficients)
ys = polynomial(x)
print coefficients
print polynomial

plt.plot(x, y, 'o')
plt.plot(x, ys)
plt.ylabel('y')
plt.xlabel('x')
#plt.xlim(-10, 10)
#plt.ylim(-1, 1)
#plt.ylabel('some numbers')
plt.show()
