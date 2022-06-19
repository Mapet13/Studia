def f(x): return 1/(1+(x*x))
    
    
a = 0
b = 1

h = 1

n = 11

x = []

for i in range(n):
    x_i =(h*i)/10
    print(x_i)
    x.append(f(x_i))

############### prostokatow
p = 0

for i in range(n-1):
    p += f(x[i]) * h
    
print(p)

############### trapwzów
t = 0

for i in range(n-1):
    t += h/2*(f(x[i]) + f(x[i+1]))
    
print(t)
