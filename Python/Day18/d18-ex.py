#Double using lambda
num=[1, 2, 3, 4, 5]
double = list(map(lambda x:x*2,num))
print(double)

#List comprehension
num = [1,2,3,4,5,6,7,8,9]
odd=[i for i in num if i%2!=0]
print(odd)

people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sort = sorted(people,key=lambda x:x[0])
print(sort)