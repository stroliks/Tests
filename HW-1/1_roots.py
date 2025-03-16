
import math

def quadratic_equation(a,b,c):
    discriminant = b * b - 4 * a * c

    if discriminant > 0:
        root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Корни уравнения: {root_1}  и {root_2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"Единственный корень уравнения: {root}"
    else:
        return "У уравнения нет действительных корней"


quadratic_equation("a","b","с")