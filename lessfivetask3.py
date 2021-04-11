import math
def area(tip):
    if tip == 1:
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        c = int(input("Введите сторону c: "))
        p = (a + b + c) / 2
        s = math.sqrt((p * (p - a) * (p - b) * (p - c)))
        return s
    if tip == 2:
        a = int(input("Введите сторону a: "))
        b = int(input("Введите сторону b: "))
        c = int(input("Введите угол: "))
        s = 0.5 * a * b * math.sin(c)
        return s
    if tip == 3:
        a = int(input("Введите сторону: "))
        s = a ** 2
        return s
tip = int(input(("введите "'1'" если известно 3 стороны, "'2'" если 2 стороны и угол, "'3'" если квадрат: ")))
print((area(tip)))
