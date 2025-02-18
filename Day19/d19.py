import time

def execution_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs) 
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return result
    return wrapper

@execution_timer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))


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
