x, y = 5, 5
Matrix = [[0 for x in range(x)] for y in range(y)]
# initialising Matrix and some test values inside of it
Matrix[0][1] = 5
Matrix[1][1] = 1
Matrix[2][0] = 1
Matrix[2][1] = 1
Matrix[2][2] = 1
Matrix[2][3] = 1
Matrix[2][4] = 1
Matrix[3][0] = 1
Matrix[3][1] = 2
Matrix[3][2] = 3
Matrix[3][3] = 4
Matrix[3][4] = 5
Matrix[4][1] = 5


def largest_column_sum(array, x_ax, y_ax):
    col_compare = 0
    col_big_sum = 0

    for i in range(x_ax):
        for p in range(y_ax):
            col_compare += array[p][i]
        if col_compare > col_big_sum:
            col_big_sum = col_compare
        col_compare = 0
    return col_big_sum


# print(largest_column_sum(Matrix, x, y))


def smallest_row_number(array, x_ax, y_ax):
    row_total = 0
    row_small_num = 0
    row_compare = 1.7976931348623157e+308

    for i in range(x_ax):
        for p in range(y_ax):
            row_total += array[i][p]
        if row_total < row_compare:
            row_compare = row_total
            row_small_num = i
        row_total = 0
    return row_small_num

# print(smallest_row_number(Matrix, x, y))


def all_equal(array, x_ax, y_ax):
    double_flag = False
    flag = False
    c = []
    for i in range(x_ax):
        for p in range(y_ax):
            c.append(array[i][p])
        for el in range(len(c)):
            if c[el] != 1:
                flag = False
                break
            else:
                flag = True
        if flag:
            double_flag = True
            break
        c.clear()

    if double_flag:
        return 'YES'
    else:
        return 'NO'

# print(all_equal(Matrix, x, y))


def all_distinct(array, x_ax, y_ax):
    d = []
    c = []
    for i in range(x_ax):
        for p in range(y_ax):
            c.append(Matrix[i][p])
        d.append(c)
        print(d)
        c.clear()
    return d

print(all_distinct(Matrix, x, y))
