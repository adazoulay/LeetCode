

def compute_integer_square_root(number):
    left, right = 0, number
    while left <= right:
        mid = (left + right) // 2
        if mid**2 <= number:
            left = mid + 1
        elif mid**2 > number:
            right = mid - 1
    return left - 1

print(compute_integer_square_root(25))