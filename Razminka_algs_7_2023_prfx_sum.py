hght_wdth = input()

hght, wdth = hght_wdth.split()
hght, wdth = int(hght), int(wdth)

vector2D = [[] * wdth for _ in range(hght)]

for i in range(hght):
    row = input()
    vector2D[i] = list(map(int, row.split()))

pr_sm = [[0] * wdth for _ in range(hght)]

for i in range(hght):#насчитываем префиксные суммы по всему прямоугольнику
    for j in range(wdth):
        up = (0 if i == 0 else pr_sm[i - 1][j])  # прямоугольник сверху, если идем по верхней границе
        lf = (0 if j == 0 else pr_sm[i][j - 1])  # прямоугольник слева, если идем по левой границе
        df = (0 if (j == 0 or i == 0) else pr_sm[i - 1][
            j - 1])  # общее множество, которое нужно вычесть, если идем по верхней или левой границе
        pr_sm[i][j] = up + lf - df + vector2D[i][j]

maxS = 0  # длина стороны квадрата максимальной площади, заполненного марковками полностью
def rec_index(a, b):# проверка следующих значений по диагонали на пригодность в расчетах
    if a + 1 < hght and b + 1 < wdth and vector2D[a][b] == 0:
        a, b = a + 1, b + 1
        a, b = rec_index(a, b)
    return a, b
def diagonal_run(i, j):
    global maxS
    up, left, df = 0, 0, 0

    i, j = rec_index(i, j)  # найдем первое значение на диагонали с верхнего левого угла, не равное 0, чтобы следующее за ним было тоже не равно 0
    i, j = i + 1, j + 1
    i_brdr, j_brdr = i - 2, j - 2  # обновляем границы

    while i < hght and j < wdth:  # идем по диагонали
        if i_brdr > -1 and j_brdr > -1:
            df = pr_sm[i_brdr][j_brdr]
        if i_brdr > -1:
            up = pr_sm[i_brdr][j]
        if j_brdr > -1:
            left = pr_sm[i][j_brdr]

        sum_sqr = pr_sm[i][j] - up - left + df
        h, w = i - i_brdr, j - j_brdr

        if sum_sqr == h * w:
            if h > maxS and h > 1:
                maxS = h
            i, j = i + 1, j + 1
        else:
            i, j = rec_index(i, j)
            if i < hght - 1 and j < wdth - 1:
                i, j = i + 1, j + 1
                i_brdr, j_brdr = i - 2, j - 2  # обновляем границы
            else:
                i, j = i + 1, j + 1  # чтобы потом выйти из цикла while, так как уперлись в границы

for jj in range(0, wdth):  # идем по диагонялям от каждого квадрата сверху
    i, j = 0, jj
    diagonal_run(i, j)

for ii in range(1, hght):  # идем по диагонялям от каждого квадрата слева
    i, j = ii, 0
    diagonal_run(i, j)

print(maxS)








