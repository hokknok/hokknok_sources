from bisect import bisect_left, bisect_right
def main():
    txt = input()
    num = int(input())
    dct = []
    for i in range(num):
        dct.append(input())
    dct.sort()

    nw_txt, i ='', 0

    sqnsc = []

    while i < len(txt):
        k = bisect_left(dct, txt[i])
        while k < len(dct) and dct[k] == txt[i:i+len(dct[k])]:
            for j in range(len(sqnsc)):
                if sqnsc[j][-1] == i+len(dct[k]):
                    el = 0
                    break
                elif sqnsc[j][-1] == i:
                    el = i+len(dct[k])
            else sqnsc[j].append(i+len(dct[k]))
        #########################################
            k += 1
        #nw_txt += txt[i:i+len(dct[k-1])] + ' '
        i += len(dct[k-1])

    print(nw_txt)

if __name__ == '__main__':
    main()
