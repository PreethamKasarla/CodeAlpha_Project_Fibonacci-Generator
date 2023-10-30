def fibonacci_generator(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    return fibonacci_sequence


n = int(input(" Enter value:"))
fibonacci_sequence = fibonacci_generator(n)
print("\n", f"The first {n} Fibonacci numbers are: ", *fibonacci_sequence)