A = [1, 2, 5, 7]
B = [2, 5, 10]
C = []
i = 0
p = 0
while i < len(A) and p < len(B):
    if A[i] == B[p]:
        C.append(A[i])
        i += 1
        p += 1
    elif A[i] < B[p]:
        i += 1
    else:
        p += 1
print(C)
