
def find_smallest_sequentially_covering_subset(paragraph, keywords):
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}
    latest_occurence = [-1] * len(keywords)
    min_interval = (-1, -1)
    for index, word in enumerate(paragraph):
        if word in keywords:
            if all(x < index for x in latest_occurence[:keyword_to_idx[word]]):
                latest_occurence[keyword_to_idx[word]] = index
        if all(x != -1 for x in latest_occurence):
            if min_interval[1] - min_interval[0] < max(latest_occurence) - min(latest_occurence):
                min_interval = (min(latest_occurence), max(latest_occurence))
    return min_interval

l = ["apple", "banana", "cat", "apple","banana","apple"]
words = ["banana", "apple"]
print(find_smallest_sequentially_covering_subset(l, words))

# Book solution:
def find_smallest_sequentially_covering_subset2(paragraph, keywords):
    keyword_to_idx = {k: i for i, k in enumerate(keywords)}
    latest_occurrence = [-1] * len(keywords)
    shortest_subarray_length = [float('inf')] * len(keywords)
    shortest_distance = float('inf')
    result = (-1, -1)

    for i, char in enumerate(paragraph):
        if char in keyword_to_idx:
            keyword_idx = keyword_to_idx[char]
            if keyword_idx == 0:
                shortest_subarray_length[keyword_idx] = 1
            elif shortest_subarray_length[keyword_idx - 1] != float('inf'):
                distance_to_previous_keyword = (i - latest_occurrence[keyword_idx - 1])
                shortest_subarray_length[keyword_idx] = distance_to_previous_keyword + shortest_subarray_length[keyword_idx - 1]
                latest_occurrence[keyword_idx] = i
            if keyword_idx == len(keywords) - 1 and shortest_subarray_length[-1] < shortest_distance:
                shortest_distance = shortest_subarray_length[-1]
                result = (i - shortest_distance + 1, i)
    return result

