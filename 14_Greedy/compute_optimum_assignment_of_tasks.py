import collections

tasks = [5,2,1,6,4,4]

def assign_optimum(tasks):
    tasks.sort()
    times = []
    for i in range(len(tasks) // 2):
        times.append(tasks[i] + tasks[~i])
    return max(times)

PairedTask = collections.namedtuple('PairedTasks', ('task1','task2'))
def optimum_task_assignment(task_durations):
    task_durations.sort()
    return [PairedTask(task_durations[i], task_durations[~i]) for i in range(len(task_durations) // 2)]


print(assign_optimum(tasks))
print(optimum_task_assignment(tasks))