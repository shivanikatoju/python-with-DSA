def create_2d_list(rows, cols, start):
    matrix = []
    current_value = start
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(current_value)
            current_value += 1
        matrix.append(row)

    return matrix

def addMatrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def subMatrix(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mulMatric(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]



if __name__ == '__main__':
    a = input("enter number of rows, coloums and stating value: ").split(' ')
    rows = int(a[0])
    cols = int(a[1])
    start = int(a[2])

    b = input("enter number of rows, coloums and stating value: ").split(' ')
    rowsb = int(b[0])
    colsb = int(b[1])
    startb = int(b[2])

    result = create_2d_list(rows, cols, start)
    resultb = create_2d_list(rowsb, colsb, startb)

    print("MATRIX 1")
    for row in result:
        print(row)

    print()

    print("MATRIX 2")
    for row in resultb:
        print(row)

    print()

    if rows == rowsb and cols == colsb:
        result_sum = addMatrix(result, resultb)
        print("SUM OF MATRICES")
        for row in result_sum:
            print(row)

        print()

        result_diff = subMatrix(result, resultb)
        print("DIFF OF MATRICES")
        for row in result_diff:
            print(row)
    else:
        print("Matrices must have the same dimensions to be added/subtracted")
