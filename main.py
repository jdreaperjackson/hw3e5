# Recursive formulation:
# opt[i,j] = {1+ max{OPT[i+1,j],OPT[i,j+1]}}
#            {max{OPT[i+1,j],OPT[i,j+1]}}
#
# base case:
# OPT[m,n] = {1 if there is dirt @ m,n}
#            {0 otherwise}

def findPathWithMaximumDirt(matrix):
    def bestpath(matrix):
        N = len(matrix)
        NegINF = float('-inf')

        # base case
        opt = [[NegINF] * N for _ in range(N)]
        opt[N - 1][N - 1] = matrix[N - 1][N - 1]

        # filling up the opt
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if matrix[i][j] >= 0 and (i != N - 1 or j != N - 1):
                    opt[i][j] = max(opt[i + 1][j] if i + 1 < N else NegINF,
                                    opt[i][j + 1] if j + 1 < N else NegINF)
                    opt[i][j] += matrix[i][j]

        # return none if no such path exists which cleans at least one dirty cell
        if opt[0][0] < 0: return None

        # initialize the path with (0,0)
        path = [(0, 0)]
        i = j = 0

        # take the cell with maximum dp value and insert it in path
        while i != N - 1 or j != N - 1:
            if j + 1 == N or i + 1 < N and opt[i + 1][j] >= opt[i][j + 1]:
                i += 1
            else:
                j += 1
            path.append((i, j))
        return path

    cost = 0
    path = bestpath(matrix)
    print("The path to clean the maximum number of dirty cells:")
    print(path)

    # return 0 if no such path exists which cleans at least one dirty cell
    if path is None: return 0

    for i, j in path:
        cost += matrix[i][j]
        matrix[i][j] = 0
    print("The maximum number of dirty cells:")
    print(cost)

A = [[1, 1, 0, 0],
     [1, 0, 0, 0],
     [1, 1, 1, 1],
     [0, 0, 0, 1]]
findPathWithMaximumDirt(A)
