n = 3
x = 2

def fun(x, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return fun(x, n / 2) * fun(x, n / 2) * x
    return fun(x, n / 2) * fun(x, n / 2)

print(fun(x, n))