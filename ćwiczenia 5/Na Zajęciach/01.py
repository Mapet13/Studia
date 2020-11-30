def suma(u1, u2):  return skroc((u1[0]*u2[1] + u2[0]*u1[1], u1[1]*u2[1]))
def odejm(u1, u2): return skroc((u1[0]*u2[1] - u2[0]*u1[1], u1[1]*u2[1]))
def mnoz(u1, u2):  return skroc((u1[0]*u2[0], u1[1]*u2[1]))
def dziel(u1, u2): return skroc((u1[0]*u2[1], u1[1]*u2[0]))
def pot(u, p): 
    if p >= 0:
        return (u[0] ** p, u[1] ** p)
    else:
        return (u[1] ** abs(p), u[0] ** abs(p))
    
    

def skroc(u):
    def nwd(a, b):
        a = abs(a)
        b = abs(b)
        while a*b != 0:
            if a >= b: a %= b
            if a == 0: break
            if b >= a: b %= a
            if b == 0: break
        return a+b
    # end 
    
    r = nwd(u[0], u[1])
    return (u[0] // r, u[1] // r)        
# end         

def wczytaj(s):
   return skroc(tuple(map(int, input(s).split('/'))))
#end  


'''
ax + by = c
dx + ey = f
'''
a = wczytaj("a = ")
b = wczytaj("b = ")
c = wczytaj("c = ")
d = wczytaj("d = ")
e = wczytaj("e = ")
f = wczytaj("f = ")

w = odejm(mnoz(a, e), mnoz(b, d))
wx = odejm(mnoz(c, e), mnoz(b, f))
wy = odejm(mnoz(a, f), mnoz(c, d))

x = dziel(wx, w)
y = dziel(wy, w)

print(x, y)

