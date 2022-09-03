def test_Callatz_conjecture(k):
    visited = set()
    for i in range(2, k + 1, 2):
        num = i
        current_iter = set()
        while num != 1:
            if num in current_iter:
                return False
            current_iter.add(num)
            if not num % 2:
                num = num / 2
            else:
                if num in visited:
                    visited.add(i)
                    break
                num = 3*num + 1
    return True

print(test_Callatz_conjecture(500))