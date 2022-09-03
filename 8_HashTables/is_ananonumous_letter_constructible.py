import collections


def is_anonimous_letter_constructible(text, magazine):
    letters = {}
    for c in text:
        if c not in letters:
            letters[c] = 0
        letters[c] -= 1
    for c in magazine:
        if c in letters:
            letters[c] += 1
    return all(i >= 0 for i in letters.values())



def is_letter_constructible_from_magazine_pythonic(text, magazine):
    x = collections.Counter(text) - collections.Counter(magazine)
    print(x)
    return not collections.Counter(text) - collections.Counter(magazine)

text = "abc"
magazine = "abcd"
print(is_letter_constructible_from_magazine_pythonic(text, magazine))