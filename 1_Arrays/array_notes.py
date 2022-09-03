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

#key methods and SEARCH SEARCH SEARCH
5 in x   #returns weather 5 is found in x
x.index(42)  #returns the index at which 42 is found


# Optional key parameter
min(x)  #returns min element
max(x)  #returms amx element
l = ["ab", "abc", "bc", "c"]
#print(max(l, lambda p: len(p)))


# bisect(list, num, beg, end)
bisect.bisect(x, 6)  #returns the index in the sorted list, where the number passed in argument can be placed to maintain the resultant list in sorted order.
bisect.bisect_left(x, 6)  #if element already in list, returns the rightmost position
bisect.bisect_right(x, 6)  #4 arguments: list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.

x.reverse()  #in-place (mutates)
reversed(x)  #returns an iterator
x.sort()  #in-place (mutates)  n log n
sorted(x)  #returns a copy

i, j = 0, 5
del x[i]  #deletes the i-th element
del x[i:j]  #removes the slice

#2D arrays:
x = [[1,2,3], [2,3,4], [2]]
print(x)

