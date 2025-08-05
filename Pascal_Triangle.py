def generate(numRows):
        rows = [[] for _ in range(1)]
        rows[0].append(1)
        print(rows)
        i = 1 #second row with 2 elements
        while i < numRows:
            row = [None] * (i + 1)

            row[0], row[-1] = 1, 1
            for j in range(1, i):
                row[j] = rows[i - 1][j - 1] + rows[i - 1][j]

            rows.append(row)
            print(rows)
            i += 1

        print(rows)

generate(5)
