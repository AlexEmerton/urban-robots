A = [8, 10, 2, 3, 5, 16, 4]
B = [2, 3, 5]


def is_sub_array(array_1, array_2):
    c = []      # array for comparison
    p = 0
    found = False

    while p + len(array_2) - 1 < len(array_1):  # go through all elements of A
        for i in range(len(array_2)):           # go through 3 elements of A at a time
            c.append(A[p+i])                    # add elements to the array c
            if c == array_2:                    # comparison
                found = True
        c.clear()                               # reset the array
        p += 1                                  # increase starting index by 1
    return found

if is_sub_array(A, B):
    print('B is a sub-array of A!')
else:
    print('B is NOT a sub-array of A!')

