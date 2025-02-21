# # Dictionary person
# person = {"Name":"John","Age":30,"City":"New York"}

# #person name
# print(person["Name"])

# ## Add country USA
# person["Country"]="USA"
# print(person)

# #update the age
# person["Age"] = 31
# print(person)

##Dictionary Methods
fruits = {"apple": 50, "banana": 20, "cherry": 30, "date": 40}

print(fruits.keys())
print(fruits.values())


for key, value in fruits.items():
    print(f"{key}: {value}")


fruits["mango"]=60
print(fruits)

fruits.pop("banana")
print(fruits)