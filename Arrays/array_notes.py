import bisect

#instantiating arrays:
x = [1,2,3,5]
print(x)

x = [1] + [0] * 10
print(x)

x = list(range(100))
print(x)


#basic operations
len(x)
x.append(42)  #can also take in an array as param. Adds to end
x.remove(2)  #Delete the element that has the value 2:
x.insert(3, 28)  #inserts an element to the list at the specified index.

#key methods
min(x)
max(x)

bisect.bisect(x, 6)
bisect.bisect_left(x, 6)
bisect.bisect_right(x, 6)

x.reverse()  #in-place (mutates)
reversed(x)  #returns an iterator
x.sort()  #in-place (mutates)
sorted(x)  #returns a copy
del A[i]  #deletes the i-th element
del A[i:j]  #removes the slice

#2D arrays:
x = [[1,2,3], [2,3,4], [2]]
print(x)

