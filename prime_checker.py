from math import sqrt


def is_prime_a(n):
    if n < 2:
        return False
    sqrt_n = int(sqrt(n))
    for i in range(2, sqrt_n + 1):
        if n % i == 0:
            return False
    return True


print(is_prime_a(int(input("Enter a number to check: "))))