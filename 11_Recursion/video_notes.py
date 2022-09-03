#Use debugger to debug stack calls
# https://www.youtube.com/watch?v=IJDJ0kBx2LM

def reverse_string(str):
    if len(str) == 0:
        return ""
    return reverse_string(str[1:]) + str[0]

s = "abcd"
print("reverse str:", reverse_string(s))


def palindrome(str):
    if len(str) == 0 or len(str) == 1:
        return True
    if str[0] == str[-1]:
        return palindrome(str[1:-1])
    return False

i = "racecar"
print("palindrome:", palindrome(i))

def decimal_to_bin(number):
    if number == 0:
        return ""
    div, mod = divmod(number, 2)
    return decimal_to_bin(div) + str(mod)

print("decimal_to_bin:", decimal_to_bin(116))
#1110100

def sum_of_natural_numbers(n):
    if n == 0:
        return 0
    return n + sum_of_natural_numbers(n - 1)

print("sum_of_natural_numbers:", sum_of_natural_numbers(5))

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("fib:", fib(3))