import math

def bisect(f,a,b, TOL):
    if (f(a)*f(b) >= 0):
        print("You have not assumed the right interval.")
        return
    mid = a
    iterations = 0
    while ((b-a) >= TOL):
        mid = (a+b)/2
        result = f(mid)
        # Check if middle point is root
        if (result == 0):
            break
        # Decide the side to repeat the steps
        if (result*f(a) < 0):
            b = mid
        else:
            a = mid
        iterations += 1
        print(f'P{iterations}: {mid:.5f}\tResult: {result}')
    print(f'Root: {mid:.7f}\nIterations: {iterations}')

if __name__ == '__main__':
    f = lambda x: 0.331 - math.asin(x) - (x*(1-x*x)**0.5)
    bisect(f, 0, 1, 0.01)
