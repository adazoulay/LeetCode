
# m = len(target), n = len(wordbank)

#Brute force
# O(m*n^m) time, O(m^2) space
def all_construct(target, wordBank):
    if target == '':
        return [[]]
    result = []
    for word in wordBank:
        if target.find(word) == 0:
            suffix_ways = all_construct(target[len(word):], wordBank)
            target_ways = list(map(lambda x: [word] + x, suffix_ways))
            result.append(target_ways)

    return result

bank = ['purp', 'purpl','l','e']

print(all_construct('purple',bank))

# Memoized
# O(n^m) time, O(m) space
def all_construct2(target, wordBank, memo={}):
    if target in memo:
        return memo
    if target == '':
        return [[]]

    result = []

    for word in wordBank:
        if target.find(word) == 0:
            suffix_ways = all_construct2(target[len(word):], wordBank)
            target_ways = list(map(lambda x: [word] + x, suffix_ways))
            result.append(target_ways)

    memo[target] = result
    return result