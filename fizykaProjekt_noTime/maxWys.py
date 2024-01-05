import math
G = 9.80665

def maxHeight(v0, alfa, u):
    return (v0**2 * math.sin(math.radians(alfa))**2) / (2 * G * (1 + u))

# def maxHeight(v0, alfa, u):
#     return (v0*v0 * pow(math.sin(math.radians(alfa)), 2)) / (2 * G * (1 - u * math.cos(math.radians(alfa))))


def czas(v0, alfa, s, u):
    return (2 * v0 * math.sin(math.radians(alfa))) / (G * (1 + u))


# def czas(v0, alfa, s, u):
#     return ((v0 + math.sqrt(v0**2 + 2 * G * (u * math.cos(math.radians(alfa)) - math.sin(math.radians(alfa))) * s)) / (G * (math.sin(math.radians(alfa)) - u * math.cos(math.radians(alfa)))))



