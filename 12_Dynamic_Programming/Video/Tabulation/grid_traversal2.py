def grid_traveler(m, n):
    col = [0] * (m + 1)
    table = list(map(lambda x: [0] * (n + 1), col))
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if j + 1 <= n:
                table[i][j+1] += current
            if i + 1 <= m:
                table[i+1][j] += current
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in table]))
    return table[m][n]



print(grid_traveler(5, 4))
