def Fibonacci(x):
    a = 0
    b = 1

    while b < x:
        print(b)  # Print the Fibonacci number

        temp = b  # Store old 'b' before updating
        b = a + b  # Update Fibonacci number
        a = temp  # Move 'a' to previous 'b'


# Example usage
x = 10
Fibonacci(x)