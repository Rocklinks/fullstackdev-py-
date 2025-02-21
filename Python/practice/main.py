#Day3
# a =3
# print(a)

# b=4
# pi=3.14
# st = "Hello Python"
# bool = True

# print(f"The type of b is {type(b)}, the type of pi is {type(pi)}, th type of st is {type(st)} and the type of bool is {type(bool)}")


# l =[5,8,3,7,9]
# print(f"The first element is {l[0]} and the last element is {l[4]}")

# dict = {"Name": "Rama", "Class":"11th","Grade":"A"}
# print(dict["Grade"])


# str ="123476765"
# str_toint =int(str)
# print(str_toint)

#Day4
# list1 = [5,8,4,9]
# list1.append(3)

# print(list1)
# list1.remove(8)
# print(list1)

# l = ["Answer",45.6,0,["Caldwell"]]
# print(l[0])
# print(l[3])

# sl=["Caldwell"]
# if sl in l:
#     print(f"The {sl} is substring of {l}")

#Day5
# tup1 = (1,5,845 ,45)
# tup2 = (4,6,3,8,4)
# tup3 = tup1 + tup2
# print(tup3)

# set1 = {23,56,7,5,6}
# set2 = {5,7,32,65,8}
# s3=set1.intersection(set2)
# print(s3)
# print(set1.union(set2))

#Day 6
dict = {"Name": "Rama", "Class":"11th","Grade":"A"}
for key,values in dict.items():
    print(f"{key}:{values}")
dict["Name"]="Rajesh"
for key,values in dict.items():
    print(f"{key}:{values}")
