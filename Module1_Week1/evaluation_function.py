def factorial(n):
    if n >= 0:
        if n == 0 or n == 1:
            return 1
        else: return n * factorial(n - 1)
    else:
        return "Math Error"
def sin(x, n):
    res = 0
    for i in range (n + 1):
        res += ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return res
def cos(x, n):
    res = 0
    for i in range (n + 1):
        res += ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
    return res
def sinh(x, n):
    res = 0
    for i in range (n + 1):
        res += (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return res
def cosh(x, n):
    res = 0
    for i in range (n + 1):
        res += (x ** (2 * n)) / factorial(2 * n)
    return res
if __name__ == "__main__":
    x = float(input())
    n = int(input())
    print("sin({}, {}): {}".format(x, n, sin(x,n)))
    print("cos({}, {}): {}".format(x, n, cos(x,n)))
    print("sinh({}, {}): {}".format(x, n, sinh(x,n)))
    print("cosh({}, {}): {}".format(x, n, cosh(x,n)))
