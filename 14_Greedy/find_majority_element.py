
arr = [2,1,3,1,1,2,1,1,3,1]

def majority_search(input_stream):
    candidate, candidate_count = None, 0
    for num in input_stream:
        if candidate_count == 0:
            candidate, candidate_count = num, candidate_count + 1
        elif num == candidate:
            num += 1
        else:
            candidate_count -= 1
    return candidate


print(majority_search(arr))