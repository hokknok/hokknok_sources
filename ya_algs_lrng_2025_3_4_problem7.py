import time


def way4():
    n = 1 + int(input())
    dp = [[0] * n for _ in range(n)]  # [x][y] - [x] кол-во кубиков, [y] размер базы;
    dp[1][1] = 1

    for i in range(2, n, +1):
        for j in range(i, 0, -1):
            for ii in range(j - 1, 0, -1):  # i - (i - j) - 1 = j - 1
                dp[i][j] += dp[i - j][ii]
            if i == j:
                dp[i][j] += 1

    # n = int(input())
    # dp = [[0] * n for _ in range(n)]  # [x][y] - [x] кол-во кубиков, [y] размер базы;
    # dp[0][0] = 1
    #
    # for i in range(1, n, +1):
    #     for j in range(i, 0, -1):
    #         for ii in range(j - 1, 0, -1):  # i - (i - j) - 1 = j - 1
    #             dp[i][j] += dp[i - j][ii]
    #         if i == j:
    #             dp[i][j] += 1
    #         elif j - 1 == 0 and i - j == 1:
    #             dp[i][j] += 1
    #
    # print(dp)
    print(sum(dp[n-1]))


def way3():
    n = int(input())
    k = 2
    strs = [[0, 149]]
    tmp = set()
    while k <= n:
        for pos in strs:
            for i in range(len(pos)):
                if pos[i] > 0:
                    postmp = list(pos)
                    if i > 0:
                        postmp[i] -= 1
                        postmp[i - 1] += 1
                    else:
                        postmp[i] -= 1
                        postmp.insert(0, 0)
                    tmp.add(tuple(postmp))
        # tmp.add(tuple([, 150 - k]))
        strs[:] = list(tmp)
        tmp.clear()
        k += 1
    print(len(strs))


def way2():
    n = int(input())
    k = 2
    strs = [[1]]
    tmp = set()
    while k <= n:
        for str in strs:
            for i in range(len(str)):
                if i + 1 < len(str) and str[i] + 1 < str[i + 1]:
                    tmp_lvl_list = list(str)
                    tmp_lvl_list[i] = str[i] + 1
                    tmp_lvl = tuple(tmp_lvl_list)
                    tmp.add(tuple(tmp_lvl))
                    tmp_lvl = tuple()

            if str[0] > 1:
                tmp_lvl = (1,) + tuple(str)
                tmp.add(tuple(tmp_lvl))
                tmp_lvl = tuple()

        tmp.add(tuple([k]))
        strs[:] = list(tmp)
        tmp.clear()
        k += 1
    print(len(strs))


def way1():
    n = int(input())
    k = 2
    strs = [[1]]
    tmp = []
    while k <= n:
        for str in strs:
            for i in range(len(str)):
                if i + 1 < len(str) and str[i] + 1 < str[i + 1]:
                    tmp_lvl = str.copy()
                    tmp_lvl[i] = str[i] + 1
                    if tmp_lvl not in tmp:
                        tmp.append(tmp_lvl.copy())
                    tmp_lvl.clear()

            if str[0] > 1:
                tmp_lvl = str.copy()
                tmp_lvl = [1] + tmp_lvl
                if tmp_lvl not in tmp:
                    tmp.append(tmp_lvl.copy())
                tmp_lvl.clear()

        tmp.append([k])
        strs[:] = tmp
        tmp.clear()
        k += 1
        print(len(strs))


if __name__ == '__main__':
    start_time = time.time()  # ⏱️ Старт
    way4()
    end_time = time.time()  # ⏱️ Финиш
    # print(f"start_time: {start_time:.4f} сек")  # Вывод времени
    # print(f"end_time: {end_time:.4f} сек")  # Вывод времени
    # print(f"Время выполнения: {end_time - start_time:.4f} сек")  # Вывод времени
