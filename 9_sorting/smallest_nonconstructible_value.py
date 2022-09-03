import collections


def smallest_change(coins):
    sum = 0
    for a in coins:
        if a > sum + 1:
            break
        sum += a
    return sum + 1








l = [1,1,1,1,1,5,10,25]
print(smallest_change(l))