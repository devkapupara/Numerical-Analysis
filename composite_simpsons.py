from math import *

def simpsons(f, a, b, n):
    if n % 2 == 1:
        print(f"Number of intervals must be even for Simpson's method. Changing your N to {n+1}")
        n += 1
    h = (b-a)/n

    total = f(a) + f(b)
    x = a+h

    for i in range(n-1):
        coeff = 2 if (i & 1) else 4
        total += coeff * f(x)
        x += h

    print(f'Estimate = {total*h/3:.9f}')

if __name__ == '__main__':
    f = lambda x: x**0.5
    a = int(input("Enter lower limit of integration: "))
    b = int(input("Enter upper limit of integration: "))
    n = int(input("Number of intervals: "))
    simpsons(f, a, b, n)
