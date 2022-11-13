

intervals = [[0,3],[2,6],[3,4],[6,9]]
def interval_cover(intervals):
    intervals.sort(key=lambda x: x[1])
    count = 0
    last_visit_time = float('-inf')
    for interval in intervals:
        if interval[0] > last_visit_time:
            last_visit_time = interval[1]
            count += 1
    return count


print(interval_cover(intervals))