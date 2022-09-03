def maxtrix_search(A, x):
    row, col = 0, len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return [row,col]
        if A[row][col] < x:
            row += 1
        elif A[row][col] > x:
            col -= 1
    return -1



matrix = [[-1,2,4,4,6],[1,5,5,9,21],[3,6,6,9,22],[3,6,8,10,24],[6,8,9,12,25],[8,10,12,13,40]]

print(maxtrix_search(matrix,7))