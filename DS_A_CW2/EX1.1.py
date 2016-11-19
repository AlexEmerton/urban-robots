A = [1, 2, 5, 7]
B = [2, 5, 10]


def union(array_a, array_b):
    c = []

    i = 0
    p = 0
    o = 0

    tot_len = len(array_a) + len(array_b)
    while len(c) != tot_len:
        if len(array_a) == i:
            c += array_b[p:]
        elif len(array_b) == p:
            c += array_a[i:]
        elif array_a[i] < array_b[p]:
            c.append(array_a[i])
            i += 1
        else:
            c.append(array_b[p])
            p += 1

    while o < len(c) - 1:
        if c[o] == c[o + 1]:
            c.remove(c[o + 1])
        else:
            o += 1

    return c

print(union(A, B))
