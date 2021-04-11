def is_prime(n):
    if n == 1:
        return False
    if n % 2 != 0 and n / n == 1:
        return True
    if n == 2:
        return True
    else:
        return False
n = int(input("enter number: "))
print(is_prime(n))
