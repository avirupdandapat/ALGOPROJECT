def rotate(A):
    # transpose the matrix
    for i in range(len(A)):
        for j in range(i, len(A)):
            A[i][j], A[j][i] = A[j][i], A[i][j]
    print(A)
    N = len(A)
    # swap columns moving inwards from outwards
    for i in range(int(N / 2)):
        for j in range(N):
            A[j][i], A[j][N - 1 - i] = A[j][N - 1 - i], A[j][i]
    return A


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate(A))
A = "the sky is blue"
A = (str.split(A, ' ')[::-1])
print(A)
