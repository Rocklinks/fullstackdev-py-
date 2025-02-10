# ## File Read
with open('homework.txt', 'r') as file:
    print(file.read())


#File write
with open('output.txt', "w") as file:
    content = "Hello, World!\nWelcome to File Handling in Python."
    file.write(content)

#Word Count
with open("output.txt", "r") as file:
    text=file.read()
    word_count = len(text.split())
    print("Total word count:", word_count)

#Append
with open('notes.txt', 'a') as file:
    file.write('This is an appended line')

# ## Copy file to new file
with open("source.txt", "r") as source_file:
    content = source_file.read()

# # Write the content to copy.txt
with open("destination.txt", "w") as destination_file:
    destination_file.write(content)