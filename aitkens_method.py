import math
e = math.e
pi = math.pi

accelerate = lambda x0, x1, x2: (x0*x2 - x1*x1)/(x0 + x2 - 2*x1)

def aitkens(f, p, n):
    initial_values = [0] * (n+2)
    for i in range(n+2):
        initial_values[i] = f(p)
        p = initial_values[i]
    print(initial_values)
    for i in range(n):
        result = accelerate(initial_values[i], initial_values[i+1], initial_values[i+2])
        print(f'P{i+1}:\t{result:.7f}')

if __name__ == '__main__':
    f = lambda x: math.cos(x)
    aitkens(f, 0.5, 5)
