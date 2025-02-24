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
sentence = input("Enter Sentences: ")
words = sentence.split()
word_count = {}

for word in words:
    word = word.lower()
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

for word,count in word_count.items():
    print(f"{word}:{count}")