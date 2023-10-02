def matrix_chain_order(dims):
    n = len(dims) - 1  # Number of matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for chain_length in range(2, n + 1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s

def optimal_parenthesization(s, i, j):
    if i == j:
        return f"M{i}"
    else:
        k = s[i][j]
        left_chain = optimal_parenthesization(s, i, k)
        right_chain = optimal_parenthesization(s, k + 1, j)
        return f"({left_chain} × {right_chain})"


matrix_dims = [10, 30, 5, 60]  # Dimensions of matrices: A1(10x30), A2(30x5), A3(5x60)
m, s = matrix_chain_order(matrix_dims)
optimal_parentheses = optimal_parenthesization(s, 1, len(matrix_dims) - 1)
print("Optimal Parenthesization:", optimal_parentheses)
print("Minimum Scalar Multiplications:", m[1][len(matrix_dims) - 1])
