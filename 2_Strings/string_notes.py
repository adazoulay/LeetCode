def is_palindromic(s):
    # Note that s[~i] for i in [0, len(s) - 1] is s[-(i + 1)].
    return all(s[i] == s[~i] for i in range(len(s) // 2))


# Iterate from right to left and left to right using ~ instead of i, avoids out of bounds
def test(x):
    for i in range(len(x)):
        print(i, ~i)
        print(x[i], x[~i])


#  !!!! STRINGS ARE IMMUTABLE !!!!!

s = "Hello World"
t = "test"

# access
x = s[3]
x = s[2:4]

# concat
x = s + t

# delete
x = s.strip()  # removes characters in args, removes space by default

# check if contains, returns boool
x = s in t
x = s.startswith("Hello")
x = s.endswith("World")

# split
x = 'Euclid,Axiom 5,Parallel Lines'.split(',')  # returns array

# duplicate
x = 3 * '01'

#upper lower
x = s.lower()
x = s.upper()

# Since strings are immutable:
# Concatenating a single character n times has O(n^2) complexity
