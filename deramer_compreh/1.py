def primal_c():
    M = []
    M.append(2)
    for i in range(1000):
        c = i + 3
        j = 0
        while j < len(M):
            if not c%M[j]:
                break
            j += 1
        else: M.append(c)
    print(M)


primal_c()

