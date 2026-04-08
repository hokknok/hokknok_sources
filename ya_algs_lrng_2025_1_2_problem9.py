import sys


def main():
    i, j  = map(int, input().split())
    ii,jj = map(int, input().split())

    if i < ii:
        i, ii = ii, i

    if j < jj:
        j, jj = jj, j

    if (i == ii and j - jj == 1) or (j == jj and i - ii == 1) or (j == jj and i == ii):
        x = 0
    elif i - ii == 1 and j - jj == 1:
        x = 1
    elif i == ii:
        x = (j - jj - 1) * 3
    elif j == jj:
        x = (i - ii - 1) * 3
    else:
        x = (i - ii - 1 + j - jj - 1) * 3 + 1

    print(x)
    return

if __name__ == '__main__':
    main()
