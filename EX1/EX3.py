A = [-100, -60, -40, -10, 0, 10, 30, 40, 50, 70, 90, 100]
B = []
R = 20
b = 0
c = 1


def is_pair(array, ind1, ind2, diff):   # returns True if the pair of numbers with a certain difference exists
    if abs(array[ind1] - array[ind2]) == diff or \
            ((array[ind1] < 0 or array[ind2] < 0) and (abs(array[ind1]) + abs(array[ind2]) == diff)):
        # set of rules for identifying the difference between both positive and negative numbers
        return True
    else:
        return False

while b < (len(A)) and c < (len(A)):    # go through all elements of array A
    if A[c] == A[len(A)-1] and is_pair(A, b, c, R) == False:    # check if at the last pair of elements in array
        b += 1                                                  # if its not the pair required increase both
        c = b + 1                                               # index one (b) and index two (c)
    elif is_pair(A, b, c, R):                                   # check if the pair is right
        B.append([A[b], A[c]])                                  # add to array if it is
        b += 1                                                  # increase both indexes b and c
        c = b + 1   # index c should always be one in front of b so it doesnt check itself
    else:
        c += 1      # else continue increasing index c >> go further through the array seaching for pairs

if len(B) != 0:
    print('Found:', B)
else:
    print('No matches!')
