

def longest_subarray_with_distinct_entries(paragraph):
    arr = []
    max_seen = 0
    for char in paragraph:
        if char not in arr:
            arr.append(char)
            max_seen = max(max_seen, len(arr))
        elif char in arr:
            arr = arr[arr.index(char):]
    return max_seen

l = ['f','s','f','e','t','w','e','n','w','e']
print(longest_subarray_with_distinct_entries(l))

def longest_subarray_with_distinct_entries2(paragraph):
    most_recent_occurrence = {}
    longest_subarray_start_id = 0
    result = 0
    for i, char in enumerate(paragraph):
        if char in most_recent_occurrence:
            if most_recent_occurrence[char] >= longest_subarray_start_id:
                result = max(result, i - longest_subarray_start_id)
                longest_subarray_start_id = most_recent_occurrence[char] + 1
        most_recent_occurrence[char] = i
    return max(result, len(paragraph) - longest_subarray_start_id)

l = ['f','s','f','e','t','w','e','n']
print(longest_subarray_with_distinct_entries2(l))