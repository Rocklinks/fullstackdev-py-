#File operations

#r- Read the File
#w - Write to the file
#a - append to the file
#/n for writing it in a new line

#File write
def create_file(filename, content=""):
    with open(filename, "w") as file:
        file.write(content)

content = """Hello, this is a file handling assignment.
Python makes it easy to work with files."""
create_file("myfile.txt", content)


## File Read
def read_file(filename):
    with open(filename,"r") as file:
        return file.read()
print(read_file('myfile.txt'))


#Append line and read
def write_to_file(filename,content):
    with open(filename,'a') as file:
        file.write('\n'+content)

content="This is an appended line"
write_to_file('myfile.txt',content)

def read_file(filename):
    with open(filename,"r") as file:
        return file.read()
print(read_file('myfile.txt'))


with open("myfile.txt", "r") as file:
    text = file.read()
    word_count = len(text.split())

print("Total word count:", word_count)


## Copy file to new file
# Read content from myfile.txt
with open("myfile.txt", "r") as source_file:
    content = source_file.read()

# Write the content to copy.txt
with open("copy.txt", "w") as destination_file:
    destination_file.write(content)

# Verify if both files have the same content
with open("copy.txt", "r") as copied_file:
    copied_content = copied_file.read()

if content == copied_content:
    print("Verification successful: copy.txt contains the same content as myfile.txt")
else:
    print("Verification failed: copy.txt content does not match myfile.txt")

