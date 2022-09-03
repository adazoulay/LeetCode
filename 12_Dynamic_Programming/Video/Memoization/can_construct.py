# canConstruct(target, wordBank) accepts a target string and an array of strings
# Returns a boolean  if target can be constructed by concatenating elements of the wordbank array

# m = len(target), n = len(wordbank)

# Brute Force
# O(m*n^m) time, O(m^2) space
def canConstruct(target, wordBank):
    if target == '':
        return True

    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank):
                return True
    return False

# Memoized
# O(n*m^2) time, O(m^2) space
def canConstruct2(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in wordBank:
        if target.find(word) == 0:
            suffix = target[len(word):]
            if canConstruct(suffix, wordBank):
                memo[target] = True
                return True
    memo[target] = False
    return False

print(canConstruct2('abcdef',['ab','abc','cd','def','abcd']))