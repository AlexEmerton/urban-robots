A = [10, 8, 1, 3, 15]
B = []

# B = [2, 3, 1, 0, 4]
# The elements of B are indices of the elements of A
# B is sorted with respect to A

sorted_A = sorted(A)
# sorted_A = [1, 3, 8, 10, 15]

for x in range(len(sorted_A)):
    for y in range(len(A)):
        if sorted_A[x] == A[y]:
            B.append(y)

print(B)
