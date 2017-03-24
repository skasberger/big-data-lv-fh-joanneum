import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import defaultdict

columns = defaultdict(list)
columns_m = defaultdict(list)
columns_w = defaultdict(list)

with open('test.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k, v) in row.items():
            if k == 'User' or k == 'geschlecht':
                columns[k].append(v)
            else:
                columns[k].append(float(v))

with open('test_m.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k, v) in row.items():
            if k == 'User' or k == 'geschlecht':
                columns_m[k].append(v)
            else:
                columns_m[k].append(float(v))

with open('test_w.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k, v) in row.items():
            if k == 'User' or k == 'geschlecht':
                columns_w[k].append(v)
            else:
                columns_w[k].append(float(v))

#print(columns)
#print(columns['wohnflaeche'])

#x = np.array([0.0, 1.0, 2.0, 3.0,  4.0,  5.0])
#y = np.array([0.0, 0.8, 0.9, 0.1, -0.8, -1.0])

x = np.array(columns['medienkonsnum_politik'])
y = np.array(columns['zufriedenheit_politik'])
x_m = np.array(columns_m['medienkonsnum_politik'])
y_m = np.array(columns_m['zufriedenheit_politik'])
x_w = np.array(columns_w['medienkonsnum_politik'])
y_w = np.array(columns_w['zufriedenheit_politik'])
print(x)
print(y)

coefficients = np.polyfit(x, y, 4)
polynomial = np.poly1d(coefficients)
ys = polynomial(x)
coefficients = np.polyfit(x_m, y_m, 4)
polynomial = np.poly1d(coefficients)
ys_m = polynomial(x_m)
coefficients = np.polyfit(x_w, y_w, 4)
polynomial = np.poly1d(coefficients)
ys_w = polynomial(x_w)
#print coefficients
#print polynomial

plt.title('Politik: Medienkonsum zu Zufriedenheit (w)')
#plt.plot(x, y, '.')
#plt.plot(x, ys)
#plt.plot(x_m, y_m, 'x')
#plt.plot(x_m, ys_m)
plt.plot(x_w, y_w, 'o')
plt.plot(x_w, ys_w)
plt.xlabel('Medienkonsum Politik')
plt.ylabel('Zufriedenheit Politik')
#plt.xlim(-10, 10)
#plt.ylim(-1, 1)
#plt.ylabel('some numbers')
plt.show()
