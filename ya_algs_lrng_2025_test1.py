import sys


def main():
    n = int(input())
    a = list(map(int, input().split()))

    sum = 0
    min, max = a[0], a[1]

    for i in range(n):
        if i % 2 == 0:
            sum += a[i]
            if a[i] < min: min = a[i]
        else:
            sum -= a[i]
            if a[i] > max: max = a[i]

    if max > min: sum += max * 2 - min * 2

    print(sum)

if __name__ == '__main__':
    main()
