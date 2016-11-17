C = [-19, -10, -1, 0, 10, 18, 30, 40]
R = 20


def is_pair(array, ind1, ind2, diff):
    if ind2 > len(array) - 1:
        return False
    else:
        if abs(array[ind1] - array[ind2]) == diff or \
                (((array[ind1] < 0 and array[ind2] > 0) or (array[ind2] < 0 and array[ind1] > 0)) and
                 (abs(array[ind1]) + abs(array[ind2]) == diff)):
            print(array[ind1], array[ind2])
            return True
        elif array[ind2] == array[len(array) - 1]:
            ind1 += 1
            ind2 = ind1 + 1
            # print('moving to elements:', array[ind1], array[ind2])
            return is_pair(array, ind1, ind2, diff)
        else:
            # print('increasing ind2 from', array[ind1], array[ind2])
            return is_pair(array, ind1, ind2 + 1, diff)

print(is_pair(C, 0, 1, R))
