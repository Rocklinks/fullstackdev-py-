# Tuples

movies = ("Baaghi3","Golmal Again", "Singham Again","Stree2")
print(len(movies))
print(type(movies))
print(movies[1])

#Set

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
set3 = set1.intersection(set2)
print(set3)


# Set and tuple conversion
fruits = ["apple","mango","gauva","mango","oranges","jack fruit","mango"]
fruitst = tuple(fruits)
print(fruitst)
fruitsset = set(fruitst)
print(fruitsset)