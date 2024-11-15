def numerical_integration(f, a, b, N):
    dx = (b - a) / N
    total_area = 0

    for i in range(N):
        x = a + i * dx
        total_area += f(x) * dx

    return total_area

def example_function(x):
    return x**2 + 1  

a = -2  # Lower limit
b = 2   # Upper limit
N = 100  # Number of intervals

integral_value = numerical_integration(example_function, a, b, N)
print(f"The approximate value of the integral is: {integral_value}")
