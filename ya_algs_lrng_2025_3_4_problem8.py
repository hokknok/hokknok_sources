def way1():
    n = int(input())
    smpl_lst = {1: 1, 2: 1, 3: 1, 4: 2}

    for i in range(5, n + 1):
        dltl = int(i ** 0.5) + 1
        while dltl > 1:
            if i % dltl == 0 or i == n:
                if any(smpl_lst.get(i - j) == 2 for j in (1, 2, 3)):
                    smpl_lst[i] = 1
                else:
                    smpl_lst[i] = 2
                break
            dltl -= 1

    print(smpl_lst[n])

if __name__ == '__main__':
    way1()
