# ## File Read
with open('homework.txt', 'r') as file:
    print(file.read())


#File write
with open('output.txt', "w") as file:
    content = "Hello, World!\nWelcome to File Handling in Python."
    file.write(content)

with open("output.txt", "r") as file:
    text=file.read()
    word_count = len(text.split())
    print("Total word count:", word_count)