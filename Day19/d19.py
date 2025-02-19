import time

def calc_factorials(numbers):
    start = time.time()
    result = []

    def fact(n):  # nested function for single value factorial
        if n == 0 or n == 1:
            return 1
        return n * fact(n - 1)

    for num in numbers:
        result.append(fact(num))

    end = time.time()
    print(f"Factorial calculation took {end - start:.6f} seconds")

    return result

l1 = 1
l2 = 10 
lst = range(l1, l2)

print(calc_factorials(lst))



# class EvenNumbers:
#     def __init__(self, n):
#         self.n = n  # Upper limit
#         self.current = 0  # Start from 0

#     def __iter__(self):
#         return self  # The class itself is the iterator

#     def __next__(self):
#         if self.current > self.n:
#             raise StopIteration  # Stop when exceeding n
#         even_number = self.current
#         self.current += 2  # Move to the next even number
#         return even_number

# # Example Usage:
# evans = EvenNumbers(10)
# for num in evans:
#     print(num)
