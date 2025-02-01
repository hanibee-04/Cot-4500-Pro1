# src/main/coding assignment_1.py
#__init__.py
def approximate_sqrt2(tol=1e-6, x0=1.5):
    
    iter_count = 0
    x = x0
    print(f"{iter_count}: {x}")

    while True:
        iter_count += 1
        y = x
        x = (x / 2) + (1 / x)

        print(f"{iter_count}: {x}")

        if abs(x - y) < tol:
            break

    print(f"Convergence after {iter_count} iterations")
    return x


def bisection_method(f, left, right, tol=1e-6, max_iter=100):

    if f(left) * f(right) >= 0:
        print("Invalid interval: f(left) and f(right) must have opposite signs.")
        return None

    iter_count = 0
    while abs(right - left) > tol and iter_count < max_iter:
        iter_count += 1
        midpoint = (left + right) / 2

        if f(left) * f(midpoint) < 0:
            right = midpoint
        else:
            left = midpoint

        print(f"Iteration {iter_count}: x = {midpoint}")

    print(f"Convergence after {iter_count} iterations")
    return midpoint


def fixed_point_iteration(g, p0, tol=1e-6, max_iter=100):
    
    iter_count = 0

    while iter_count < max_iter:
        iter_count += 1
        p = g(p0)

        print(f"Iteration {iter_count}: x = {p}")

        if abs(p - p0) < tol:
            print("SUCCESS")
            return p

        p0 = p

    print("FAILURE")
    return None


def newton_raphson(f, df, p0, tol=1e-6, max_iter=100):
   
    iter_count = 0

    while iter_count < max_iter:
        iter_count += 1

        if df(p0) == 0:
            print("Derivative is zero, method fails.")
            return None

        p = p0 - f(p0) / df(p0)
        print(f"Iteration {iter_count}: x = {p}")

        if abs(p - p0) < tol:
            print("SUCCESS")
            return p

        p0 = p

    print("FAILURE")
    return None


#now print all tests out

if __name__ == "__main__":
    print("### Approximation Algorithm (√2) ###")
    approximate_sqrt2()

    print("\n### Bisection Method (Finding √2) ###")
    bisection_method(lambda x: x**2 - 2, 1, 2)

    print("\n### Fixed-Point Iteration (√2 Approximation) ###")
    fixed_point_iteration(lambda x: (x / 2) + (1 / x), 1.5)

    print("\n### Newton-Raphson Method (Finding √2) ###")
    newton_raphson(lambda x: x**2 - 2, lambda x: 2*x, 1.5)





#init__.py section of code
# src/test/test_assignment_1.py
import unittest
from src.main.assignment_1 import approximate_sqrt2, bisection_method, fixed_point_iteration, newton_raphson

class TestNumericalMethods(unittest.TestCase):

    def test_approximate_sqrt2(self):
        result = approximate_sqrt2()
        self.assertAlmostEqual(result, 1.414213562373095, places=6)

    def test_bisection_method(self):
        result = bisection_method(lambda x: x**2 - 2, 1, 2)
        self.assertAlmostEqual(result, 1.414213562373095, places=6)

    def test_fixed_point_iteration(self):
        result = fixed_point_iteration(lambda x: (x / 2) + (1 / x), 1.5)
        self.assertAlmostEqual(result, 1.414213562373095, places=6)

    def test_newton_raphson(self):
        result = newton_raphson(lambda x: x**2 - 2, lambda x: 2*x, 1.5)
        self.assertAlmostEqual(result, 1.414213562373095, places=6)

if __name__ == "__main__":
    unittest.main()
