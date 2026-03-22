def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def main():
    print("Simple Command Line Calculator")
    print("Operation: Addition (+)")
    print("-" * 30)

    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = add(a, b)
        print(f"Result: {a} + {b} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    main()
