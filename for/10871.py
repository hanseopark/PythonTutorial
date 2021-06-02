N,X = map(int,input().split())
A = []
A = list(map(int,input().split()))
temp =[]
for i in range(N):
    if A[i]<X:
        temp.append(A[i])
        print(A[i], end=' ')
#print(int(temp))
