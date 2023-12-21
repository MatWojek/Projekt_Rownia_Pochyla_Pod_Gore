import math
G = 9.81
masa = input("podaje mase w kg: ")
print("masa rowna sie: " + masa)
kat = float(input("podaj kat nachylenia w stopniach:"))
print("kat rowna sie: " + str(kat))
# konwersja kąta z stopni na radiany
kat_w_radianach = math.radians(kat)
#obliczenia sily grawitacyjnej na rowni pochylej
sila_grawitacyjna = float(masa) * G * math.sin(kat_w_radianach)
#wynik
print(f"sila grawitacyjna na rowni pochylej rowna sie: {sila_grawitacyjna:.2f} N")