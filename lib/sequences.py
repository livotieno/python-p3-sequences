#!/usr/bin/env python3

def print_fibonacci(length):
    pass
fibonacci = [0,1]

while len(fibonacci) < length:
    new_number = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(new_number)
print(fibonacci)

print_fibonacci(9)
