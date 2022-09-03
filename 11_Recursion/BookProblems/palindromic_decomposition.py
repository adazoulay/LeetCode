
# Book solution
def palindrome_decomposition(input):
    def directed_palindrome_decomposition(offset, partial_partition):
        if offset == len(input):
            result.append(list(partial_partition))
            return

        for i in range(offset + 1, len(input) + 1):
            prefix = input[offset:i]
            if prefix == prefix[::-1]:
                directed_palindrome_decomposition(i, partial_partition + [prefix])
    result = []
    directed_palindrome_decomposition(0, [])
    return result

print(palindrome_decomposition("racecar"))


# Pythonic book solution
def palindrome_decompositions_pythonic(text):
    return ([[text[:i]] + right for i in range(1, len(text) + 1)
            if text[:i] == text[:i][::-1]
            for right in palindrome_decomposition(text[i:])] or [[]])

print(palindrome_decompositions_pythonic("racecar"))

# Long sol
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return False
    return True

def printSubArrays(arr, start, end, result):
    if end == len(arr):
        return
    elif start > end:
        printSubArrays(arr, 0, end + 1, result)
    else:
        if len(arr[start:end + 1]) >= 2 and is_palindrome(arr[start:end + 1]):
            result.append(arr[start:end + 1])
        printSubArrays(arr, start + 1, end, result)

r = []
printSubArrays('racecar',0,0, r)
print(r)


