def bin_srch(dct, el):
    left, right = 0, len(dct)

    while left < right:
        mid = (left + right) // 2
        if dct[mid][0] >= el:
            right = mid
        else:
            left = mid + 1

    if dct[left][0] == el:
        return left
    else:
        return -1


def main():
    txt, num = input(), int(input())
    dct = []
    for i in range(num):
        dct.append(input())

    i, sqnsc = 0, []

    while i < len(txt):
        k = bin_srch(dct, txt[i])
        if k == -1:
            i += 1
            continue
        while k < len(dct):
            ln_wrd = len(dct[k])
            if dct[k] != txt[i:i + ln_wrd]:  # после первого же несовпадения перебирать нет смысла
                k += 1
                continue
            el = i + ln_wrd - 1  # вычитаем 1, чтобы не записать лишнего
            j = 0
            for j in range(len(sqnsc)):  # перебираем все имеющиеся комбинации
                if sqnsc[j][-1] == el:  # уже есть комбинация, заканчивающаяся на такое слово
                    break  # поэтому ничего не добавляем в массив ответов
                elif sqnsc[j][-1] == i - 1:  # уже есть комбинация, которая подходит, как предыдущая. И, если она есть, то она единственная
                    sqnsc.append(sqnsc[j].copy())  # создаем еще один экземпляр для дополнения другими словами
                    sqnsc[j].append(el)  # дополнение корректной найденной комбинации
                    break
            else:
                if i == 0:
                    sqnsc.append([el])  # добавление новой корректной комбинации
            #########################################
            if len(sqnsc) != 0 and sqnsc[j][-1] == len(txt) - 1:
                # если уже есть хотя бы один ответ и перебрали всю строку txt
                prv = 0
                for el in sqnsc[j]:  # выводим ответ
                    print(txt[prv:el + 1], end=' ')
                    prv = el + 1
                return  # и выходим из функции
            k += 1
        i += 1


def bin_srch_deepseek(dct, el):
    """Бинарный поиск по первым буквам слов в словаре"""
    left, right = 0, len(dct)

    while left < right:
        mid = (left + right) // 2
        if dct[mid][0] >= el:
            right = mid
        else:
            left = mid + 1

    return left if left < len(dct) and dct[left][0] == el else -1


def main_deepseek():
    txt = input().strip()
    num = int(input())

    # Считываем словарь и сразу сортируем по первым буквам для бинарного поиска
    dct = sorted([input().strip() for _ in range(num)])

    # Используем BFS вместо множества комбинаций
    from collections import deque

    # Очередь для BFS: (позиция в тексте, путь разбиения)
    queue = deque([(0, [])])
    # Множество посещенных позиций для избежания повторений
    visited = [False] * (len(txt) + 1)
    visited[0] = True

    while queue:
        i, path = queue.popleft()

        # Если дошли до конца строки - нашли ответ
        if i == len(txt):
            # Формируем и выводим ответ
            result = []
            prev = 0
            for pos in path:
                result.append(txt[prev:pos + 1])
                prev = pos + 1
            print(' '.join(result))
            return

        # Бинарный поиск первого слова, начинающегося с txt[i]
        k = bin_srch_deepseek(dct, txt[i])
        if k == -1:
            continue

        # Проверяем все слова, начинающиеся с этой буквы
        while k < len(dct) and dct[k][0] == txt[i]:
            word = dct[k]
            word_len = len(word)
            end_pos = i + word_len - 1

            # Проверяем, что слово помещается и совпадает
            if end_pos < len(txt) and txt[i:i + word_len] == word:
                next_pos = end_pos + 1

                # Если еще не посещали эту позицию, добавляем в очередь
                if not visited[next_pos]:
                    visited[next_pos] = True
                    queue.append((next_pos, path + [end_pos]))

            k += 1

    # Если дошли сюда - разбиение не найдено
    print("Разбиение не найдено")
#проверка на дорогах
#мой друг Иван Лапшин
#горные ветры (Фильм берега)
#белые одежды (про науку)
def dp_main():
    txt, num = input(), int(input())
    dct = set()
    max_len = 0
    for i in range(num):
        wrd = input()
        max_len = ()

    st = [False] * len(txt)
    prv = [''] * len(txt)

    #for i in range()

    print(dct)

def gustokashin():
    s = '#' + input()
    s_len = len(s)
    poss_end = [False] * s_len
    prev_word = [' '] * s_len
    poss_end[0] = True
    words = set()
    n = int(input())
    max_len = 0

    for i in range(n):
        word = input()
        max_len = max(max_len, len(word))
        words.add(word)

    print(words)

    for i in range(1, s_len):
        for j in range(min(max_len, i)):
            if poss_end[i - j - 1] and s[i - j:i + 1] in words:
                poss_end[i] = True
                prev_word[i] = s[i - j:i + 1]
                break

    now = s_len - 1
    ans = []

    print(poss_end)
    print(prev_word)

    while now > 0:
        ans.append(prev_word[now])
        now -= len(prev_word[now])

    print(*ans[::-1])

if __name__ == '__main__':
    #dp_main()
    gustokashin()
    #main_deepseek()
