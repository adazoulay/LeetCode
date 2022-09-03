# Check all elements in list
li = [1,2,3,4,5]
all(li[i] > 0 for i in range(len(li) // 2))

# Lambda function

#EX1
ex1 = lambda a, b, c: a + b + c
print('ex1', ex1(5, 6, 2))

#EX2
tables = [lambda x=x: x * 10 for x in range(1, 11)]

#for table in tables:
#    print(table())

#EX3
List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
sortList = lambda x: (sorted(i) for i in x)   # Lambda 1 used as arg in Lambda 2
secondLargest = lambda x, f: [y[len(y) - 2] for y in f(x)]
res = secondLargest(List, sortList)
print(res)


#FILTER: Takes in two arguments filter(function, list)
# Returns elements that satisfy input condition, does not mutate original list
# In this case the function is a lambda
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print('Ex1', final_list)

ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print('Ex2', adults)

# MAP: takes in two arguments function and list
# returns the altered elements in list but does not mutate original array
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x * 2, li))
print(final_list)

animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
print(uppered_animals)

# REDUCE: takes two arguments function and list
# OPTIONAL third parameter is initializer/starting value, default is None but can be set ex 0
# New reduced result is returned, always returns a single element
# Belongs to functools module
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
total = reduce((lambda x, y: x + y), li)
print(total)

li = ["hi", "there", "i'm", "Adam"]
total = reduce((lambda x, y: x + " " + y), li)
print(total)

lis = [1, 3, 5, 6, 2,]
maxNumber = reduce(lambda a,b: a if a > b else b, lis)
print(maxNumber)