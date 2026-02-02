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
            el = 0
            for j in range(len(sqnsc)):
                if sqnsc[j][-1] == i+len(dct[k]):
                    el = 0
                    break
                elif sqnsc[j][-1] == i - 1:
                    el = j + i + len(dct[k]) - 1
            else:
                sqnsc[el - i + len(dct[k]) - 1].append(i + len(dct[k]) - 1)
                if i == len(txt) - 1 and sqnsc[el - i + len(dct[k]) - 1][-1] == i:
                    print(sqnsc[el - i + len(dct[k]) - 1])
        #########################################
            k += 1
        i += 1

if __name__ == '__main__':
    main()
