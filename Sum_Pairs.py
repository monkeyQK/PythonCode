import time


def sum_pairs(ints, s):
    p1 = 0
    li = []
    for i in ints:
        p1 = p1 + 1
        p2 = 0
        for j in ints[p1:]:
            if i + j == s:
                li.append([p1 - 1, p2 + p1])
            p2 += 1

    if len(li) == 0:
        return None

    a, b = sorted(li, key=lambda x: x[1])[0]

    return [ints[a], ints[b]]


start_time = time.time()
temp = sum_pairs([10, 5, 2, 3, 7, 5], 10)
end_time = time.time()
print(temp, end_time - start_time)


def sum_pairs_god(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)
