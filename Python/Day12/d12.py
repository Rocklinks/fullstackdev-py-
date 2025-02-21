#File write
with open('myfile.txt', "w") as file:
    content = """Hello, World!
Welcome to File Handling in Python."""
    file.write(content)

# ## File Read
with open('myfile.txt', 'r') as file:
    print(file.read())


# #Append the content
with open('myfile.txt', 'a') as file:
    file.write('This is an appended line')


with open('myfile.txt',"r") as file:
    print(file.read())

file =open("myfile.txt", "r")
text = file.read()
word_count = len(text.split())
print("Total word count:", word_count)

# ## Copy file to new file
with open("myfile.txt", "r") as source_file:
    content = source_file.read()

# # Write the content to copy.txt
with open("copy.txt", "w") as destination_file:
    destination_file.write(content)

# # Verify if both files have the same content
with open("copy.txt", "r") as copied_file:
    copied_content = copied_file.read()

if content == copied_content:
    print("Verification successful: copy.txt contains the same content as myfile.txt")
else:
    print("Verification failed: copy.txt content does not match myfile.txt")

