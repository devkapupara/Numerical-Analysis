import math

"""
Chebyshev's Polynomial
f(x) = 1/(1+25x^2)
The standard interval is [-1, 1]
Transforming it to our interval, we get x = z using x = 1/2[(b-a)z + (b+a)]
"""
def chebyshev_coefficients(f, n):
    nodes = [math.cos(((2*i-1)/(2*n))*math.pi) for i in range(1,n+1)]
    y = [f(i) for i in nodes]
    print('i\t\tNode\t\t\tf(x)')
    for i in range(n):
        print(f'{i}\t\t{nodes[i]:.5f}\t\t{y[i]:.5f}')
    diff = 1
    final = []
    for i in range(len(nodes)):
        final.append(y[0])
        newy = []
        for j in range(1, len(y)):
            newy.append((y[j]-y[j-1])/(nodes[i+j]-nodes[i+j-diff]))
        y = newy
        diff += 1
    print("#"*50)
    print("Chebyshev's Coefficient:")
    for i in range(len(final)):
        print(f'a{i} = {final[i]:0.5f}')
    func = f'{final[0]}'
    x_coeff = ''
    nodes[len(nodes)//2] = 0
    print("#"*50)
    for i in range(1, len(final)):
        if nodes[i-1] != 0:
            x_coeff += f"(x{' - ' if nodes[i-1] > 0 else ' + '}{abs(nodes[i-1])})"
        else:
            x_coeff += "(x)"
        func += f"{' + '  if final[i] > 0 else ' - '}{abs(final[i])}{x_coeff}"
    print("P(x) = %s" % func)

if __name__ == "__main__":
    f = lambda x: 1/(1+25*x**2)
    n = 11
    chebyshev_coefficients(f, n)