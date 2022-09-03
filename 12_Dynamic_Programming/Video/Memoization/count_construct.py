# m = len(target), n = len(wordbank)

# O(m*n^m) time, O(m^2) space
def countConstruct(target, wordBank):
    if target == '':
        return 1
    total_count = 0
    for word in wordBank:
        if target.find(word) == 0:
            num_ways = countConstruct(target[len(word):], wordBank)
            total_count += num_ways

    return total_count

# O(n*m^2) time, O(m^2) space
def countConstruct2(target, wordBank, memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    total_count = 0
    for word in wordBank:
        if target.find(word) == 0:
            num_ways = countConstruct(target[len(word):], wordBank)
            total_count += num_ways

    memo[target] = total_count
    return total_count

