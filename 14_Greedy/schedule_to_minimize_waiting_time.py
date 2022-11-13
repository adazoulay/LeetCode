

times = [2,5,1,3]
def minimum_total_time(times):
    times.sort()
    total_time = 0
    for i, service_time in enumerate(times):
        remaining_queries = len(times) - (i + 1)
        total_time += service_time * remaining_queries
    return total_time

print(minimum_total_time(times))