# 1.Concatenated first two strings
a,b,c = input("Enter 3 Strings: ").split()
concatenated = f"{a} + {b}"
print(concatenated)

sliced = concatenated[2:8]
print(f"{sliced}")



#2. case Conversion

name  = input("Enter name: ")
nameu = name.upper()
print(nameu)
namel = name.lower()
print(namel)
nameswap = name.swapcase()
print(nameswap)

print(name.istitle())


#3) replace

sentence =input("Enter a sentences: ")
modified_sentence =sentence.replace("Pytho", "Java")

print(f"Original Sentence is {sentence}")
print(f"Modified Sentence is {modified_sentence}")


# Count program
ch = input("Enter characters: ")
def analyze(ch): 
    vowels = 'aeiou'
    vowels_count = 0
    consonants_count = 0
    space_count = 0
    for i in ch:
        if i.isspace():
            space_count +=1
            # print(f"The Space Count is {space_count}")
        elif i in vowels:
            vowels_count +=1
            # print(f"The vowels count is{vowels_count}")
        elif i.isalpha():
            consonants_count +=1
            # print(f"Consonants count is {consonants_count}")
    return space_count,vowels_count,consonants_count

space_count,vowels_count,consonants_count = analyze(ch)

print(f"Total Vowels Count is {vowels_count}")
print(f"Total Consonants is {consonants_count}")
print(f"Total Space count is {space_count}")

