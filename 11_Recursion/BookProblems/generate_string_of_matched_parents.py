
def generate_balanced_parentheses(k):
    def dfs(left, right, curr, result=[]):
        if left > 0:
            dfs(left - 1, right, curr + '(')
        if left < right:
            dfs(left, right - 1, curr + ')')
        if not right:
            result.append(curr)
        return result
    return dfs(k,k,'')

print(generate_balanced_parentheses(3))


#My sol
def build_valid_k_paren(k):

    def bfs(curr, left, right):
        if len(curr) == 2*k:
            result.append(''.join(curr[::]))
            return

        if left < k:
            curr.append('(')
            bfs(curr, left + 1, right)
            curr.pop()
        if right < left:
            curr.append(')')
            bfs(curr, left, right + 1)
            curr.pop()
        return

    result = []
    bfs([], 0, 0)
    return result

print(build_valid_k_paren(3))


# Book sol
def is_valid_paren(l):

    matching = {')':'(','}':'{',']':'['}
    stack = []
    for p in l:
        if p in matching:
            if stack and stack[-1] == matching[p]:
                stack.pop()
            else:
                return False
        else:
            stack.append(p)
    return True if len(stack) == 0 else False

p1 = '()'
p2 = '(()())'
p3 = ')'

print(is_valid_paren(p3))