def goal(size):
    x = y = size - 1
    matrix = [[x + y * size for x in range(size)] for y in range(size)]

    return matrix

m = goal(3)
for row in m:
    print(row)