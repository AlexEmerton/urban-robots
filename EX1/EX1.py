A = [0, 5, 3, 6, 8, 7, 15, 9]
B = []

for i in range(len(A)):     # go through all elements of A
    if i != 0 and i != len(A)-1:    # set of rules fur extreme points below
        if (A[i - 1] < A[i] and A[i] > A[i + 1]) or (A[i - 1] > A[i] and A[i] < A[i + 1]):
            B.append(A[i])  # add extreme point to the array B

if len(B) == 0:
    print('Sorted!')
else:
    print('Extreme points:', B)
