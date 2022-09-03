import collections


def merge_intervals(intervals):
    stack = []
    intervals.sort(key=lambda x:x[0])
    print(intervals)
    for i in intervals:
        if not stack:
            stack.append(i)
        elif stack[-1][-1] < i[0]:
            stack.append(i)
        elif stack[-1][-1] >= i[0]:
            stack[-1] = [min(stack[-1][0],i[0]),max(stack[-1][1],i[1])]
    return stack

l = [[-4,-1],[0,2],[3,6],[7,9],[11,12],[14,17],[1,8]]

print(merge_intervals(l))

Interval = collections.namedtuple('Interval',('left','right'))
def add_interval(disjoint_intervals, new_interval):
    i, result = 0, []
    while i < len(disjoint_intervals) and new_interval.left > disjoint_intervals[i].right:
        result.append(disjoint_intervals[i])
        i += 1
    while i < len(disjoint_intervals) and new_interval.right >= disjoint_intervals[i].left:
        new_interval = Interval((min(new_interval.left, disjoint_intervals[i].left), max(new_interval.right, disjoint_intervals[i].right)))
    i += 1
    return result + [new_interval] + disjoint_intervals[i:]