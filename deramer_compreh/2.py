def Selection(M):
    for i in range(len(M)):
        for j in range(len(M) - i - 1):
            if M[i + j + 1] < M[i]:
                M[i], M[i + j + 1] = M[i + j + 1], M[i]
    print(M)


P = [9,3,2,4,1,5,8,6,7]
Selection(P)
