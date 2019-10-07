def sets_diff(A, B):
    """пробегает оба множества и создает новое из уникальных элементов А"""
    C = []
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                break
        else:
            C.append(A[i])
    print(C)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
B = [2, 4, 6, 8, 3323]
sets_diff(A, B)
