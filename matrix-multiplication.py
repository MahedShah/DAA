def num_of_rows(m):
    return len(m)


def num_of_columns(m):
    return len(m[0])


def matrix_multiplication(m1, m2):
    rm = [[0] * num_of_rows(m1) for n in range(num_of_columns(m2))]
    if num_of_columns(m1) != num_of_rows(m2):
        return -1
    else:
        for i in range(len(m1)):
            for j in range(len(m1)):
                rm[i][j] = 0
                for k in range(len(m2)):
                    rm[i][j] = rm[i][j] + m1[i][k] * m2[k][j]
        return rm


a = [[6, 4, 9], [5, 2, 1]]
b = [[8, 6], [15, 10], [3, 7]]

print(matrix_multiplication(a, b))
