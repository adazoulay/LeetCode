def longest_contained_range(A):
    unprocessed_entries = set(A)
    max_interval_size = 0

    while unprocessed_entries:
        a = unprocessed_entries.pop()
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1
        max_interval_size = max(max_interval_size, upper_bound - lower_bound - 1)
    return max_interval_size

l = [10,5,3,11,6,100,4]

print(longest_contained_range(l))