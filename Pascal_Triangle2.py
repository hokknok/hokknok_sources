def getRow(rowIndex):
    # row1 = [1];
    # for i in range(1, rowIndex + 2):
    #     row = [1] * i;
    #     for j in range(1, i - 1):
    #         row[j] = row1[j - 1] + row1[j]
    #     row1 = row
    # return row1

    c = [1] * (rowIndex + 1)
    for i in range(1, rowIndex + 1):
        c[i] = c[i - 1] * (rowIndex - i + 1) // i
    return c


print(getRow(10000))
