import time
import random

def main1(test_string):
    #r = list(input())
    r = test_string
    sd = 'L'
    ans, i, ind = 0, 0, 0

    while i < len(r):
        if r[i] == 'B':
            ans += 1
        if r[i] == sd:
            ind += 1
            for j in range(i + 1, len(r)):
                if r[j] == 'B':
                    ans += 1
                elif r[j] != r[i]:
                    ans += 1
                    if ind >= 2:
                        sd = r[j]
                    i = j
                    ind = 0
                    break
                elif r[j] == r[i]:
                    ind += 1
            else:
                if (r[i] == 'R' or r[i] == 'B') and ind > 1:
                    ans += 2
                else:
                    ans += 1
                i = len(r)
        else:
            if i == len(r) - 1 and (r[i] == 'R' or r[i] == 'B'):
                ans += 1
            i += 1

    print(ans)

def main2(test_string):
    # r = list(input())
    r = test_string
    resL, resR = 0, 1

    for i in range(len(r)):
        if r[i] == 'L':
            resL = min(resL + 1, resR + 1)
            resR = min(resL + 1, resR)
        if r[i] == 'R':
            resL = min(resL, resR + 1)
            resR = min(resL + 1, resR + 1)
        if r[i] == 'B':
            resL = min(resL + 1, resR + 2)
            resR = min(resL + 2, resR + 1)

    print(min(resL+1, resR))


def main3(test_string):
    #s = input()
    s = test_string

    if len(s) == 0: return 1

    mapping = {"L": 1, "R": 0, "B": 1}
    l = [mapping[c] for c in s]
    mapping = {"L": 0, "R": 1, "B": 1}
    p = [mapping[c] for c in s]

    p_flag = 1
    l_flag = 0
    right = 1
    min = 0

    m1 = l[0]
    m2 = p[0]

    while right < len(s):

        if m1 + l[right] + l_flag > m2 + p[right] + p_flag:
            min = min + m2 + p_flag
            if right == len(s) - 1:
                min = min + p[right]
                p_flag = 0
                break
            m1 = l[right]
            m2 = p[right]
            right = right + 1
            p_flag = 0
            l_flag = 1

        elif m1 + l[right] + l_flag < m2 + p[right] + p_flag:
            min = min + m1 + l_flag
            if right == len(s) - 1:
                if p[right] + p_flag <= l[right] + l_flag:
                    min = min + p[right] + p_flag
                    p_flag = 0
                else:
                    min = min + l[right]
                break
            m1 = l[right]
            m2 = p[right]
            right = right + 1
            p_flag = 1
            l_flag = 0
        else:
            if right == len(s) - 1:
                if p_flag == 1:
                    min = min + m1 + l[right]
                else:
                    min = min + m2 + p[right]
                p_flag = 0
                break
            m1 = m1 + l[right]
            m2 = m2 + p[right]
            right = right + 1

    if p_flag == 1:
        min = min + 1
    print(min)

if __name__ == '__main__':

    k = 1000000
    while k < 1000000000:
        test_string = ''.join(random.choices('LRB', weights=[0.4, 0.4, 0.4], k=k))

        # выбор только из 'L'
        # test_string = ''.join(random.choices(['L'], k=k))  # всегда 'L'

        # выбор только из 'R'
        # test_string = ''.join(random.choices(['R'], k=k))  # всегда 'R'

        # # выбор только из 'B'
        # test_string = ''.join(random.choices(['B'], k=k))  # всегда 'B'

        # # Или строгое чередование:
        # test_string = ''.join('L' if i % 2 == 0 else 'R' for i in range(k))

        # # Большинство 'B' с редкими L/R
        # test_string = ''.join(random.choices('LRB', weights=[0.05, 0.05, 0.9], k=k))

        start_time = time.time()
        print("Ответ: ", end='')
        main1(test_string)

        end_time = time.time()
        print(f"{f'{len(test_string):,}'.replace(',', ' ')}  млн. символов. Время выполнения метода без ДП(мой метод): {end_time - start_time:.4f} секунд")
        print()

        start_time = time.time()
        print("Ответ: ", end='')
        main2(test_string)

        end_time = time.time()
        print(f"{f'{len(test_string):,}'.replace(',', ' ')}  млн. символов. Время выполнения метода c ДП: {end_time - start_time:.4f} секунд")
        print()

        start_time = time.time()
        print("Ответ: ", end='')
        main3(test_string)

        end_time = time.time()
        print(f"{f'{len(test_string):,}'.replace(',', ' ')} млн. символов. Время выполнения метода без ДП(метод Саши): {end_time - start_time:.4f} секунд")
        print()
        k *= 10