class Name:
    def __init__(self, first_name, last_name):
        self.first_name, self.last_name = first_name, last_name

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __lt__(self, other):
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)

def eliminate_duplicate(A):
    A.sort()
    write_idx = 1
    for cand in A[1:]:
        if cand != A[write_idx -1]:
            A[write_idx] = cand
            write_idx += 1
    del A[write_idx]