import collections


def can_form_palindrome(s):
    return (v % 2 for v in collections.Counter(s).values()) <= 1