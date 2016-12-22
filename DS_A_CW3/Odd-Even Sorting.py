A = [1, 7, 8, 11, 14, 16]

i = 0
even_array = []
odd_array = []

# B = [1, 7, 11, 8, 14, 16]
# All odd elements occur before even ones. Sorted in increasing order
# Algorithm should not exceed O(n) complexity


def is_odd(x):
    if x % 2 != 0:
        return True
    else:
        return False

while i <= len(A)-1:
    if is_odd(A[i]):
        odd_array.append(A[i])
    else:
        even_array.append(A[i])
    i += 1

B = odd_array + even_array

print(B)
