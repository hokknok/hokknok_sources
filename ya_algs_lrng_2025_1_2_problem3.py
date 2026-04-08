import sys

def main():
    str_srtd = sorted(input())
    #print(str_srtd)
    pnter = str_srtd[0]
    vl = 0
    j = 0

    for i in range(len(str_srtd)):
        if str_srtd[i] == pnter:
            j += 1
        else:
            vl += (len(str_srtd) - j) * j
            j = 1
            pnter = str_srtd[i]
    vl += (len(str_srtd) - j) * j

    vl = vl/2 + 1

    print(int(vl))

if __name__ == '__main__':
    main()
