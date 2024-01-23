# Przyśpieszenie i odległość
# a = g*(sin(alfa) - u*cos(alfa))
# s = (v0*t + 1/2*a*t*t)/(1 - (u*g*t*t)/2*v0)
import math

G = 9.81

def przyspieszenie(u, alfa):
    return G*(math.sin(math.radians(alfa)) + u*math.cos(math.radians(alfa)))

# print(przyspieszenie(1, 30))

def droga(v0, t, a, u): #przyjmuje v0 w m/s, czas w s
    return (v0*t+(a*t*t)/2 - (u*G*t*t)/2)

def force(m, alfa):
    return m * G * math.sin(math.radians(alfa))


# print(droga(30, 5, 5, 0.5))

# masa = input("podaje mase w kg: ")
# print("masa rowna sie: " + masa)
# kat = float(input("podaj kat nachylenia w stopniach:"))
# print("kat rowna sie: " + str(kat))
# # konwersja kąta z stopni na radiany
# kat_w_radianach = math.radians(kat)
# #obliczenia sily grawitacyjnej na rowni pochylej
# sila_grawitacyjna = float(masa) * G * math.sin(kat_w_radianach)
# #wynik
# print(f"sila grawitacyjna na rowni pochylej rowna sie: {sila_grawitacyjna:.2f} N")