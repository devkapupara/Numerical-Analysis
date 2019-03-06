# Numerical Analysis Package

### This repository contains the Python implementation of the following method:

####Please do note that your f(x) needs to be defined in the main part of the program. You will also need to specify the Tolerance level. Input handling hasn't been implemented yet.

<ol>
  <li>Finding the roots of a polynomial:
    <ul>
      <li><strong>Bisection Method</strong>: Used to find the roots of a polynomial. Guaranteed to converge.</li>
      <li><strong>Fixed Poin</strong>t Iteration: x = g(x)</li>
      <li><strong>Newton-Raphson</strong>: The fastest converging method, with an order of 2. Need extra computation for the derivative and might fail when f'(x) = 0. Also added the modified Newton's method that uses the second derivative for computations, thereby possibly reducing the iterations needed for convergence.</li>
      <li><strong>Secant Method</strong>: Uses the same methodology of Newton's method, but without the need of calculating the derivative. Needs two point for manual slope calculation.</li>
      <li><strong>Müeller's Method</strong>: Faster than Secant method, slower than Newton's. The benefit of using this method is that it can find Complex Roots without the need of a derivative. But in order to do so, we need to have an idea of the curve on which our root lies and needs three points so it can plot a parabola passing through it.</li>
    </ul>
  <li> Accelerating techniques:
    <ul>
      <li><strong>Aitken's Method</strong>: His method speeds up the convergence of any of the above methods by calculating 𝝙 after we have 3 points.</li>
      <li><strong>Steffensen's Method</strong>: A combination of Fixed-Point Iteration and the accelration of Aitken's Method. Compute three points using Fixed-Point and apply Aitken's on those three to get another point. Then again perform Fixed-Point Iteration on it and profit.</li>
    </ul>
  </li>
</ol

