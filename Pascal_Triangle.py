def generate(numRows):
        rows = []

        for i in range(numRows):
                row = [None] * (i + 1)
                row[0], row[-1] = 1, 1
                for j in range(1, i):
                        row[j] = rows[i - 1][j -1] + rows[i - 1][j]

                rows.append(row)

        return(rows)



print(generate(5))
