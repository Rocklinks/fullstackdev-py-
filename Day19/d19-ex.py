# Task1 Multiple Decorators
import time
import functools

def log_function_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def time_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

@log_function_name
@time_execution
def sum_numbers(n):
    return sum(range(1, n + 1))

print(sum_numbers(1000000))


class EvenNumbers:
    def __init__(self, n):
        self.n = n  # Upper limit
        self.current = 0  # Start from 0

    def __iter__(self):
        return self  # The class itself is the iterator

    def __next__(self):
        if self.current > self.n:
            raise StopIteration  # Stop when exceeding n
        even_number = self.current
        self.current += 2  # Move to the next even number
        return even_number

# Example Usage:
evans = EvenNumbers(10)
for num in evans:
    print(num)
