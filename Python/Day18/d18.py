celsius_to_fahrenheit = lambda c: (c * 9/5) + 32

print(f" The frahrein for the 25 celcius is {celsius_to_fahrenheit(25)}\u00b0F")


words = ["apple", "banana", "grape", "kiwi", "mango", "orange"]
long_words = [word for word in words if len(word) <= 5]
print(long_words)

