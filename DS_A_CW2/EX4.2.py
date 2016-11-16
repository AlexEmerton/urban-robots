A = [0, 10, 25, 30, 45, 50, 60, 80, 90]


def equal_elements(array, ind1, ind2):
    if ind2 > len(array)-1:
        return False
    else:
        if array[ind1] == array[ind2]:
            return True
        elif array[ind2] == array[len(array) - 1]:
            ind1 += 1
            ind2 = ind1 + 1
            # print('moving to elements:', array[ind1], array[ind2])
            return equal_elements(array, ind1, ind2)
        else:
            # print('increasing ind2 from', array[ind1], array[ind2])
            return equal_elements(array, ind1, ind2 + 1)

print(equal_elements(A, 0, 1))
