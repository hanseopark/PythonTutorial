def numPos(k,n):
    if n ==1:
        return 1
    if k ==1:
        return n+numPos(k,n-1)
    return numPos(k-1,n)+numPos(k,n-1)

T= int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(numPos(k,n))


