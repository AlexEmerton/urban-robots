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
            col_big_sum = col_compare           # update the biggest sum value
        col_compare = 0
    return col_big_sum


# print(largest_column_sum(Matrix, x, y))


def smallest_row_number(array, x_ax, y_ax):
    row_total = 0
    row_small_num = 0
    row_compare = 1.7976931348623157e+308       # kind of a "dirty" trick. Used a huge number to compare first element
    for i in range(x_ax):                       # against to make sure the conditional statement will execute on the
        for p in range(y_ax):                   # first run. Can (and should) be replaced with an array to select the
            row_total += array[i][p]            # first element but for the sake of simplicity is kept this way
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
            double_flag = True                  # second flag is used to display the 'NO', 'YES' values the way
            break                               # it was required to display
        c.clear()

    if double_flag:
        return 'YES'
    else:
        return 'NO'

# print(all_equal(Matrix, x, y))


def all_distinct(array, x_ax, y_ax):
    c = []
    flag = False
    found = False

    for i in range(x_ax):
        p = 1
        for k in range(y_ax):
            c.append(array[i][k])
        for j in range(len(c)):
            found = False
            while p < len(c):
                if c[p] == c[len(c) - 1] and c[j] != c[p]:      # a huge problem can be seen here. This kind of a
                    j += 1                                      # statement will be blind in case the first element
                    p = j + 1                                   # is also the one repeated. Python is a bit
                elif c[j] == c[p]:                              # problematic to work with when it comes to going
                    found = True                                # through arrays without using special libraries
                    break                                       # and/or loop structures (iterations). The bug is
                else:                                           # acknowledged and the pseudo-code version is provided
                    p += 1                                      # where such problem does not exist
        c.clear()
        if not found:                                           # This version of the task 4.4 was kept as a way to keep
            flag = True                                         # the project consistent
    if flag:
        return 'NO'
    else:
        return 'YES'

# print(all_distinct(Matrix, x, y))
