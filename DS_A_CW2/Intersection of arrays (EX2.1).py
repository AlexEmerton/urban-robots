A = [1, 2, 5, 7]
B = [2, 5, 10]


def intersection(array_a, array_b):
    c = []
    i = 0
    p = 0

    while i < len(array_a) and p < len(array_b):
        if array_a[i] == array_b[p]:
            c.append(array_a[i])
            i += 1
            p += 1
        elif array_a[i] < array_b[p]:
            i += 1
        else:
            p += 1
    return c

print(intersection(A, B))
