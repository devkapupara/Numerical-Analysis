from rref import reduced_row_echelon_form as rref
from math import *

"""
For a Natural Cubic Spline, the system of equations are solved using Ax = b
To get an idea how to form the A and b matrices, please refer to page 146 of Numerical-Analysis, 10th Edition.
"""

def natural_spline(x, y, choice):
	n = len(x)
	h = [x[i+1] - x[i] for i in range(n-1)]
	A = [0] * n 															# first row in A is [1, 0, 0, ...]
	A[0] = [0]*(n+1)
	A[0][0] = 1
	A[n-1] = [0] * (n+1)
	A[n-1][n-1] = 1															# Last row in A is [0, 0, 0, ......, 1]
	A[n-1][n] = 0
	idx = 0
	for i in range(1,n-1):
		a = [0] * (n+1)
		a[idx] = h[i-1]
		a[idx+1] = 2*(h[i-1] + h[i])
		a[idx+2] = h[i]
		a[n] = 3*((y[i+1]-y[i])/h[i] - (y[i]-y[i-1])/h[i-1])
		idx += 1
		A[i] = a
	reduced = rref(A)														# Reduce the augmented matrix A|b to get the c in the last column
	b = [0] * (n-1)
	c = [0] * (n-1)
	d = [0] * (n-1)
	for i in range(n-1):
		c[i] = reduced[i][-1]
		c2 = reduced[i+1][-1]
		b[i] = (y[i+1]-y[i])/h[i] - h[i]/3*(c2 + 2*c[i])					# Compute b and d
		d[i] = (c2-c[i])/(3*h[i])

	if choice == 2:
		return [y[:3], b, c, d]

	for i in range(n-1):													# Print out each equation if requested.
		factor = f"(x{')' if x[i] == 0 else f' - {x[i]:.2f})' }"
		print(f"S_{i}(x) = ", end='')
		if y[i] != 0:
			if y[i] < 0:
				print("-", end ='')
			print("%5.4f" % abs(y[i]), end = ' ')
		if b[i] != 0:
			print("-" if b[i] < 0 else "+", end =' ')
			print("%5.4f%s" % (abs(b[i]), factor), end = ' ')
		if c[i] != 0:
			print("-" if c[i] < 0 else "+", end =' ')
			print("%5.4f%s^2" % (abs(c[i]), factor), end = ' ')
		if d[i] != 0:
			print("-" if d[i] < 0 else "+", end =' ')
			print("%5.4f%s^3" % (abs(d[i]), factor))


if __name__ == '__main__':
	n = int(input("How many points to interpolate? "))
	choice = int(input("1) Display Equations\n2) Get Coefficients a,b,c,d\n"))
	x = [0] * n
	y = x.copy()
	print("Enter x,y one at a time")
	for i in range(n):
		data = input().split(",")
		x[i], y[i] = float(data[0]),float(data[1])
	natural_spline(x, y, choice)