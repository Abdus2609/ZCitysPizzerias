def rangeChecker(num, lowerLimit, upperLimit):
    if num < lowerLimit or num > upperLimit:
        raise Exception("Sorry, this input is out of range.")
    
    return num


def translate(str):
    nums = str.split()
    ints = [int(x) for x in nums]
    
    return ints


def genMatrix(dim):
    matrix = []
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(0)
        matrix.append(row)
    
    return matrix


def updateCity(mat, coord, dim):
    x = coord[0] - 1
    y = coord[1] - 1
    r = coord[2]
    mat[y][x] += 1
    for i in range(1, r + 1):
        if (y - i) >= 0:
            mat[y - i][x] += 1
        if (y + i) < dim:
            mat[y + i][x] += 1
        if (x - i) >= 0:
            mat[y][x - i] += 1
        if (x + i) < dim:
            mat[y][x + i] += 1

        if (x - i) >= 0 and (y - i) >= 0:
            mat[y - i][x - i] += 1
        if (x - i) >= 0 and (y + i) < dim:
            mat[y - i][x + i] += 1
        if (x + i) < dim and (y - i) >= 0:
            mat[y + i][x - i] += 1
        if (x + i) < dim and (y + i) < dim:
            mat[y + i][x + i] += 1
            
    return mat


NM = translate(input())
NM = [rangeChecker(x, 1, 10000) for x in NM]

N = NM[0]
city = genMatrix(N)

coords = []
M = NM[1]

for i in range(M):
    coord = translate(input())
    points = [rangeChecker(n, 1, N) for n in [coord[0], coord[1]]]
    R = rangeChecker(coord[2], 1, 100)
    points.append(R)
    coords.append(points)

a = 0
while a < M:
    city = updateCity(city, coords[a], N)
    a += 1

listOfRanges = [num for rows in city for num in rows]
print(max(listOfRanges))