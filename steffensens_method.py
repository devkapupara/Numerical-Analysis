import math

accelerate = lambda x0, x1, x2: (x0*x2 - x1*x1)/(x0 + x2 - 2*x1)

def steffensens(f, p, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        p1 = f(p)
        p2 = f(p1)
        p_new = accelerate(p, p1, p2)
        error = abs(p_new-p)
        iterations += 1
        print(f'P0: {p:.7f}\nP1: {p1:.7f}\nP2: {p2:.7f}\nP-hat_{iterations}: {p_new:.7f}\n')
        p = p_new
    print(f'Final value: {p}\nIterations: {iterations}')

if __name__ == '__main__':
    f = lambda x: 5**-x
    steffensens(f, 0, 5e-2)
