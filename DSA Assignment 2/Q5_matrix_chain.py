def matrix_chain(p):
    n = len(p) - 1

    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (m[i][k] + m[k+1][j]
                        + p[i] * p[k+1] * p[j+1])

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_order(s, i, j):
    if i == j:
        print("A" + str(i+1), end="")
    else:
        print("(", end="")
        print_order(s, i, s[i][j])
        print_order(s, s[i][j]+1, j)
        print(")", end="")


p = [30, 35, 15, 5, 10, 20, 25]

m, s = matrix_chain(p)

print("Minimum Cost:", m[0][5])
print("Optimal parenthesization:")
print_order(s, 0, 5)