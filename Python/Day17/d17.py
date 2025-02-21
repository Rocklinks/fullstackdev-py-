def power(base, exponent):

    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    return base * power(base, exponent - 1)
print(power(2,3))


def gcd(a, b):

    a, b = abs(a), abs(b)
    if b == 0:
        return a
    if a == 0:
        return b
    
    return gcd(b, a % b)
print(gcd(4,2))