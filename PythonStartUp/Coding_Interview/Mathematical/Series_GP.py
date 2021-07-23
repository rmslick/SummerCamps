def Nth_term(A,R,N):
    a=4
    for i in range(N-1):A*=R
    print(A)
Nth_term(4,3,3)