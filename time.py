from math import sin, cos, radians
u = 0.5
G = 9.81

def acceleration(alpha, u, g): 
    a = g * (sin(radians(alpha)) + u * cos(radians(alpha)))
    return a

def time(v0,a):
    t = v0/a
    return round(t, 4)
 
alpha = float(input("Podaj kąt (w stopniach): "))
v0 = float(input("Podaj prędkość początkową (w m/s): "))
    
a = acceleration(alpha=alpha, u=u, g=G)
time = time(v0=v0, a=a)
print(f"Czas po jakim klocek wjedzie {time}s")