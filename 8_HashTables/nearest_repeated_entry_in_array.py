

def find_nearest_repetition(paragraph):
    words = dict()
    for index, word in enumerate(paragraph):
        if word not in words:
            words[word] = [index]
        else:
            words[word].append(index)
    minimum = [0,len(paragraph)]
    for word in words.values():
        for index1, index2 in zip(word, word[1:]):
            if index2 - index1 < minimum[1] - minimum[0]:
                minimum = index1, index2
    return minimum

l = ["all","work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]
print(find_nearest_repetition(l))