def square(a):
    p = 4 * a
    s = a * a
    d = (a ** 2) / 2
    d = d ** 0.5
    k = (p, s, d)
    return k
n = int(input("enter number: "))
print(square(n))
