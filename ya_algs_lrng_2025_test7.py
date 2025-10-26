import sys

fgr = ''
count = 0


def cycle_my(fld):
    global fgr, count

    if fld == fgr:
        count += 1
        # print("fld = ", fld)
        # print("fgr = ", fgr)
        # print("count = ", count)
    else:
        fgr = fld
        count = 0

    if count == 4 and fgr != '.':
        print("Yes")
        return True


def main():
    n, m = map(int, input().split())
    field = []
    global fgr, count

    for i in range(n):
        field.append(input())

    for i in range(n):
        fgr = 'Y'
        count = 0
        for j in range(m):
            if cycle_my(field[i][j]):
                return
            j += 1

    for j in range(m):
        fgr = 'Y'
        count = 0
        for i in range(n):
            if cycle_my(field[i][j]):
                return
            i += 1
    ######################################################diagonals
    for i in range(n - 1, -1, -1):  # диагонали от левого нижнего угла по строкам вверх / (верхняя половина)
        j = 0
        fgr = "Y"
        ind = i
        count = 0
        while j < m and ind >= 0:
            if cycle_my(field[ind][j]):
                return
            j += 1
            ind -= 1

    for j in range(m):  # диагонали от левого нижнего угла по стобцам вправо / (нижняя половина)
        i = n - 1
        fgr = "Y"
        ind = j
        count = 0
        while ind < m and i >= 0:
            if cycle_my(field[i][ind]):
                return
            i -= 1
            ind += 1

    for j in range(m):  # диагонали от левого верхнего угла по столбцам вниз \ (верхняя половина)
        i = 0
        fgr = "Y"
        ind = j
        count = 0
        while i < n and ind < m:
            if cycle_my(field[i][ind]):
                return
            i += 1
            ind += 1

    for i in range(n):  # диагонали от левого верхнего угла по строкам вниз \ (нижняя половина)
        j = 0
        fgr = "Y"
        ind = i
        count = 0
        while ind < n and j < m:
            if cycle_my(field[ind][j]):
                return
            j += 1
            ind += 1

    print("No")
    return


if __name__ == '__main__':
    main()
