#Q1
# list = [1,4,5,8,5,9,1,2,3]
# a=[]
# for i in list:
#     if i not in a:
#         a.append(i)
# print(a)

#Q2
# mlist = [4,5,7,6,8,3]

# for i in range(len(mlist)-1):
#     for j in range(i+1):
#         if i>j:
#             continue
# print(mlist[i])

#Q3

# string ="welcome to aiepoch technologies python fullstack development course"
# ch = "co"
            ##method1
# count =0
# for char in string:
#     if char == ch:
#         count+=1
# print(count)

            ##method2
# count =string.count(ch)
# print(count)

#Q4
# words = ["one..two.three", ".four.five.", "six.."]
# separator = "."
# c=[]
# for word in words:
#     a=word.split(separator)
#     for i in a:
#         if i!="":
#             c.append(i)
# print(c)

#Q5
# sentence = input("Enter Sentences: ")
# words = sentence.lower().split()
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word]+=1
#     else:
#         word_count[word]=1

# for word,count in word_count.items():
#     print(f"{word}:{count}")


#Q6
# words = input("Enter some words: ").lower().split()
# a=[]
# for word in words:
#     if len(word)>5:
#         a.append(word)
# print(a)

#Q7
# n =int(input("Enter a number; "))
# for i in range(1,11):
#     a=n*i
#     print(f"{n}x{i} = {a}")


#Q8

sentence =input("Enter Sentences: ").lower()
count = 0
word = False
for char in sentence:
    if char.isalnum():
        if not word:
            count +=1
            word=True
    else:
        word = False
print(f"Number of words in sentences:  {count}")
