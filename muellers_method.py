MAX_ITERATIONS = 100

def muellers(f, p0, p1, p2, TOL):
    iterations = 3
    error = 1
    print(f'Iteration\t\tPi')
    while error > TOL and iterations < MAX_ITERATIONS:

        h1 = p1-p0
        h2 = p2-p1
        del1 = (f(p1)-f(p0))/h1
        del2 = (f(p2)-f(p1))/h2
        d = (del2-del1)/(h2+h1)
        c = f(p2)

        b = del2 + h2*d
        discriminant = (b*b - 4*c*d)**0.5

        E = b+discriminant if abs(b-discriminant) < abs(b+discriminant) else b-discriminant

        proximity = -2*c/E
        p = p2+proximity

        print(f'{iterations:^5}\t\t{p:.5f}')

        error = abs(proximity)

        p0 = p1
        p1 = p2
        p2 = p
        iterations += 1

    print("Incorrect initial points. Try again." if iterations > MAX_ITERATIONS else "Exiting...")

if __name__ == '__main__':
    #f = lambda x: x**4 + 2*x**2 - x - 3
    f = lambda x: x**5 - x**4 + 2*x**3 - 3*x**2 + x - 4
    muellers(f, 1, 0, -1, 1e-5)
