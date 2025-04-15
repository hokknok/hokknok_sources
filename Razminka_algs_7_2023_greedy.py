hght_wdth = input()

hght, wdth = hght_wdth.split()
hght = int(hght)
wdth = int(wdth)

line = [[] for _ in range(hght)]

for i in range(hght):
    line[i] = input()
    line[i] = line[i].split()
    line[i] = list(map(int, line[i]))

size = min(hght, wdth)

x1 = 0
x2 = x1 + size - 1
y1 = 0
y2 = y1 + size - 1
ln = y1

while size > 0:

    sqr_line = line[ln][x1:x2+1]

    if any(val == 0 for val in sqr_line) == True:
        x2 += 1  # смещаем вправо правую границу квадрата бегунка
        if x2 < wdth:  # если НЕ достигли правой границы
            x1 += 1  # смещаем вправо левую границу квадрата бегунка
            ln = y1
        else:  # если достигли правой границы
            x1 = 0  # и возвращаемся влево
            x2 = x1 + size - 1  # и возвращаемся влево
            y1 += 1  # смещаемся вниз
            y2 += 1  # смещаемся вниз
            ln = y1

        if y2 >= hght:  # если после смещений еще достигли и нижней границы и спускаться некуда
            size -= 1
            x1 = 0
            x2 = x1 + size - 1
            y1 = 0
            y2 = y1 + size - 1
            ln = y1

    else:
        ln += 1
        if ln == y2 + 1:
            break

print(size if size > 1 else 0)