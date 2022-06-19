
def f1(x, y): return (x**2) + (y**2) - 1
def f2(x, y): return (x**2) - y
def f1x(x, y): return 2*x
def f1y(x, y): return 2*y
def f2x(x, y): return 2*x
def f2y(x, y): return -1

def jacob(x, y): 
    return (f1x(x, y) * f2y(x,y)) - (f2x(x, y)*f1y(x,y))

def delta(x, y, a, b, c, d): 
    return (-a(x, y)*b(x, y) + c(x, y)*d(x, y))/jacob(x, y)

x = 1
y = 1
n = 10

for i in range(n):
    x += delta(x, y, f1, f2y, f2, f1y)
    y += delta(x, y, f2, f1x, f1, f2x)
    print(f"k = {i}, x_k = {x}, y_k = {y}")