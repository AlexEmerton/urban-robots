B = [19, 100, -1, 22, 66]
R = 20


def is_pair(array, ind1, ind2, diff):
    if ind2 > len(array) - 1:
        return False
    else:
        if abs(array[ind1] - array[ind2]) == diff:
            return True
        elif array[ind2] == array[len(array) - 1]:
            ind1 += 1
            ind2 = ind1 + 1
            # print('moving to elements:', array[ind1], array[ind2])
            return is_pair(array, ind1, ind2, diff)
        else:
            # print('increasing ind2 from', array[ind1], array[ind2])
            return is_pair(array, ind1, ind2 + 1, diff)

print(is_pair(B, 0, 1, R))
