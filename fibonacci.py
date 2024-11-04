#A sequence of numbers where each number is the sum of the two numbers that come before it
# example 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
# Write a function fibonacci(n) that generates a list containing the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    fib_sequence = []
    for i in range (n):
        if i == 0:
            fib_sequence.append(0)
        elif i == 1:
            fib_sequence.append(1)
        else:
           next_fib = fib_sequence[i-1] + fib_sequence[i-2]
           fib_sequence.append(next_fib)

    return fib_sequence

result= fibonacci(10)
print(result)

result= fibonacci(100)
print(result)

