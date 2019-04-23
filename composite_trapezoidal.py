from math import *

def trapezoidal(f, a, b, n):
    h = (b-a)/n

    total = (f(a)+f(b))/2
    x = a + h

    for i in range(n-1):
        total += f(x)
        x += h

    print(f'Estimate = {total*h:.6f}')

if __name__ == '__main__':
    f = lambda x: x**0.5
    a = int(input("Enter lower limit of integration: "))
    b = int(input("Enter upper limit of integration: "))
    n = int(input("Enter n: "))
    trapezoidal(f, a, b, n)
