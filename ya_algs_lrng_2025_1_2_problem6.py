import sys


def main():
    n, m = map(int, input().split())
    table = []
    table_r = []
    table_c = []

    for i in range(n):
        row = input()
        table.append([1 if ch == '?' else 0 for ch in row])
        table_r.append([1 if ch == '+' or ch == '?' else -1 for ch in row])
        table_c.append([-1 if ch == '-' or ch == '?' else 1 for ch in row])

    best_rws = {}
    best_clm = {}

    max_rw = sum(table_r[0])
    for i in range(n):
        sm_rw = sum(table_r[i])
        if sm_rw >= max_rw:
            if sm_rw > max_rw:
                best_rws.clear()
                max_rw = sm_rw
            best_rws[str(i)] = sm_rw

    max_clm = sum(table_c[i][0] for i in range(n))
    for j in range(m):
        sm_cl = sum(table_c[i][j] for i in range(n))
        if sm_cl <= max_clm:
            if sm_cl < max_clm:
                best_clm.clear()
                max_clm = sm_cl
            best_clm[str(j)] = sm_cl

    for key, value in best_rws.items():
        for cl_key, cl_value in best_clm.items():
            if table[int(key)][int(cl_key)] != 1:
                diff = value - cl_value
                print(diff)
                return
            else:
                diff = value - cl_value - 2

    print(diff)
    return


if __name__ == '__main__':
    main()
