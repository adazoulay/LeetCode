# How it comes up in problems:
# 1: Use 9_sorting to make subsequent steps in algo simpler. Can use built in sort optional custom comparator
# 2: Design a custom 9_sorting routine. Use BST, 6_Heap or array indexed by values

# Use 9_sorting as preprocessing to speed up searching

l = [1, 2, 4, 3, 5, 0, 11, 21, 100]
y = sorted(l, key=lambda x: str(x), reverse=True)  # Does not mutate the list
l.sort(key=lambda x: str(x), reverse=True)  # Mutates the array
print(l,y)


class Student(object):
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.name < other.name

students = [
    Student('A', 4.0),
    Student('B', 3.0),
    Student('C', 2.0),
    Student('D', 3.2)
]

# Sorts according to lt defined in class, students remains unchanged
students_sorted_by_name = sorted(students)
print(students_sorted_by_name)

# Sorts students by gpa, in place, mutates the array
students.sort(key=lambda student: student.gpa)
print(students)