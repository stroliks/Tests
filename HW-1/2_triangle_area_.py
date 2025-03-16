import math


def triangle_area(a, b, c):
    if a<0 or b < 0 or c < 0:
        raise ValueError("Сторона должна быть больше нуля")
    if (a + b > c) and (a + c > b) and (b + c > a):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return f"Площадь треугольника: {area}"
    raise ValueError("Треугольника не существует")


print(triangle_area(100,100,200))
