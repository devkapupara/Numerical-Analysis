import math

def fixed_point_iteration(f, p, TOL):
    error = 1
    iterations = 0
    while error > TOL:
        p_new = f(p)
        error = abs(p_new - p)
        p = p_new
        iterations += 1
        print(f'p{iterations} = {p: 0.5f}')
    print(f'Root: {p}\nIterations: {iterations}')

if __name__ == '__main__':
    f = lambda x: (math.sin(x) + math.cos(x))/2
    fixed_point_iteration(f, 0, 1e-5)
