# from math import sin, cos

# def get_y_delta(f, h, x, y):
#     k1 = h*f(x, y)
#     k2 = h*f(x + h/2, y + k1/2)
#     k3 = h*f(x + h/2, y + k2/2)
#     k4 = h*f(x + h, y + k3)
#     return (k1 + (2 * k2) + (2 * k3) + k4) / 6

# def f(x, y):
#     return sin(x) * cos(x) - y * cos(x)

# n = 1000
# h = 0.001

# x = 0
# y = 0

# for _ in range(n):
#     y += get_y_delta(f, h, x, y)
#     x += h

# print(y)
# ################################################################
from math import sin, cos

def f(x, y):
    return sin(x) * cos(x) - y * cos(x)

n = 1000
h = 0.001

x = 0
y = 0

for _ in range(n):
    y += h*f(x, y)
    x += h

print(y)


# from math import sin, cos, pi

# def euler(f, a, b, n, initial):
#     def f1(x, y, z):
#         return z
#     def f2(x, y, z):
#         return f(x, y)

#     h = (b - a) / n
#     z = initial
#     y = a

#     for i in range(n):
#         x = a+(i*h)
#         y_next = y + h*f1(x, y, z)
#         z_next = z + h*f2(x, y, z)
#         y = y_next
#         z = z_next

#     return y

# def f(x, y):
#     return x - y

# a = 0
# ya = 1
# b = 0.5*pi
# yb = 0.5*pi - 1

# n = 1000

# step = pi/2
# start = -pi

# err = 10e-6
# first_result = euler(f, a, b, n, start)

# init = start + step
# current = euler(f, a, b, n, init)

# while((first_result - yb) * (current - yb) > 0):
#     init =+ step
#     current = euler(f, a, b, n, init)


# if (first_result - yb) > 0:
#     low = init
#     high = start
# else:
#     low = start
#     high = init

# low = min(first_result, current)
# high = max(first_result, current)
# while(abs(yb - current) > err):
#     middle = (high + low) / 2
#     current = euler(f, a, b, n, middle)
#     if(current < yb):
#         low = middle
#     else:
#         high = middle


# print(middle, current)



