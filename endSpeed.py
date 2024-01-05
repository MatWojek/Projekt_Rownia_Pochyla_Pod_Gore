# program na prędkość końcową 
from math import radians, sin, sqrt, pow, cos
T = 0.5
G = 9.81

alpha = float(input("Podaj kąt (w stopniach): "))
v0 = float(input("Podaj prędkość początkową (w m/s): "))
h = float(input("Podaj wysokość (w metrach): "))

def end_speed(alpha, v0, h, a): 
    s = h/sin(radians(alpha))
    print(s)
    vk = sqrt(pow(v0, 2) - 2*a*s)
    return round(vk, 4)

def acceleration(alpha, t, g): 
    a = g * (sin(radians(alpha)) + t * cos(radians(alpha)))
    return a

def unit_conversion(not_modified_speed):
    modified_speed = (not_modified_speed * 1000)/3600
    return round(modified_speed, 4)

a = acceleration(alpha=alpha, t=T, g=G)
print(a)
end_speed = end_speed(alpha=alpha, v0=v0, h=h, a=a)
modified_speed = unit_conversion(end_speed)

print(f"Prędkość końcowa równa się {end_speed} m/s")
print(f"Prędkość końcowa równa się {modified_speed} km/h")