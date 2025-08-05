def generate(numRows):
        rows = [[] for _ in range(numRows)]
        rows[0].append(1)
        i = 1
        while i < numRows:
            row = [None] * i

            row[0], row[i - 1] = 1, 1
            for j in range(1, i - 1):
                row[j] = rows[i - 1][j - 1] + rows[i - 1][j]

            rows[i].append(row)

        print(rows)

generate(5)
