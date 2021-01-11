import math

v = []
r = 2
n = 100
a = (2*math.pi)/n
for i in range(0,n):
    x = r*math.cos(a*i)
    y = 0    
    z = r*math.sin(a*i)
    v += [[x,y,z]]

print(v)
