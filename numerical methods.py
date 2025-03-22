import math

# Function to evaluate f(x)
def f(x):
    return x**3 - 4*x - 9  # Example function (Modify as needed)

# 1️⃣ Bisection Method
def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. Choose different initial values.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2  # Midpoint
        if abs(f(c)) < tol:  # Root found
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

# 2️⃣ Newton-Raphson Method
def derivative_f(x):
    return 3*x**2 - 4  # Derivative of f(x)

def newton_raphson(x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fx = f(x0)
        dfx = derivative_f(x0)
        if dfx == 0:
            print("Zero derivative. No solution found.")
            return None
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

# 3️⃣ Trapezoidal Rule (Numerical Integration)
def trapezoidal_rule(a, b, n=100):
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2
    for i in range(1, n):
        integral += f(a + i * h)
    return integral * h

# 4️⃣ Simpson’s Rule (Numerical Integration)
def simpsons_rule(a, b, n=100):
    if n % 2 == 1:
        n += 1  # Ensure even n
    h = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        integral += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        integral += 2 * f(a + i * h)
    return integral * h / 3

# Main menu
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Bisection Method (Root Finding)")
        print("2. Newton-Raphson Method (Root Finding)")
        print("3. Trapezoidal Rule (Numerical Integration)")
        print("4. Simpson’s Rule (Numerical Integration)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':  # Bisection Method
            a = float(input("Enter lower bound: "))
            b = float(input("Enter upper bound: "))
            result = bisection(a, b)
            print(f"Root found: {result}")

        elif choice == '2':  # Newton-Raphson Method
            x0 = float(input("Enter initial guess: "))
            result = newton_raphson(x0)
            print(f"Root found: {result}")

        elif choice == '3':  # Trapezoidal Rule
            a = float(input("Enter lower limit: "))
            b = float(input("Enter upper limit: "))
            result = trapezoidal_rule(a, b)
            print(f"Approximate integral: {result}")

        elif choice == '4':  # Simpson's Rule
            a = float(input("Enter lower limit: "))
            b = float(input("Enter upper limit: "))
            result = simpsons_rule(a, b)
            print(f"Approximate integral: {result}")

        elif choice == '5':  # Exit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
