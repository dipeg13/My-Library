#linear regression
import matplotlib.pyplot as plt

x = [2,4,3,6,8,8,10]
y = [10,9,6,6,6,3,2]
n = len(x)

x_mean = 0
y_mean = 0

for i in x: x_mean+=i
for i in y: y_mean+=i
x_mean = x_mean/n
y_mean = y_mean/n

s1 = 0
s2 = 0
for i in range(n):
    s1+= (x[i] - x_mean) * (y[i] - y_mean)
    s2+= (x[i] - x_mean)**2
tan = s1/s2
c = y_mean -tan * x_mean
yy = lambda x:  tan * x + c

x_line = [min(x),max(x)]
y_line = [yy(0), yy(10)]

plt.plot(x_line , y_line)
plt.plot(x,y,'ro')
plt.show()
