import collections

def compute_all_string_decomposition(s, words):
    def match_all_words_in_dict(start):
        curr_string_to_freq = collections.Counter()
        for i in range(start, start + len(words) * unit_size, unit_size):
            curr_word = s[i:i + unit_size]
            it = word_to_feq[curr_word]
            if it == 0:
                return False
            curr_string_to_freq[curr_word] += 1
            if curr_string_to_freq[curr_word] > it:
                return False
        return True

    word_to_feq = collections.Counter(words)
    unit_size = len(words[0])
    return [i for i in range(len(s) - unit_size * len(words) + 1) if match_all_words_in_dict(i)]

word = "amanaplanacanal"
l = ["can","apl","ana"]
print(compute_all_string_decomposition(word, l))