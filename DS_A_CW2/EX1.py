A = [1, 2, 5, 7]
B = [2, 5, 10]
p = 0
C = A
while p < len(B):
    # print(B[p], C[len(C)-1]) debug
    if B[p] > C[len(C)-1]:
        C.append(B[p])
    p += 1
print(C)
